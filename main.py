import streamlit as st
from datetime import datetime

# Dữ liệu báo mẫu
news_data = [
    {
        "title": "Việt Nam thắng đậm Thái Lan 3-0 tại AFF Cup",
        "content": "Đội tuyển Việt Nam đã thi đấu thăng hoa và giành chiến thắng trước Thái Lan với tỉ số 3-0 trong trận chung kết lượt đi AFF Cup...",
        "image": "https://cdnmedia.baotintuc.vn/Upload/zWp5cYx9kgfy0sBAo7FQ/files/vietnam-thailand.jpg",
        "date": "2025-06-13"
    },
    {
        "title": "Bộ Giáo dục công bố lịch thi tốt nghiệp THPT 2025",
        "content": "Bộ GD&ĐT vừa công bố lịch thi tốt nghiệp THPT quốc gia năm 2025. Kỳ thi sẽ diễn ra trong ba ngày, từ 25 đến 27 tháng 6...",
        "image": "https://i1-vnexpress.vnecdn.net/2024/04/01/thi-thpt-quoc-gia.jpg",
        "date": "2025-06-12"
    },
    {
        "title": "TP.HCM cấm xe máy khu trung tâm từ năm 2030",
        "content": "Chính quyền thành phố Hồ Chí Minh vừa công bố kế hoạch cấm xe máy vào khu trung tâm từ năm 2030 để giảm ùn tắc và ô nhiễm...",
        "image": "https://cdn.tuoitre.vn/thumb_w/730/471584752817336320/2024/4/22/xe-may-1713754067717908856906.jpeg",
        "date": "2025-06-10"
    }
]

# Cài đặt trang
st.set_page_config(page_title="📰 Trang đọc báo", page_icon="🗞️", layout="wide")

# Header
st.title("🗞️ Trang Đọc Báo Online")
st.markdown("Chào mừng bạn đến với trang báo điện tử Streamlit!")

# Sidebar: chọn bài viết
titles = [item["title"] for item in news_data]
selected_title = st.sidebar.selectbox("📰 Chọn bài viết", titles)

# Hiển thị bài viết được chọn
selected_article = next(item for item in news_data if item["title"] == selected_title)

st.image(selected_article["image"], use_column_width=True)
st.header(selected_article["title"])
st.caption(f"🗓️ Ngày đăng: {selected_article['date']}")
st.markdown(selected_article["content"])

# Footer
st.markdown("---")
st.markdown("© 2025 - Trang đọc báo Streamlit | Thiết kế bởi bạn và ChatGPT 😄")
