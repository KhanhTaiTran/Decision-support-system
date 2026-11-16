# DSS chọn phòng trọ cho sinh viên

Final project: hệ thống hỗ trợ quyết định đa tiêu chí bằng TOPSIS. Seminar bắt đầu **12/12/2026**. Mục tiêu: demo MVP **22/11**, chốt tính năng **29/11**, report và slide **07/12**.

## Chạy trên máy cá nhân

Cần Python 3.11 trở lên và Git. Chạy lần lượt trong PowerShell:

```powershell
git clone https://github.com/KhanhTaiTran/Decision-support-system.git
cd Decision-support-system
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m streamlit run app.py
```

macOS/Linux: thay `.\.venv\Scripts\python.exe` bằng `.venv/bin/python`.

Không cần kích hoạt virtualenv. Dừng ứng dụng bằng Ctrl+C.

Trên Windows nên dùng Python chính thức từ python.org. Nếu lệnh `python` trỏ tới MSYS2/Git Bash và tạo `.venv/bin` thay vì `.venv/Scripts`, dùng `py -3 -m venv .venv` từ Python chính thức để tránh phải tự biên dịch thư viện.

## Cấu trúc

```text
app.py                       # Giao diện Streamlit và tích hợp
src/housing_dss/
  criteria.py                # Tên tiêu chí, đơn vị và cost/benefit
  data.py                    # Đọc và kiểm tra CSV
  topsis.py                  # Hàm xếp hạng độc lập UI
data/
  rooms_sample.csv           # 8 phòng giả lập cho bản khởi tạo
  README.md                  # Schema và rubric chấm điểm
tests/                       # Test thuật toán và dữ liệu
docs/                        # Phương pháp, report, slide, demo
.github/workflows/tests.yml  # Chạy test khi push/PR
```

## Phân công module

- **Hồ Ngọc An**: `data/`, yêu cầu và nội dung report. Mở rộng 30–50 phòng và kiểm tra nguồn dữ liệu.
- **Châu Thành Phát**: `src/housing_dss/topsis.py`, phương pháp và phân tích độ nhạy.
- **Trần Khánh Tài**: `app.py`, đóng gói, giao diện, import/export CSV và tích hợp.
- **Trần Việt Trung**: `tests/`, kịch bản demo, test tích hợp và video dự phòng.

Thay đổi schema hoặc chữ ký hàm cần trao đổi trước với người tích hợp. Mỗi người viết phần report tương ứng công việc mình thực hiện.

[Kế hoạch Google Sheets và deadline](https://docs.google.com/spreadsheets/d/1wgrpr-N_P16rFBHk9lmXNfw0crfg0Z2PDYrWAIVx7LE/edit)

## Làm việc bằng branch và pull request

Mỗi đầu việc tạo branch riêng, ví dụ:

```powershell
git switch main
git pull --ff-only
git switch -c feat/topsis-sensitivity
# sửa file, chạy test rồi commit
git add src/housing_dss/topsis.py tests/test_topsis.py
git commit -m "Add sensitivity comparison"
git push -u origin feat/topsis-sensitivity
```

Mở pull request vào `main`, nhờ một bạn review và đợi CI xanh rồi merge. Không force push lên `main`. Chủ repo cần cấp quyền cộng tác cho 3 bạn còn lại trong GitHub Settings → Collaborators.

## Kiểm tra trước khi push

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m compileall -q app.py src tests
```

## Phạm vi bản khởi tạo

Đã có lọc ngân sách, điều chỉnh 5 trọng số, TOPSIS, top 3 và bảng bước tính. Dữ liệu là giả lập. Điểm xếp hạng phụ thuộc tập ứng viên, không phải xác suất phù hợp. Đồng hạng sắp theo ID; tập không có khác biệt nhận điểm 0,5. Không có phòng thì gợi ý tăng ngân sách.

Các phần team tiếp tục: mở rộng dữ liệu, ví dụ tính tay độc lập, import/export, so sánh 3 bộ trọng số, cải thiện giải thích, report và slide. Không thêm login, thanh toán, scraping hoặc API bản đồ trong phạm vi hiện tại.

## Tài liệu tham khảo

- [Streamlit: Create an app](https://docs.streamlit.io/get-started/tutorials/create-an-app)
- [Towards Explainable TOPSIS](https://arxiv.org/abs/2306.07706)
