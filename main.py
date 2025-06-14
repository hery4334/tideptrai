import streamlit as st
import random

st.set_page_config(page_title="🐍 Snake Game", page_icon="🐍")

# Khởi tạo
if "snake" not in st.session_state:
    st.session_state.snake = [(5, 5)]
    st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
    st.session_state.direction = "RIGHT"
    st.session_state.game_over = False

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

def move_snake():
    if st.session_state.game_over:
        return

    x, y = st.session_state.snake[0]
    if st.session_state.direction == "UP": y -= 1
    elif st.session_state.direction == "DOWN": y += 1
    elif st.session_state.direction == "LEFT": x -= 1
    elif st.session_state.direction == "RIGHT": x += 1

    new_head = (x, y)

    if (new_head in st.session_state.snake or
        not 0 <= x < 10 or not 0 <= y < 10):
        st.session_state.game_over = True
        return

    st.session_state.snake = [new_head] + st.session_state.snake
    if new_head == st.session_state.food:
        st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
    else:
        st.session_state.snake.pop()

st.title("🐍 Snake Game (Streamlit)")

st.text(draw_grid())

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

move_snake()

if st.session_state.game_over:
    st.error("💀 Game Over!")
    if st.button("🔁 Chơi lại"):
        st.session_state.snake = [(5, 5)]
        st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
        st.session_state.direction = "RIGHT"
        st.session_state.game_over = False
