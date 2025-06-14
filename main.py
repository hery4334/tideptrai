import streamlit as st

# Dummy credentials
users = {
    "admin": "admin123",
    "user1": "password1"
}

st.set_page_config(page_title="Login Page", page_icon="🔒")
st.title("🔐 Login Page")

# Form Login
with st.form("login"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

# Logic
if submit:
    if username in users and users[username] == password:
        st.success(f"Welcome, {username}!")
        st.balloons()
    else:
        st.error("Invalid username or password.")
