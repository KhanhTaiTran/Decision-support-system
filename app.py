"""Run after installation: python -m streamlit run app.py."""

from pathlib import Path
import streamlit as st
from housing_dss.criteria import CRITERIA
from housing_dss.data import load_rooms
from housing_dss.topsis import rank_rooms

st.set_page_config(page_title="DSS chọn phòng trọ", layout="wide")
st.title("Hỗ trợ sinh viên chọn phòng trọ")
st.caption("Bản khởi tạo · Dữ liệu giả lập để phát triển và demo, không phải tin cho thuê thực tế.")

with st.sidebar:
    st.header("Nhu cầu của bạn")
    budget = st.number_input("Ngân sách tối đa / tháng (VND)", min_value=0, value=4000000, step=100000)
    st.subheader("Mức ưu tiên")
    weights = {key: st.slider(label, 0, 100, 20, key=key) for key, (label, _) in CRITERIA.items()}

try:
    rooms = load_rooms(Path(__file__).parent / "data" / "rooms_sample.csv")
    eligible = [room for room in rooms if room["monthly_cost_vnd"] <= budget]
    ranked = rank_rooms(eligible, weights)
except (ValueError, OSError) as error:
    st.error(str(error))
    st.stop()

if not ranked:
    st.info("Không có phòng trong ngân sách. Hãy tăng ngân sách để xem thêm lựa chọn.")
    st.stop()
if len(ranked) == 1:
    st.info("Chỉ có một phòng đủ điều kiện. Chưa có phương án khác để so sánh.")

st.subheader(f"Top {min(3, len(ranked))} trong {len(ranked)} phòng đủ điều kiện")
labels = {key: value[0] for key, value in CRITERIA.items()}
def display(rows):
    return [{"ID": room["id"], "Tên phòng": room["name"],
             **{labels[key]: room[key] for key in CRITERIA},
             "Điểm TOPSIS": round(room["score"], 4)} for room in rows]

st.dataframe(display(ranked[:3]), width="stretch", hide_index=True)
st.caption("Điểm thể hiện thứ hạng tương đối trong tập phòng hiện tại, không phải xác suất phù hợp. "
           "Các phòng đồng hạng được hiển thị theo ID. Trường hợp không có khác biệt, điểm là 0,5.")
with st.expander("Toàn bộ kết quả"):
    st.dataframe(display(ranked), width="stretch", hide_index=True)
with st.expander("Cách tính và trọng số đang dùng"):
    total = sum(weights.values())
    st.write({labels[key]: f"{value / total:.1%}" for key, value in weights.items()})
    st.write("Lọc ngân sách → chuẩn hóa vector → nhân trọng số → xác định phương án lý tưởng "
             "theo cost/benefit → tính D+, D- → C = D- / (D+ + D-).")
    st.dataframe([{"ID": r["id"], "D+": r["d_plus"], "D-": r["d_minus"], "C": r["score"]}
                  for r in ranked], hide_index=True)
