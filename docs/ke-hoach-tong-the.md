
**TOPIC:** Student Housing Decision Support System  

---

## 1. Mục tiêu và Sản phẩm Bắt buộc (Deliverables)

Đến ngày 12/12, nhóm cần có đủ 4 sản phẩm:
1. **Ứng dụng Web DSS hoàn thiện 100% (Hoàn thành trước 06/12):** 
   * Lọc ngân sách cứng + 5 slider điều chỉnh trọng số.
   * Nút chọn nhanh kịch bản trọng số (Preset Weight Profiles: Cân bằng, Tiết kiệm, Gần trường, Tiện nghi/Rộng rãi).
   * Tải file CSV phòng tùy chỉnh & Nút tải về kết quả xếp hạng kèm điểm TOPSIS.
   * Thẻ tóm tắt Top 3 trực quan (Badge nổi bật: Rẻ nhất, Gần nhất, Điểm cao nhất).
   * Biểu đồ so sánh trực quan các tiêu chí của các phòng ứng viên.
   * Bảng chi tiết minh bạch công thức ($D^+, D^-, C_i$).
2. **Video Demo dự phòng (Hoàn thành trước 06/12):** Video 3–5 phút Full HD ghi lại trọn vẹn luồng demo (đề phòng sự cố mạng/máy chiếu).
3. **Báo cáo cuối kỳ (Report PDF) (07/12 – 09/12):** 25–35 trang tiếng Anh chuẩn ISM, dùng ảnh chụp app thật và số liệu thật.
4. **Bộ Slide thuyết trình & Kịch bản 20 phút (09/12 – 10/12):** 18–20 slides chia đều cho 4 thành viên (An 4p, Phát 6p, Tài 5p, Trung 5p).

---

## 2. Lộ trình Chi tiết 3 Tuần

```text
┌────────────────────────────────────────────────────────────┐  ┌─────────────────────────┐
│       2 TUẦN ĐẦU: CODE HOÀN CHỈNH 100% (23/11 – 06/12)     │  │ 1 TUẦN CUỐI: NƯỚC RÚT   │
│                                                            │  │ (07/12 – 12/12)         │
│  [Tuần 1: 23/11 - 29/11]      [Tuần 2: 30/11 - 06/12]      │  │ [Tuần 3: 07/12 - 12/12] │
│  • Nâng cấp Core Features     • Biểu đồ phân tích trực quan│  │ • Viết Report (07-08/12)│
│  • Preset Profiles (1-click)  • Test phủ kín mọi case biên │  │ • Chốt PDF & Slide (09) │
│  • Import/Export CSV          • Quay video demo 1080p      │  │ • Tập dượt 20p (10/12)  │
│  • Giao diện Top 3 thẻ đẹp    • CHỐT CODE 100% (06/12)     │  │ • SEMINAR DAY (12/12)   │
└────────────────────────────────────────────────────────────┘  └─────────────────────────┘
```

### Tuần 1 (23/11 – 29/11): Phát triển Tính năng Cốt lõi & Trọng số Mẫu
* **23/11 – 25/11:**
  * **Trần Khánh Tài (Code UI & App):**
    * Thêm 4 nút chọn nhanh Preset Profiles vào sidebar (`preferences.py`):
      1. *🎯 Balanced (Cân bằng):* 20% đều cả 5 tiêu chí.
      2. *💰 Budget-First (Tiết kiệm):* Chi phí 40%, Khoảng cách 20%, Diện tích 15%, An ninh 15%, Tiện nghi 10%.
      3. *🏫 Campus-Proximity (Gần trường):* Khoảng cách 45%, Chi phí 25%, An ninh 10%, Diện tích 10%, Tiện nghi 10%.
      4. *🛋️ Comfort & Space (Tiện nghi & Rộng rãi):* Diện tích 35%, Tiện nghi 25%, An ninh 20%, Chi phí 10%, Khoảng cách 10%.
    * Thêm ô Upload file CSV tùy chọn và nút Download CSV kết quả đã xếp hạng vào `app.py`.
    * Cải tiến phần hiển thị Top 3 trong `results.py`: hiển thị thẻ tóm tắt phòng nổi bật kèm badge ưu điểm (Best Price, Closest, Top Pick).
  * **Châu Thành Phát (Toán & Thuật toán):**
    * Chọn 3 phòng từ dataset, tính tay từng bước các ma trận ($X, R, V, A^+, A^-, D^+, D^-, C$) để làm chuẩn đối chứng.
