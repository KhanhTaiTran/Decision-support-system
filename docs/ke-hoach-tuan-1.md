# Kế hoạch tuần 1: 23–29/11/2026

## 1. Mục tiêu thật sự của tuần này

Cuối tuần, nhóm cần có một bản **chạy được từ đầu đến cuối**, không cần đẹp và chưa cần nhiều chức năng:

```text
Dữ liệu phòng trọ giả lập gồm 30 phòng có sẵn trong repo
        ↓
Kiểm tra dữ liệu có hợp lệ hay không
        ↓
Người dùng nhập ngân sách và chỉnh mức ưu tiên
        ↓
TOPSIS tính điểm và xếp hạng
        ↓
Hiển thị 3 phòng phù hợp nhất và lý do xếp hạng
        ↓
Test + demo local 5 phút
```

Tuần này **không làm**: đăng nhập, tài khoản người dùng, thanh toán, chatbot, bản đồ Google, scraping dữ liệu, machine learning, deploy public hay giao diện quá đẹp. Những phần đó chỉ xem xét sau khi bản cơ bản chạy đúng.

## 2. Những gì nhóm đang tạm chốt để bắt đầu

Nhóm vẫn có thể đổi sau khi trao đổi, nhưng nên dùng các lựa chọn này để bắt đầu ngay, tránh chờ đợi:

| Nội dung | Lựa chọn tạm thời | Nghĩa là gì |
| --- | --- | --- |
| Đề tài | Student Housing Decision Support System | Hệ thống hỗ trợ sinh viên chọn phòng trọ |
| Kỹ thuật gợi ý | TOPSIS | Không train AI; hệ thống chấm điểm và xếp hạng nhiều phòng theo nhiều tiêu chí |
| Dạng DSS | Model-driven DSS | Dùng mô hình toán học để hỗ trợ quyết định |
| Nền tảng | Web app chạy local | Mở bằng trình duyệt trên máy tính khi demo |
| Ngôn ngữ | Python | Cả thuật toán và giao diện đều dùng Python |
| Framework giao diện | Streamlit | Tạo web app nhanh, không cần làm React hay backend API riêng |
| Dữ liệu tuần 1 | 30 phòng giả lập | Phải ghi `synthetic`; không được nói là dữ liệu thật |
| Ngôn ngữ sản phẩm | English | Code, app, report, slide, mô tả dữ liệu đều dùng tiếng Anh |

### Năm tiêu chí đầu vào

| Tên cột trong dữ liệu | Ý nghĩa | Loại tiêu chí | Quy tắc |
| --- | --- | --- | --- |
| `monthly_cost_vnd` | Tổng chi phí mỗi tháng, gồm tiền thuê và phí cố định ước tính | Cost | Càng thấp càng tốt; đồng thời không được vượt ngân sách |
| `distance_km` | Khoảng cách từ phòng tới một campus đã chọn | Cost | Càng gần càng tốt |
| `area_m2` | Diện tích sử dụng | Benefit | Càng lớn càng tốt |
| `security_score` | Điểm an ninh từ 1 đến 5 | Benefit | Càng cao càng tốt |
| `amenities_score` | Điểm tiện nghi từ 1 đến 5 | Benefit | Càng cao càng tốt |

## 3. Cách làm việc chung

1. Mỗi người tạo **một branch riêng**, làm phần mình và mở pull request vào `main`.
2. Mỗi task chỉ có **một người chịu trách nhiệm chính**. Khi bị phụ thuộc vào phần của người khác thì tự nhắn trao đổi trực tiếp.
3. Trước khi push, chạy test. Nếu test lỗi thì chưa mở pull request.
4. Không tự đổi tên cột CSV, tên hàm `rank_rooms`, hoặc ý nghĩa năm tiêu chí mà không báo trong pull request.
5. Khi hoàn thành một việc, phải có bằng chứng: file đã tạo, test pass, ảnh chụp hoặc mô tả kết quả. Không chỉ nhắn “done”.

### Tài sản dùng chung đã chuẩn bị sẵn

`data/rooms_sample.csv` đã có 30 phòng giả lập và được kiểm tra bằng test tự động. Đây là dữ liệu chung để cả nhóm dùng khi làm thuật toán, giao diện và test; **không phải đầu việc được phân công cho một thành viên trong tuần này**.

