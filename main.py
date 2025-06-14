import streamlit as st

# --- Cấu hình trang ---
st.set_page_config(page_title="Ứng dụng Bán Hàng", page_icon="🛒")

# --- Tiêu đề ---
st.title("🛍️ Ứng dụng Bán Hàng Đơn Giản")

# --- Dữ liệu sản phẩm mẫu ---
products = {
    "Áo thun": 150000,
    "Quần jeans": 300000,
    "Giày thể thao": 500000,
    "Mũ lưỡi trai": 100000
}

# --- Khởi tạo session state cho giỏ hàng ---
if "cart" not in st.session_state:
    st.session_state.cart = {}

# --- Form chọn sản phẩm ---
st.subheader("🛒 Chọn sản phẩm")

with st.form("add_to_cart_form"):
    product = st.selectbox("Chọn sản phẩm:", list(products.keys()))
    quantity = st.number_input("Số lượng:", min_value=1, value=1, step=1)
    submitted = st.form_submit_button("Thêm vào giỏ")

    if submitted:
        if product in st.session_state.cart:
            st.session_state.cart[product] += quantity
        else:
            st.session_state.cart[product] = quantity
        st.success(f"✅ Đã thêm {quantity} {product} vào giỏ hàng!")

# --- Hiển thị giỏ hàng ---
st.subheader("🧾 Giỏ hàng của bạn")
if st.session_state.cart:
    total = 0
    for item, qty in st.session_state.cart.items():
        price = products[item]
        item_total = price * qty
        total += item_total
        st.write(f"- {item} x {qty} = {item_total:,} VND")
    st.markdown(f"### 💵 Tổng cộng: **{total:,} VND**")

    # --- Nút thanh toán ---
    if st.button("✅ Thanh toán"):
        st.success("🎉 Thanh toán thành công!")
        st.session_state.cart.clear()

    # --- Nút xóa giỏ hàng ---
    if st.button("🗑️ Xóa giỏ hàng"):
        st.session_state.cart.clear()
        st.info("🛒 Giỏ hàng đã được làm trống.")
else:
    st.info("Giỏ hàng hiện đang trống.")
