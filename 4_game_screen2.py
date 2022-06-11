# 이후 격자에 숫자 그려넣어야함

import pygame
from random import *


def setup(level):
    number_count = (level // 3) + 5
    number_count = min(number_count, 20)

    shuffle_grid(number_count)


def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130  # 각 grid의 cell별 가로,세로크기
    button_size = 110  # 각 grid cell 내에 실제로 그려질 버튼 크기
    screen_left_margin = 55  # 전체 스크린의 왼쪽 여백
    screen_top_margin = 20  # 전체 스크린 위쪽 여백

    grid = [[0 for col in range(columns)]
            for row in range(rows)]

    number = 1
    while number <= number_count:
        row_idx = randrange(0, rows)
        col_idx = randrange(0, columns)

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            # 숫자 그리기
            # 현재 그리드 셀 위치 기준으로 x, y 위치 구하기
            center_x = screen_left_margin + col_idx*cell_size + cell_size/2
            center_y = screen_top_margin + row_idx*cell_size + cell_size/2

            # 좌표에 해당하는 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            # 버튼들을 새로운 리스트에 집어 넣기
            number_buttons.append(button)

    print(grid)


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center,
                       60, 5)


def display_game_screen():
    for idx, rect in enumerate(number_buttons, start=1):
        pygame.draw.rect(screen, GRAY, rect)

        # 숫자 텍스트 그리기
        # 먼저 바깥에서 폰트 정의
        cell_text = game_font.render(str(idx), True, WHITE)
        # 그리기
        text_rect = cell_text.get_rect(
            center=rect.center)  # 버튼의 중간값을 텍스트에 적용하기 위함
        screen.blit(cell_text, text_rect)


def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode(
    (screen_width, screen_height))

pygame.display.set_caption("memory game")

# 게임 폰트 정의
game_font = pygame.font.Font(None, 120)

start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

# 플레이어가 눌러야하는 버튼들을 관리하는 리스트
number_buttons = []

start = False

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