* **26/11 – 27/11:**
  * **Trần Việt Trung (Kiểm thử):**
    * Viết test cho tính năng Preset Profiles và viết test kiểm chứng ví dụ 3 phòng của Phát trong `tests/test_topsis.py`.
  * **Hồ Ngọc An (Dữ liệu):**
    * Rà soát chuẩn hóa 30 phòng trong `data/rooms_sample.csv`, kiểm tra rubric an ninh/tiện nghi.
* **28/11 – 29/11:**
  * Cả nhóm chạy thử app, kiểm tra luồng demo kéo slider và chuyển đổi nhanh giữa các Profile trọng số.

### Tuần 2 (30/11 – 06/12): Trực quan hóa, Gia cố Hệ thống
* **30/11 – 02/12:**
  * **Tài:** Bổ sung biểu đồ trực quan (ví dụ: bar chart so sánh các tiêu chí chuẩn hóa của Top 3 phòng hoặc so sánh thứ hạng khi đổi profile) để giao diện nhìn sinh động, chuyên nghiệp.
  * **Phát:** Rà soát lại công thức toán và xuất sẵn các bảng số liệu so sánh độ nhạy (Sensitivity Analysis data) giữa các profile.
* **03/12 – 04/12:**
  * **Trung & Tài:**
    * Kiểm thử áp lực các trường hợp biên: danh sách 0 phòng, ngân sách cực thấp, tải file CSV sai định dạng/thiếu cột, toàn bộ trọng số bằng 0.
    * Đảm bảo app hiện thông báo lỗi bằng tiếng Anh thân thiện, không bao giờ bị văng/crash màn hình đỏ.
* **05/12 – 06/12:**
  * **Trung & Tài:** Quay video màn hình demo 3–5 phút chất lượng Full HD 1080p có thuyết minh tiếng Anh, lưu sẵn file `.mp4` vào máy và USB.
  * **06/12: CHỐT CODE HOÀN CHỈNH 100% (Final Code Freeze).** Merge nhánh chính, không chỉnh sửa code nữa. Chụp toàn bộ ảnh màn hình app sắc nét để chuẩn bị viết report.

### Tuần 3 (07/12 – 12/12): Viết Report, Làm Slide & Thuyết trình
* **07/12 (T2):** Viết bản thảo Báo cáo (Report Draft): Lấy ảnh chụp app thật và số liệu phân tích thật đưa vào 7 chương (An: Ch.1,2,3; Phát: Ch.4; Tài: Ch.5; Trung: Ch.6,7).
* **08/12 (T3):** Ghép và hoàn thiện Báo cáo: An & Tài chủ trì, cả nhóm cùng rà soát chéo số liệu và chính tả.
* **09/12 (T4):** Chốt file **Report PDF chính thức** + Thiết kế Slide 18–20 trang (chia đều: An 4p, Phát 6p, Tài 5p, Trung 5p).
* **10/12 (T5):** Tập Thuyết trình lần 1 & 2 (bấm giờ đúng 20p, chạy app offline trên laptop, chuẩn bị Q&A và 2 câu hỏi phản biện nhóm khác).
* **11/12 (T6):** Nộp bài lên cổng trường, sao lưu file vào 2 USB dự phòng. Nghỉ ngơi giữ sức khỏe.
* **12/12 (T7):** **SEMINAR DAY — BẢO VỆ ĐỒ ÁN!**

---

## 3. Hướng dẫn Chi tiết Task của Phát, An và Trung

### 3.1. Châu Thành Phát - Tính tay ví dụ 3 phòng đối chứng
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

