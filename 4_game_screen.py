# 게임 화면 만들기.
# 몇개의 숫자를 보여줄지 정의
# 격자도 만들어야함 - 리스트의 중복.


import pygame
from random import *

# 레벨에 맞게 설정


def setup(level):
    # 얼마나 많은 숫자를 보여줄것인가
    number_count = (level // 3) + 5
    number_count = min(number_count, 20)  # 최대값 제한

    # 격자 그리고 숫자 랜덤 배치
    shuffle_grid(number_count)

# 숫자 섞기 ( 가장 중요 )


def shuffle_grid(number_count):
    rows = 5
    columns = 9

    grid = [[0 for col in range(columns)]
            for row in range(rows)]  # 5x9에 해당하는 격자

    # 격자에 숫자 집어 넣기.
    number = 1  # 시작 숫자를 1~ number_count 까지 숫자를 랜덤으로 배치하기.
    while number <= number_count:
        # 좌표 랜덤 뽑기
        row_idx = randrange(0, rows)
        col_idx = randrange(0, columns)

        # 해당 좌표 값이 0인지 확인하고 숫자를 집어넣어야한다.
        if grid[row_idx][col_idx] == 0:  # 빈값이면
            grid[row_idx][col_idx] = number  # 숫자 지정
            number += 1

    print(grid)  # 배치된 랜덤숫자확인


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center,
                       60, 5)


def display_game_screen():
    print("gaem start")


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

start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

start = False

# 게임 시작 전에 게임 설정 함수 수정.
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
