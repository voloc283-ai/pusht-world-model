# pusht_pose.py - ước lượng tư thế (x, y, góc) khối T từ ảnh 96x96
import numpy as np
import cv2

S = 96 / 512                                                           # hệ số đổi toạ độ 0..512 sang pixel 0..96
BAR = np.array([(-60, 30), (60, 30), (60, 0), (-60, 0)], float)        # thanh ngang của chữ T
STEM = np.array([(-15, 30), (-15, 120), (15, 120), (15, 30)], float)   # thân dọc của chữ T


def block_mask(img):
    """Chọn các pixel màu xám-xanh (khối T). Robot xanh đậm và đích xanh lá bị loại bằng ngưỡng màu."""
    im = img.astype(int)
    R, G, B = im[..., 0], im[..., 1], im[..., 2]
    return ((B - R >= 15) & (B - R <= 75) & (G - R >= 5) & (G - R <= 45) & (im.mean(-1) < 205)).astype(np.float32)


def agent_centroid(img):
    """Tâm hình tròn xanh (robot), trả về toạ độ 0..512."""
    im = img.astype(int)
    ys, xs = np.nonzero(im[..., 2] - im[..., 0] > 120)
    if len(xs) < 5:
        return np.array([np.nan, np.nan])
    return np.array([xs.mean() + 0.5, ys.mean() + 0.5]) / S


def raster(x, y, th, size=96, ss=4):
    """Vẽ chữ T ở tư thế (x, y, góc) lên lưới 96x96, giá trị 0..1 (ss = siêu lấy mẫu cho viền mịn)."""
    c, s = np.cos(th), np.sin(th)
    Rm = np.array([[c, -s], [s, c]])
    m = np.zeros((size * ss, size * ss), np.uint8)
    for poly in (BAR, STEM):
        w = (poly @ Rm.T + [x, y]) * S * ss
        cv2.fillPoly(m, [np.round(w - 0.5).astype(np.int32)], 1)
    return cv2.resize(m.astype(np.float32), (size, size), interpolation=cv2.INTER_AREA)


def iou(a, b):
    return np.minimum(a, b).sum() / (np.maximum(a, b).sum() + 1e-9)


def estimate(img):
    """Trả về ((x, y, góc), độ khớp IoU). Thử 72 góc, chọn góc khớp nhất rồi tinh chỉnh từng toạ độ."""
    m = block_mask(img)
    ys, xs = np.nonzero(m)
    if len(xs) < 20:
        return np.array([np.nan] * 3), 0.0
    cx, cy = (xs.mean() + 0.5) / S, (ys.mean() + 0.5) / S
    best = (-1.0, None)
    for th in np.linspace(-np.pi, np.pi, 72, endpoint=False):
        r = raster(256, 256, th)
        yy, xx = np.nonzero(r > 0.5)
        ox, oy = (xx.mean() + 0.5) / S - 256, (yy.mean() + 0.5) / S - 256     # tâm khuôn lệch so với gốc toạ độ khối
        p0 = (cx - ox, cy - oy, th)
        sc = iou(raster(*p0), m)
        if sc > best[0]:
            best = (sc, p0)
    sc, p = best
    p = np.array(p, float)
    step = np.array([8.0, 8.0, 0.08])
    for _ in range(40):                                                         # tinh chỉnh từng toạ độ, giảm dần bước
        improved = False
        for k in range(3):
            for d in (-1, 1):
                q = p.copy()
                q[k] += d * step[k]
                s2 = iou(raster(*q), m)
                if s2 > sc:
                    sc, p, improved = s2, q, True
        if not improved:
            step *= 0.5
            if step[0] < 0.2:
                break
    p[2] = (p[2] + np.pi) % (2 * np.pi) - np.pi
    return p, sc


def work(img):
    return estimate(img)
