import pygame
import time
import random

# Khởi tạo pygame
pygame.init()

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Kích thước cửa sổ
width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('🐍 Snake Game - by ChatGPT')

# Clock
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

def your_score(score):
    value = score_font.render("Điểm: " + str(score), True, green)
    win.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    snake_list = []
    length = 1

    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10

    while not game_over:

        while game_close:
            win.fill(blue)
            message("Bạn thua! Nhấn C để chơi lại hoặc Q để thoát", red)
            your_score(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Kiểm tra va chạm tường
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        win.fill(blue)

        pygame.draw.rect(win, green, [food_x, food_y, snake_block, snake_block])
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        your_score(length - 1)

        pygame.display.update()

        # Khi ăn thức ăn
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Bắt đầu trò chơi
gameLoop()