### Lệnh cơ bản mỗi người cần biết

```powershell
git pull --ff-only
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Nếu đã có `.venv` thì không cần tạo lại. Khi Streamlit chạy, mở URL local được terminal hiển thị, thường là `http://localhost:8501`.

## 4. Plan chi tiết của Hồ Ngọc An — Requirement và nội dung report

**Mục tiêu cá nhân:** xác định rõ bài toán, phạm vi và yêu cầu hệ thống; chuẩn bị phần nội dung có thể dùng lại cho report cuối kỳ. Bộ CSV dùng chung đã có sẵn, nên không cần tạo hoặc kiểm tra dữ liệu như một đầu việc riêng.

| Ngày | Làm gì | Làm như thế nào | File cần tạo hoặc sửa | Khi nào được xem là xong |
| --- | --- | --- | --- | --- |
| 23/11 | Chốt mô tả bài toán | Viết ngắn: người dùng là ai, họ gặp khó khăn gì, app giải quyết thế nào, 5 tiêu chí là gì | Tạo `docs/requirements-week-1.md` | Có 1 trang ngắn bằng English; không viết lan man về login, map hay AI |
| 24/11 | Viết user stories | Viết ít nhất 2 user stories: sinh viên nhập budget; sinh viên thay đổi weights và xem top 3 | Sửa `docs/requirements-week-1.md` | Mỗi story có actor, hành động và kết quả mong đợi |
| 25/11 | Chốt yêu cầu chức năng | Liệt kê các chức năng bắt buộc: lọc theo budget, chỉnh 5 weights, xếp hạng TOPSIS, hiển thị top 3 và calculation details | Sửa `docs/requirements-week-1.md` | Yêu cầu khớp với flow app hiện tại, không có tính năng ngoài scope |
| 26/11 | Chốt yêu cầu phi chức năng | Ghi rõ app chạy local, phản hồi nhanh với dataset hiện tại, giao diện và tài liệu sản phẩm bằng English, không lưu personal data | Sửa `docs/requirements-week-1.md` | Có ít nhất 4 yêu cầu kiểm tra được |
| 27/11 | Viết phần report thô | Viết `Problem`, `Target User`, `System Scope`, `Criteria` và `Assumptions` | Tạo `docs/report-draft-week-1.md` | Có nội dung English để dùng lại cho report cuối; không tự nhận dữ liệu giả lập là dữ liệu thị trường thật |
| 28/11 | Rà lại tính nhất quán | Mở app, đối chiếu requirement với labels/input/result trên màn hình. Ghi phần nào chưa khớp để báo qua issue hoặc PR | Sửa `docs/requirements-week-1.md` nếu cần | Không còn yêu cầu nào mâu thuẫn với app hoặc 5 tiêu chí cố định |
| 29/11 | Đưa tài liệu lên GitHub | Tạo branch `docs/week-1-requirements`, commit tài liệu requirement/report, mở pull request | `docs/requirements-week-1.md`, `docs/report-draft-week-1.md` | Pull request chỉ có nội dung tài liệu, không lẫn code hoặc CSV |

## 5. Plan chi tiết của Châu Thành Phát — TOPSIS và logic xếp hạng

**Mục tiêu cá nhân:** chứng minh TOPSIS tính đúng, giải thích được thuật toán khi bị hỏi và biến kết quả tính tay thành test tự động.

