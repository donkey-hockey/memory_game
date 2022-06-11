# 숫자 숨기기
# 시간 초과
# 타이머 사용.

import pygame
from random import *


def setup(level):
    # 얼마동안 숫자를 보여줄지 정의
    global display_time
    display_time = 5 - (level // 3)
    display_time = max(display_time, 1)  # 1초 미만이면 1초로 처리

    number_count = (level // 3) + 5
    number_count = min(number_count, 20)

    shuffle_grid(number_count)


def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130
    button_size = 110
    screen_left_margin = 55
    screen_top_margin = 20

    grid = [[0 for col in range(columns)]
            for row in range(rows)]

    number = 1
    while number <= number_count:
        row_idx = randrange(0, rows)
        col_idx = randrange(0, columns)

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            center_x = screen_left_margin + col_idx*cell_size + cell_size/2
            center_y = screen_top_margin + row_idx*cell_size + cell_size/2

            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)

    print(grid)


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center,
                       60, 5)


def display_game_screen():
    global hidden
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() -
                        start_ticks) / 1000  # ms -> s로 단위 바꾸기
        if elapsed_time > display_time:
            hidden = True

    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            pygame.draw.rect(screen, WHITE, rect)
        else:
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(
                center=rect.center)
            screen.blit(cell_text, text_rect)


def check_buttons(pos):
    global start, start_ticks

    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks()  # 타이머를 시작 (현재시간 저장)


def check_number_buttons(pos):
    global hidden
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                print("correct")
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                print("wrong")
            break


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode(
    (screen_width, screen_height))

pygame.display.set_caption("memory game")

game_font = pygame.font.Font(None, 120)

start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

number_buttons = []
display_time = None  # 숫자를 보여주는 시간
start_ticks = None  # 시간계산 (현재 시간정보 저장)

start = False

hidden = False

setup(1)

running = True
while running:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    screen.fill(BLACK)

    if start:
        display_game_screen()
    else:
        display_start_screen()

    if click_pos:
        check_buttons(click_pos)

    pygame.display.update()

pygame.quit()
