# 숫자 숨기기
#  클릭했을떄 남은 숫자들

import pygame
from random import *


def setup(level):
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
    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:  # 숨김 처리
            # 버튼 사격형 그리기
            pygame.draw.rect(screen, WHITE, rect)
        else:
            # 실제 숫자 텍스트 보여주기
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(
                center=rect.center)
            screen.blit(cell_text, text_rect)


def check_buttons(pos):
    global start
    if start:  # 게임이 시작 했으면?
        check_number_buttons(pos)  # 숫자가 올바르게 클릭되었는지 확인
    elif start_button.collidepoint(pos):  # 게임시작안했으면 시작
        start = True


def check_number_buttons(pos):
    global hidden
    # 사용자가 클릭한 좌표가 버튼리스트의 첫번째안에 있는지 확인
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:  # 올바른 숫자를 클릭
                print("correct")
                del number_buttons[0]  # 첫번째꺼 삭제
                if not hidden:
                    hidden = True  # 숫자 숨김 처리
            else:  # 잘못된 숫자 클릭
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

start = False

hidden = False  # 숫자 숨김 여부, 사용자가 1을 클릭했거나 보여주는 시간을 초과했을때.

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