| Ngày | Làm gì | Làm như thế nào | File cần tạo hoặc sửa | Khi nào được xem là xong |
| --- | --- | --- | --- | --- |
| 23/11 | Làm ví dụ TOPSIS bằng tay | Chọn đúng 3 phòng từ CSV và dùng đủ 5 tiêu chí. Chọn một bộ trọng số, ví dụ cost 35, distance 25, area 15, security 15, amenities 10 | Tạo `docs/topsis-worked-example.md` | Có bảng decision matrix ban đầu và bộ trọng số |
| 24/11 | Tính đầy đủ TOPSIS | Tính chuẩn hóa vector `r`, nhân trọng số thành `v`, tìm positive/negative ideal, rồi tính `D+`, `D-`, `C = D- / (D+ + D-)` | Tiếp tục `docs/topsis-worked-example.md` | Có thể giải thích vì sao cost dùng min cho positive ideal còn benefit dùng max |
| 25/11 | So kết quả tính tay với code | Gọi hàm `rank_rooms` trên đúng 3 phòng và cùng trọng số. So ID xếp hạng và score sau khi làm tròn | Sửa `tests/test_topsis.py` nếu cần | Thứ hạng trùng với ví dụ tính tay; sai khác score nằm trong mức làm tròn đã ghi |
| 26/11 | Viết phần phương pháp | Viết mục Methodology: input, normalization, weights, ideal solutions, distances, score và interpretation | Sửa `docs/topsis-worked-example.md` | Có thể copy trực tiếp vào report và slide methodology |
| 27/11 | Tạo 3 profile trọng số | Tạo `budget-focused`, `campus-focused`, `space-amenities-focused`. Mỗi profile phải giải thích ưu tiên nào cao nhất | Tạo `docs/weight-profiles.md` | Có bảng 3 profile, tổng weight mỗi profile lớn hơn 0 |
| 28/11 | Kiểm tra tình huống biên | Test: danh sách rỗng, 1 phòng, 2 phòng giống hệt, một cột toàn 0, toàn bộ trọng số bằng 0 | Sửa `tests/test_topsis.py` khi thiếu test | Mỗi tình huống có expected result và test pass |
| 29/11 | Đưa phần TOPSIS lên GitHub | Tạo branch `feat/topsis-validation`, commit code/test/tài liệu phương pháp, mở pull request | `src/housing_dss/topsis.py`, `tests/test_topsis.py`, `docs/` | Pull request không đụng tới CSV hoặc giao diện nếu không thật sự cần |

**Công thức cần hiểu để demo:**

```text
r(i,j) = x(i,j) / sqrt(sum(x(i,j)^2))
v(i,j) = r(i,j) × normalized_weight(j)
C(i)   = D-(i) / (D+(i) + D-(i))
```

`C` càng gần 1 thì phương án càng tốt trong tập phòng hiện tại. `C` không phải xác suất “phòng này phù hợp 100%”.

## 6. Plan chi tiết của Trần Khánh Tài — Web app và tích hợp

**Mục tiêu cá nhân:** app Streamlit chạy rõ ràng từ lúc nhập nhu cầu đến lúc thấy top 3; người xem demo hiểu được kết quả trong chưa tới 1 phút.

| Ngày | Làm gì | Làm như thế nào | File cần tạo hoặc sửa | Khi nào được xem là xong |
| --- | --- | --- | --- | --- |
| 23/11 | Chạy baseline hiện tại | Clone/pull repo, cài dependency, chạy test và `streamlit run app.py`. Ghi lại các bước user đi qua | Tạo `docs/ui-checklist-week-1.md` | Checklist có: budget input, 5 sliders, top 3, all results, calculation details, error states |
| 24/11 | Kiểm tra input | Bảo đảm label, đơn vị VND/km/m² và ý nghĩa của 5 sliders dễ hiểu. Kiểm tra budget bằng 0 và all weights = 0 | Sửa `app.py` nếu cần | App hiển thị message English dễ hiểu, không crash |
| 25/11 | Làm kết quả top 3 dễ đọc | Bảng top 3 phải có ID, Room, 5 tiêu chí và TOPSIS score. Không để user phải mở code mới hiểu | Sửa `app.py` | Kết quả nhìn một lần biết vì sao phòng đứng top |
| 26/11 | Kiểm tra phần giải thích | Trong expander calculation, phải hiện normalized weights, `D+`, `D-`, `C` và mô tả ngắn bằng English | Sửa `app.py` nếu thiếu | Có thể dùng màn hình này để thuyết trình methodology |
| 27/11 | Chạy app với dữ liệu 30 phòng | Pull dataset mới, chạy 3 profile trọng số và 3 budget khác nhau | Tạo `docs/ui-smoke-check.md` | Ghi input dùng, kết quả quan sát, không có lỗi giao diện |
| 28/11 | Kiểm tra trên môi trường sạch | Clone repo sang một thư mục khác hoặc dùng máy khác; chạy lại hướng dẫn README từ đầu | Sửa `README.md` nếu bước chạy sai | Một máy khác có thể mở app chỉ bằng README |
| 29/11 | Đưa phần app lên GitHub | Tạo branch `feat/week-1-ui`, commit thay đổi UI/tài liệu UI, mở pull request | `app.py`, `README.md`, `docs/ui-*.md` | Pull request không lẫn code TOPSIS hoặc data nếu không cần |

