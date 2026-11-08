# World Model cho PushT

Mã nguồn và tư liệu của bài toán học quy luật tương tác giữa robot và khối chữ T. World Model dự đoán thay đổi tư thế vật từ trạng thái và hành động; phần mở rộng dùng Diffusion để sinh ứng viên và World Model để lựa chọn.

## Xem chương trình và kết quả

- [Notebook gồm toàn bộ code và output lưu sẵn](PushT_WorldModel.ipynb)
- [Bản HTML được cung cấp cùng notebook](PushT_WorldModel.html) — tải về và mở bằng trình duyệt
- [Mã ước lượng tư thế khối T](pusht_pose.py)
- [Hình và GIF trích từ output notebook](results/notebook_figures/)
- [Log output đã lưu](results/notebook_stdout.txt)
- [Video quay màn hình MP4](media/screen_recording_original.mp4)
- [Danh mục tệp và mã băm Git](ARTIFACT_MANIFEST.json)

## Demo

Mỗi GIF so sánh cùng một seed: bên trái **Chỉ Diffusion**, bên phải **Diffusion + World Model vòng 1**. Seed 4036 và 4093 là các ví dụ được chọn vì có cải thiện rõ; seed 4000 cho ví dụ cả hai cấu hình đều thành công. Các clip minh họa không thay thế đánh giá trên toàn bộ tập seed.

### Seed 4000

![Demo seed 4000](media/clip_seed4000.gif)

### Seed 4036

![Demo seed 4036](media/clip_seed4036.gif)

### Seed 4093

![Demo seed 4093](media/clip_seed4093.gif)

Video đi kèm: [mở hoặc tải bản MP4](media/screen_recording_original.mp4). Đây là bản quay màn hình demo, không phải bản ghi chứng minh một lần huấn luyện mới.

## Hiện trạng và phạm vi

Notebook được cung cấp để tìm hiểu phương pháp và đã có output của một lần chạy trước. Các số liệu, hình và demo lưu sẵn **không phải một lần chạy lại toàn bộ mới được nhóm xác nhận**. Chưa huấn luyện hoặc đánh giá lại khi chuẩn bị bản nộp này.

| Tư liệu | Nguồn và giới hạn |
|---|---|
| Notebook, HTML, ba GIF và video MP4 | Các tệp có trong thư mục dự án hiện tại |
| `pusht_pose.py` | Tách nguyên mã từ ô ghi file trong notebook |
| `results/notebook_figures` và log | Trích output đã lưu, không phát sinh phép đo mới |

Repository hiện chỉ giữ notebook, HTML, mã hỗ trợ, output đã lưu, hình kết quả, GIF demo và video MP4. Các tệp dữ liệu huấn luyện, checkpoint và kết quả trung gian cũ đã được loại khỏi nhánh chính. Để chạy lại đầy đủ cần tải dữ liệu và tự tạo các trọng số cùng kết quả mới; output sẵn có trong notebook không thay thế các tệp này.

Theo phạm vi nộp bài, file PDF tài liệu và ảnh JPG rời đi kèm thư mục ban đầu được để ngoài bản hiện tại trên GitHub. Báo cáo Word/PDF cũng được nộp riêng. Hình kết quả trích từ notebook và GIF demo vẫn được giữ đầy đủ.

## Chiến thuật triển khai

1. Nạp dữ liệu, phân biệt vị trí robot với điểm đặt điều khiển và giữ ranh giới từng ván.
2. Khớp khuôn hình học để suy ra tư thế khối T; kiểm tra độ khớp, nội suy các khung kém và kiểm chứng nhãn.
3. Học World Model dự đoán độ thay đổi tư thế, dùng đặc trưng tương đối và chia dữ liệu theo ván.
4. So sánh với mốc vật đứng yên, kiểm tra riêng khung có chuyển động và dự đoán nhiều bước.
5. Sinh chuỗi hành động bằng Diffusion, dùng World Model chọn ứng viên, thu dữ liệu robot tự chơi và đánh giá lại.

## Khi chạy lại

Notebook dùng Python và các thư viện `numpy`, `torch`, `matplotlib`, `gymnasium`, `gym-pusht`, `pandas`, `pyarrow`, `opencv-python`, `av`, `huggingface_hub`, `pillow` và môi trường Jupyter. Chọn đúng kernel có các thư viện trước khi chạy từ trên xuống.

Đường dẫn mặc định trong bản notebook hiện tại là `D:\AI\PushT`, có thể đổi biến `ROOT` hoặc đặt biến môi trường `PUSHT_ROOT`. Cờ `FORCE` quyết định một bước có chạy lại khi đã có tệp đầu ra hay không; đây không phải cơ chế tự tiếp tục huấn luyện từ giữa epoch. Cần kiểm tra đủ parquet, metadata và video trước khi bỏ qua tải dữ liệu. Nếu giảm số epoch Diffusion để thử nhanh, phải điều chỉnh cả bước chọn checkpoint đang yêu cầu tối thiểu epoch 175.

Bản notebook được giữ theo tệp hiện có, chưa sửa hoặc chạy lại chương trình trong lần chuẩn bị này. Chọn đúng thư mục và lưu riêng các kết quả mới khi tái lập.

## Dữ liệu và phương pháp liên quan

- Dataset: https://huggingface.co/datasets/lerobot/pusht
- Bộ điểm góc kiểm chứng: https://huggingface.co/datasets/lerobot/pusht_keypoints
- Diffusion Policy: https://diffusion-policy.cs.columbia.edu/
- Mã nguồn chính thức: https://github.com/real-stanford/diffusion_policy

Các nguồn bên ngoài giữ nguyên điều kiện sử dụng tương ứng. Nguồn tác giả của notebook được cung cấp cần được bổ sung khi được xác nhận.
