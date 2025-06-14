import streamlit as st

# --- Dummy user credentials ---
users = {
    "admin": "admin123",
    "user1": "password1",
    "user2": "password2"
}

# --- Page title ---
st.set_page_config(page_title="Login Page", page_icon="🔐")
st.title("🔐 Login Page")

# --- Login Form ---
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.form_submit_button("Login")

# --- Authentication Logic ---
if login_btn:
    if username in users and users[username] == password:
        st.success(f"Welcome, {username}! 🎉")
        st.balloons()
    else:
        st.error("Invalid username or password ❌")