### 3.2. Hồ Ngọc An - Chuẩn hóa Dữ liệu & Rubric Chấm điểm
* **Mục đích:** Khi giảng viên hỏi: *"Dữ liệu 30 phòng này ở đâu ra? Điểm Security và Amenities dựa vào cơ sở nào mà chấm?"*, An giải thích được quy tắc tính điểm khoa học, minh bạch.
* **Các bước thực hiện cụ thể:**
  1. **Quy tắc tính điểm An ninh (1–5):** Điểm = $1 +$ số điều kiện thỏa mãn trong 4 tiêu chí: (1) Khóa cửa riêng, (2) Kiểm soát ra vào/bảo vệ, (3) Camera an ninh, (4) Đèn chiếu sáng lối đi.
  2. **Quy tắc tính điểm Tiện nghi (1–5):** Điểm = $1 +$ số điều kiện thỏa mãn trong 4 tiêu chí: (1) WC riêng, (2) Khu nấu ăn, (3) Có Wi-Fi, (4) Chỗ để xe máy an toàn.
  3. **Kiểm tra file `data/rooms_sample.csv`:**
     * Không trùng ID (`R01` đến `R30`).
     * Cột `source` ghi rõ `synthetic` (dữ liệu giả lập thực tế, bảo đảm tính liêm chính học thuật).
     * Mức giá, diện tích và khoảng cách sát với thực tế quanh trường ĐH Quốc Tế (VNU-HCM).
* **Đầu ra:** File `data/README.md` cập nhật đầy đủ bảng từ điển dữ liệu (Data Dictionary) $\rightarrow$ Đưa vào **Chapter 3 của Report** và **Slide mở đầu**.

### 3.3. Trần Việt Trung - Kiểm thử Tự động & Phân tích Độ nhạy
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

---

## 4. Quy ước Chung về Code & Phối hợp (Team Rules)

Để cả nhóm code mượt mà, không giẫm chân lên nhau và không bị xung đột code:

### 4.1. Quy chuẩn Đặt tên (Naming Conventions - Chuẩn PEP 8)
* **Ngôn ngữ 100% Tiếng Anh:** Toàn bộ tên biến, tên hàm, tên cột dữ liệu, comments, docstrings, commit messages đều viết bằng tiếng Anh.
* **Tên biến & hàm (Functions & Variables):** Dùng `snake_case`.  
  * *Hợp lệ:* `rank_rooms`, `load_rooms`, `monthly_cost_vnd`, `d_plus`, `d_minus`, `topsis_score`.  
  * *Không dùng:* `RankRooms`, `rankRooms`, `monthlyCost`.
* **Tên hằng số (Constants):** Dùng `UPPER_SNAKE_CASE`.  
  * *Hợp lệ:* `CRITERIA`, `REQUIRED_FIELDS`, `PRESET_PROFILES`.
* **Tên Class (Classes):** Dùng `PascalCase`.  
  * *Hợp lệ:* `TopsisTests`, `DataTests`, `ResultFormattingTests`.

### 4.2. Hợp đồng Bất biến về Dữ liệu (Data Schema Contract)
* **Tuyệt đối KHÔNG tự ý đổi tên 5 cột tiêu chí cốt lõi:**
  1. `monthly_cost_vnd`
  2. `distance_km`
  3. `area_m2`
  4. `security_score`
  5. `amenities_score`
* Bất kỳ ai muốn đổi tên cột hoặc sửa signature hàm `rank_rooms(rooms, weights)` phải báo trước.

### 4.3. Quy trình Git & Tránh Xung đột (Git Workflow)
* **Mỗi task 1 branch riêng biệt:**
  * Nhánh tính năng: `feat/<tên-tính-năng>` (vd: `feat/preset-profiles`, `feat/csv-export`).
  * Nhánh test: `test/<tên-test>` (vd: `test/worked-example`).
  * Nhánh docs: `docs/<tên-doc>` (vd: `docs/report-outline`).
* **Tuyệt đối KHÔNG commit/push thẳng vào `main`**, KHÔNG force push (`git push -f`).
* **Quy tắc Kiểm tra trước khi mở Pull Request:**  
  Trước khi tạo PR, thành viên phải chạy 2 lệnh sau trên terminal của mình:
  ```powershell
  .\.venv\Scripts\python.exe -m unittest discover -s tests -v
  .\.venv\Scripts\python.exe -m compileall -q app.py src tests
  ```
  Chỉ khi 2 lệnh trên chạy thành công không có lỗi đỏ thì mới được mở PR vào `main`.
