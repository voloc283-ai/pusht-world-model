# PushT World Model

Notebook tham khảo cho project học quy luật tương tác giữa robot và vật thể trong bài toán PushT.

## Nguồn và hiện trạng

Notebook này được người nộp nhận từ người khác và đang được dùng để tìm hiểu phương pháp. Các output, hình và GIF được lưu sẵn trong notebook thuộc lần chạy được cung cấp cùng tài liệu; **không phải kết quả của một lần chạy lại đầy đủ do người nộp thực hiện**.

Người nộp chưa chạy lại toàn bộ quy trình huấn luyện, chọn checkpoint, thu dữ liệu tự chơi và đánh giá. Repository chỉ giữ notebook hiện có cùng hướng dẫn này. Không bổ sung trọng số, video hay số liệu thực nghiệm mới cho các bước chưa hoàn thành. Báo cáo được nộp riêng và không nằm trong repository.

Các chỉnh sửa vận hành đã áp dụng gồm đường dẫn lưu dữ liệu theo thư mục dự án, đúng tên file biểu đồ khi nạp checkpoint, kiểm tra đủ dữ liệu/video khi tải và xử lý sai số làm tròn của thanh sai số biểu đồ.

## Nội dung notebook

1. Tải dữ liệu `lerobot/pusht` và kiểm tra trạng thái, hành động, ảnh.
2. Mô phỏng PushT và ước lượng tư thế khối T từ ảnh.
3. Xây dựng World Model dự đoán độ thay đổi tư thế vật thể.
4. Phần mở rộng Diffusion Policy và kết hợp chọn hành động bằng World Model.
5. Thiết kế đánh giá, thu dữ liệu tự chơi và clip minh họa.

Sự hiện diện của mã và output có sẵn không được hiểu là mọi bước đã được người nộp chạy lại.

## Xem nội dung

Mở [PushT_WorldModel.ipynb](PushT_WorldModel.ipynb) để xem mã và các output lưu trong file. Khi xem offline bằng VS Code hoặc JupyterLab, có thể đọc notebook mà không khởi chạy huấn luyện. Một số trình xem notebook trên web có thể xử lý ảnh động khác nhau; việc kiểm tra thực thi cần môi trường Python và dữ liệu riêng.

## Chạy lại trên Windows

Môi trường đã kiểm tra: Python 3.11.9, PyTorch 2.7.1 với CUDA 11.8. Chọn bản PyTorch phù hợp với phần cứng trước khi huấn luyện.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install jupyterlab ipykernel numpy gymnasium gym-pusht pandas pyarrow opencv-python av huggingface_hub matplotlib pillow
.\.venv\Scripts\python.exe -m pip install torch==2.7.1 --index-url https://download.pytorch.org/whl/cu118
.\.venv\Scripts\python.exe -X utf8 -m jupyter lab "PushT_WorldModel.ipynb"
```

Trong VS Code, phải chọn kernel `.venv/Scripts/python.exe`; kích hoạt `.venv` ở Terminal không tự đổi kernel của notebook. Chạy từ trên xuống. Thư mục `PushT` sẽ chứa dữ liệu và kết quả của lần chạy mới. Mặc định, các bước nặng dùng lại file đã có khi cờ `FORCE` tương ứng là `False`.

Huấn luyện Diffusion là bước tốn thời gian. Khi mới tìm hiểu, có thể chạy từng ô trước. Không giảm `DP_EPOCHS` xuống dưới 175 mà giữ nguyên bước chọn checkpoint, vì mã chọn hiện xét checkpoint từ epoch 175.

## Video trên GitHub

GitHub có thể lưu và hiển thị ảnh GIF, đồng thời hỗ trợ đính kèm video MP4, MOV và WebM. Tài liệu GitHub khuyến nghị H.264 để tăng khả năng tương thích với trình duyệt. Đây là xem lại video đã ghi, không có nghĩa GitHub tự chạy huấn luyện mô hình hay cấp GPU khi mở repository.

Theo yêu cầu hiện tại, không đưa thêm video kết quả chưa được người nộp tự chạy vào repository. Các hình và GIF sẵn có vẫn nằm trong notebook tham khảo và cần được đọc cùng phần ghi chú nguồn ở trên.

## Tài liệu

- Dataset: https://huggingface.co/datasets/lerobot/pusht
- Diffusion Policy: https://diffusion-policy.cs.columbia.edu/
- Mã nguồn chính thức: https://github.com/real-stanford/diffusion_policy
- Bài báo: https://arxiv.org/abs/2303.04137
- Tutorial do giảng viên gợi ý: https://learnrobotics.ai/learn/day-17
- Hướng dẫn video của GitHub: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files

Nguồn tác giả và quyền sử dụng của notebook nhận từ người khác cần được người nộp xác nhận. Các nguồn bên ngoài giữ nguyên điều kiện sử dụng và bản quyền của tác giả tương ứng.