**Luồng demo app cần giữ nguyên:**

```text
Nhập ngân sách
→ chỉnh 5 weights
→ xem top 3
→ mở calculation details
→ đổi weights
→ chỉ ra thứ hạng thay đổi
```

## 7. Plan chi tiết của Trần Việt Trung — Test và demo

**Mục tiêu cá nhân:** chứng minh app không chỉ “chạy được” mà còn xử lý đúng các trường hợp quan trọng; chuẩn bị demo có thể chạy khi mất mạng.

| Ngày | Làm gì | Làm như thế nào | File cần tạo hoặc sửa | Khi nào được xem là xong |
| --- | --- | --- | --- | --- |
| 23/11 | Lập checklist kiểm thử | Viết từng case, input, expected result và actual result. Case tối thiểu: valid CSV, invalid CSV, no match, one match, tie, zero weights, weight change | Tạo `docs/week-1-test-checklist.md` | Có ít nhất 7 test case, không ghi chung chung kiểu “test app” |
| 24/11 | Test dữ liệu sai | Tạo CSV tạm có ID trùng, cột thiếu, score = 6, score = 2.5, chi phí âm, area = 0 | Sửa `tests/test_data.py` khi thiếu test | Mỗi lỗi đều ra thông báo hợp lý và test tự động pass |
| 25/11 | Test ngân sách và xếp hạng | Kiểm tra budget nhỏ hơn mọi phòng, chỉ đủ 1 phòng, hai phòng bằng nhau, và đổi profile trọng số | Sửa `tests/test_topsis.py` hoặc checklist | Actual result trùng expected result đã ghi |
| 26/11 | Chạy toàn bộ test và ghi bug | Chạy `python -m unittest discover -s tests -v`; với lỗi UI, ghi bước tái hiện, expected, actual, ảnh nếu có | Sửa `docs/week-1-test-checklist.md` | Có bảng bug rõ ràng; bug nào không tái hiện được thì không ghi là bug |
| 27/11 | Viết kịch bản demo 5 phút | Chia thời gian: 30 giây problem, 60 giây input, 90 giây top 3, 90 giây đổi weights, 30 giây conclusion | Tạo `docs/week-1-demo-script.md` | Có lời nói ngắn bằng English và input cụ thể để demo |
| 28/11 | Chuẩn bị backup demo | Chụp ảnh màn hình hoặc quay video local; lưu đúng dataset và lệnh chạy app | Tạo thư mục/tài liệu demo phù hợp | Có thể chứng minh flow ngay cả khi Wi-Fi không ổn |
| 29/11 | Đưa phần test/demo lên GitHub | Tạo branch `test/week-1`, commit tests/checklist/script, mở pull request | `tests/`, `docs/week-1-test-checklist.md`, `docs/week-1-demo-script.md` | Pull request có kết quả test hoặc lệnh test đã chạy |

## 8. Checklist chung cuối tuần 1 — kiểm tra từng ô

| Hạng mục | Kết quả bắt buộc |
| --- | --- |
| Dữ liệu dùng chung | CSV có sẵn 30 phòng, ID không trùng, dữ liệu giả lập được gắn nhãn và test đọc file pass |
| Thuật toán | Có ví dụ TOPSIS tính tay cho 3 phòng và khớp với code |
| App | Nhập budget + 5 weights, trả về top 3 và calculation details |
| Test | Pass valid/invalid CSV, no match, one match, tie, zero weights và weight profiles |
| Demo | Có script 5 phút, screenshot/video backup, chạy local được |
| GitHub | Mỗi phần có branch/PR rõ ràng; không push thẳng hoặc force-push vào `main` |

## 9. Nếu bị trễ thì cắt gì trước?

Không cắt phần TOPSIS, dữ liệu, test hoặc demo. Cắt theo thứ tự này:

1. Bỏ CSV import/export.
2. Bỏ giao diện nâng cao và biểu đồ.
3. Bỏ dữ liệu thật, chỉ dùng synthetic data rõ ràng.
4. Bỏ deploy public; demo local bằng Streamlit.

Mục tiêu cuối tuần không phải là một app hoàn hảo. Mục tiêu là một DSS nhỏ, đúng logic, giải thích được và demo không lỗi.
