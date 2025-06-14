import streamlit as st
import random

# Cấu hình trang
st.set_page_config(page_title="Snake Game", page_icon="🐍")

# Khởi tạo trạng thái
if "snake" not in st.session_state:
    st.session_state.snake = [(5, 5)]
    st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
    st.session_state.direction = "RIGHT"
    st.session_state.game_over = False

# Hàm vẽ lưới
def draw_grid():
    grid = ""
    for y in range(10):
        for x in range(10):
            if (x, y) == st.session_state.food:
                grid += "🍎"
            elif (x, y) in st.session_state.snake:
                grid += "🟩"
            else:
                grid += "⬜"
        grid += "\n"
    return grid

# Di chuyển rắn
def move_snake():
    if st.session_state.game_over:
        return

    head_x, head_y = st.session_state.snake[0]
    direction = st.session_state.direction

    if direction == "UP":
        head_y -= 1
    elif direction == "DOWN":
        head_y += 1
    elif direction == "LEFT":
        head_x -= 1
    elif direction == "RIGHT":
        head_x += 1

    new_head = (head_x, head_y)

    # Kiểm tra va chạm
    if (new_head in st.session_state.snake or
        not 0 <= head_x < 10 or not 0 <= head_y < 10):
        st.session_state.game_over = True
        return

    st.session_state.snake = [new_head] + st.session_state.snake

    if new_head == st.session_state.food:
        st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
    else:
        st.session_state.snake.pop()

# Hiển thị trò chơi
st.title("🐍 Snake Game (Streamlit phiên bản đơn giản)")
st.markdown(draw_grid())

# Hiển thị điều khiển
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("⬆️"):
        st.session_state.direction = "UP"

col1, _, col3 = st.columns([1, 0.2, 1])
with col1:
    if st.button("⬅️"):
        st.session_state.direction = "LEFT"
with col3:
    if st.button("➡️"):
        st.session_state.direction = "RIGHT"

col1, col2, col3 = st.columns(3)
with col2:
    if st.button("⬇️"):
        st.session_state.direction = "DOWN"

# Tự động di chuyển mỗi lần chạy
move_snake()

# Kết thúc
if st.session_state.game_over:
    st.error("💀 Game Over! Nhấn nút dưới để chơi lại.")
    if st.button("🔁 Chơi lại"):
        st.session_state.snake = [(5, 5)]
        st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
        st.session_state.direction = "RIGHT"
        st.session_state.game_over = False
