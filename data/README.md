# Dữ liệu phòng trọ

`rooms_sample.csv` chứa 8 phòng **giả lập**, chỉ để chạy bản khởi tạo. An mở rộng lên 30–50 phòng theo kế hoạch. Tất cả khoảng cách lấy cùng một điểm trường giả định. Không coi đây là dữ liệu thị trường.

- `id`: duy nhất, không rỗng.
- `name`: tên phòng, không rỗng.
- `monthly_cost_vnd`: tổng tiền thuê và phí cố định ước tính mỗi tháng, VND, > 0. Tiêu chí cost.
- `distance_km`: khoảng cách tới trường, km, >= 0. Tiêu chí cost.
- `area_m2`: diện tích sử dụng, m², > 0. Tiêu chí benefit.
- `security_score`: số nguyên 1–5, bằng 1 + số điều kiện đạt: khóa riêng, kiểm soát ra vào, camera khu chung, chiếu sáng lối vào.
- `amenities_score`: số nguyên 1–5, bằng 1 + số điều kiện đạt: WC riêng, chỗ nấu ăn, wifi, chỗ để xe.
- `source`: `synthetic` cho phòng giả lập. Dữ liệu thật cần URL nguồn và ngày thu thập trong các cột mở rộng.

CSV dùng UTF-8. Không đưa dữ liệu cá nhân hoặc thông tin liên hệ riêng lên repo. Không trộn dữ liệu thật và giả lập mà thiếu nhãn nguồn.
