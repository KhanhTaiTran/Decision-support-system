
**TOPIC:** Student Housing Decision Support System  

---

## 1. Phân chia Task theo Mức độ Ưu tiên (Priority Tiers)

```text
┌────────────────────────────────────────────────────────────────────────┐
│ Phase 1: CORE ESSENTIALS                                               │
│ • Preset Profiles 1-click • Import/Export CSV • UI Top 3 thẻ nổi bật   │
│ • Ví dụ tính tay 3 phòng  • Rubric dữ liệu    • Test tự động 100%      │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │ (Xong sớm chuyển ngay sang)
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Phase 2: ADVANCED EXTENSIONS                                           │
│ • Web Scraping: Cào tin trọ thực tế quanh khu vực trường ĐHQG          │
│ • Interactive Maps: Bản đồ trực quan (aps/Folium) định vMị các phòng   │
│ • Visual Analytics: Biểu đồ so sánh đa chiều (Radar/Bar Chart)         │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Phase 3: FINAL DELIVERY                                                │
│ • Báo cáo Final Report PDF (25–35 trang, 7 chương, lấy ảnh & data thật)│
│ • Slide Thuyết trình (18–20 trang, căn đúng 20 phút cho 4 người)       │
│ • Quay video demo 3–5 phút & Q&A                                       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Chi tiết Phân công Thành viên theo Giai đoạn

### Giai đoạn 1: Core Essentials

* **Trần Khánh Tài (Application & Integration):**
  * Thêm 4 nút **Preset Weight Profiles** vào sidebar (Balanced, Budget-First, Campus-Proximity, Comfort & Space).
  * Thêm ô **Upload CSV tùy chỉnh** và nút **Download CSV kết quả xếp hạng**.
  * Thiết kế lại **Top 3 phòng dạng thẻ (Cards)** với badge ưu điểm (Rẻ nhất, Gần nhất, Lựa chọn tối ưu).
* **Châu Thành Phát (Toán & Thuật toán):**
  * Lấy 3 phòng từ dataset, tính tay từng bước các ma trận ($X, R, V, A^+, A^-, D^+, D^-, C$) làm chuẩn đối chứng khoa học cho thuật toán.
* **Hồ Ngọc An (Dữ liệu & Yêu cầu):**
  * Chuẩn hóa 30 phòng trong `rooms_sample.csv`, kiểm tra rubric điểm an ninh và tiện nghi (1–5) theo công thức khách quan.
* **Trần Việt Trung (Kiểm thử & QA):**
  * Viết test kiểm chứng kết quả tính tay của Phát trong `tests/test_topsis.py` (`assertAlmostEqual`).
  * Viết test cho tính năng Preset Profiles và test các trường hợp biên (0 phòng, ngân sách thấp, file sai).

---

### Giai đoạn 2: Advanced Extensions (khi Xong Core)

1. **Web Scraping (Cào tin phòng trọ thực tế):**
   * Viết script cào tự động các tin đăng cho thuê phòng trọ thật quanh khu vực ĐHQG-HCM / TP. Thủ Đức / Dĩ An (từ các nguồn công khai như Phongtro123, Chotot, Batdongsan...).
   * Trích xuất các trường: Giá thuê, Khoảng cách ước tính, Diện tích, Tiện ích $\rightarrow$ Đổ vào file CSV thật để hệ thống DSS xếp hạng phòng trọ thị trường.
2. **Interactive Map (Bản đồ Trực quan):**
   * Tích hợp bản đồ tương tác (Google Maps / Folium / OpenStreetMap) trực tiếp trên Streamlit.
   * Hiển thị tọa độ khuôn viên trường (Campus) và cắm ghim (Pins) các phòng trọ xung quanh; click vào ghim sẽ hiện thông tin phòng, giá và điểm xếp hạng TOPSIS.
3. **Visual Analytics (Biểu đồ Đa chiều):**
   * Thêm biểu đồ Radar / Bar Chart so sánh trực quan tương quan giữa các tiêu chí của các phòng trong Top 3.

---

### Giai đoạn 3: Final Delivery (Báo cáo & Thuyết trình)

* **Report:**
  7 chương:
    * *An:* Ch.1 (Problem Statement & Scope), Ch.2 (Model-driven DSS Theoretical Background), Ch.3 (Requirements & Rubric).
    * *Phát:* Ch.4 (TOPSIS Mathematical Modeling & Ví dụ tính tay 3 phòng).
    * *Tài:* Ch.5 (System Architecture, DFD, UI Implementation, Web Scraping/Maps nếu có).
    * *Trung:* Ch.6 (Testing & Sensitivity Analysis), Ch.7 (Limitations & Future Work), Ch.8 Conclusion.
* **Slide Thuyết trình & Demo:**
  * Soạn 18–20 slides chia đều thời lượng
  * Quay video màn hình demo 3–5 phút
  * Tập dượt thuyết trình và chuẩn bị câu hỏi phản biện.
* **Ngày 12/12/2026: SEMINAR DAY.**

---

## 3. Hướng dẫn Chi tiết Từng Bước cho Task của Từng Thành viên

### 3.1. Châu Thành Phát — Tính tay ví dụ 3 phòng đối chứng
* **Mục đích:** Khi giảng viên hỏi: *"Làm sao chứng minh code tính đúng thuật toán TOPSIS?"*, Phát sẽ chiếu bảng tính tay chứng minh kết quả tính bằng tay khớp 100% với số hiển thị trên app.
* **Các bước thực hiện cụ thể:**
  1. Chọn 3 phòng từ `rooms_sample.csv` (ví dụ: `R01`, `R02`, `R03`) với đầy đủ 5 tiêu chí.
  2. Chọn một bộ trọng số cố định (ví dụ: $w = [0.35, 0.25, 0.15, 0.15, 0.10]$).
  3. Lập **Ma trận quyết định $X$** ($3 \times 5$).
  4. Tính **Ma trận chuẩn hóa vector $R$**: $r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{k=1}^3 x_{kj}^2}}$.
  5. Tính **Ma trận có trọng số $V$**: $v_{ij} = r_{ij} \times w_j$.
  6. Xác định **Phương án lý tưởng $A^+$ và $A^-$**:
     * Tiêu chí Cost (chi phí, khoảng cách): $A^+$ lấy giá trị min, $A^-$ lấy max.
     * Tiêu chí Benefit (diện tích, an ninh, tiện nghi): $A^+$ lấy giá trị max, $A^-$ lấy min.
  7. Tính **Khoảng cách Euclidean $D^+$ và $D^-$**:
     * $D^+_i = \sqrt{\sum (v_{ij} - v^+_j)^2}$; $D^-_i = \sqrt{\sum (v_{ij} - v^-_j)^2}$.
  8. Tính **Điểm tương đồng tương đối $C_i$**: $C_i = \frac{D^-_i}{D^+_i + D^-_i}$.
* **Đầu ra:** 1 bảng tính Markdown/Excel có đầy đủ các bước trên $\rightarrow$ Đưa vào **Chapter 4 của Report** và **Slide thuyết trình**.

### 3.2. Hồ Ngọc An — Chuẩn hóa Dữ liệu & Rubric Chấm điểm
* **Mục đích:** Khi giảng viên hỏi: *"Dữ liệu 30 phòng này ở đâu ra? Điểm Security và Amenities dựa vào cơ sở nào mà chấm?"*, giải thích được quy tắc tính điểm khoa học, minh bạch.
* **Các bước thực hiện cụ thể:**
  1. **Quy tắc tính điểm An ninh (1–5):** Điểm = $1 +$ số điều kiện thỏa mãn trong 4 tiêu chí: (1) Khóa cửa riêng, (2) Kiểm soát ra vào/bảo vệ, (3) Camera an ninh, (4) Đèn chiếu sáng lối đi.
  2. **Quy tắc tính điểm Tiện nghi (1–5):** Điểm = $1 +$ số điều kiện thỏa mãn trong 4 tiêu chí: (1) WC riêng, (2) Khu nấu ăn, (3) Có Wi-Fi, (4) Chỗ để xe máy an toàn.
  3. **Kiểm tra file `data/rooms_sample.csv`:**
     * Không trùng ID (`R01` đến `R30`).
     * Cột `source` ghi rõ `synthetic` (dữ liệu giả lập thực tế, bảo đảm tính liêm chính học thuật).
     * Mức giá, diện tích và khoảng cách sát với thực tế quanh trường ĐH Quốc Tế (VNU-HCM).
* **Đầu ra:** File `data/README.md` cập nhật đầy đủ bảng từ điển dữ liệu (Data Dictionary) $\rightarrow$ Đưa vào **Chapter 3 của Report** và **Slide mở đầu**.

### 3.3. Trần Việt Trung — Kiểm thử Tự động & Phân tích Độ nhạy
* **Mục đích:** Chứng minh chất lượng phần mềm, đảm bảo app không bao giờ crash khi demo và chứng minh thứ hạng thay đổi hợp lý khi đổi ưu tiên (Sensitivity Analysis).
* **Các bước thực hiện cụ thể:**
  1. **Test kiểm chứng toán:** Vào `tests/test_topsis.py`, viết test truyền đúng 3 phòng và trọng số của Phát, kiểm tra xem `rank_rooms()` có trả về đúng điểm $C$ của Phát hay không (`assertAlmostEqual`).
  2. **Test Preset Profiles & Độ nhạy:**
     * Viết test kiểm tra: khi chọn "Budget-First" thì phòng rẻ nhất phải lên top.
     * Khi chọn "Campus-Proximity" thì phòng gần trường nhất phải lên top.
  3. **Test trường hợp biên (Edge Cases):**
     * Budget = 0 hoặc quá thấp (kết quả rỗng, không crash).
     * Toàn bộ 5 weights = 0 (báo lỗi hợp lệ).
     * File CSV thiếu cột hoặc sai định dạng (thông báo lỗi thân thiện).
* **Đầu ra:** Các hàm test tự động trong `tests/`, chạy `unittest` ra PASS 100% $\rightarrow$ Chụp log test đưa vào **Chapter 6 của Report** và **Slide**.

### 3.4. Trần Khánh Tài — Kiến trúc App, Giao diện & Tính năng Nâng cao
* **Mục đích:** Tạo ra một web app hoàn chỉnh, trực quan, chuyên nghiệp để người xem hiểu kết quả ngay trong 1 phút.
* **Các bước thực hiện cụ thể:**
  1. **Preset Profiles:** Tạo 4 nút chọn nhanh bộ trọng số trên sidebar để demo phân tích độ nhạy mượt mà.
  2. **Import / Export CSV:** Xử lý upload file CSV mới và download kết quả đã xếp hạng kèm điểm TOPSIS.
  3. **Giao diện Top 3:** Hiển thị thẻ tóm tắt phòng nổi bật với badge và thông tin trực quan.
  4. **Tính năng nâng cao (Giai đoạn 2):** Cào dữ liệu web thật và tích hợp bản đồ cắm ghim tọa độ các phòng quanh trường.
* **Đầu ra:** Ứng dụng Streamlit hoàn chỉnh $\rightarrow$ Chụp ảnh màn hình đưa vào **Chapter 5 của Report** và **Slide**.

---

## 4. Quy ước Lập trình & Phối hợp Nhóm (Team Rules)

* **Ngôn ngữ 100% Tiếng Anh:** Toàn bộ tên biến, tên hàm, commit message, comments, docstrings.
* **Quy chuẩn đặt tên (PEP 8):**
  * Biến & Hàm: `snake_case` (vd: `rank_rooms`, `monthly_cost_vnd`, `d_plus`, `topsis_score`).
  * Hằng số: `UPPER_SNAKE_CASE` (vd: `CRITERIA`, `REQUIRED_FIELDS`, `PRESET_PROFILES`).
  * Class: `PascalCase` (vd: `TopsisTests`, `DataTests`).
* **Hợp đồng Dữ liệu (Schema Contract):** Tuyệt đối không tự ý đổi tên 5 cột cốt lõi: `monthly_cost_vnd`, `distance_km`, `area_m2`, `security_score`, `amenities_score`.
* **Quy trình Git & Pre-PR:**
  * Làm việc trên nhánh riêng: `feat/<name>`, `test/<name>`, `docs/<name>`. Không push thẳng vào `main`.
  * Trước khi mở PR, chạy bắt buộc trên terminal:
    ```powershell
    .\.venv\Scripts\python.exe -m unittest discover -s tests -v
    .\.venv\Scripts\python.exe -m compileall -q app.py src tests
    ```
