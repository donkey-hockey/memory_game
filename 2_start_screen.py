# 스타트 버튼 그리기 - 사각형을 이용해 버튼을 만들고 중심점을 기준으로 해서 동그라미를 그리기.

import pygame

# 시작화면 보여주는 함수


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center,
                       60, 5)  # 반지름 60, 선두께는 5
    # 흰색으로 동그라미를 그리는데 중심좌표는 start_button의 중심좌표를 따라간다.


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode(
    (screen_width, screen_height))

pygame.display.set_caption("memory game")

# 시작버튼 만들기
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)  # 스타트 버튼 놓이는 위치

# 색
BLACK = (0, 0, 0)  # rgb값
WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 검정으로 색칠
    screen.fill(BLACK)

    # 시작 화면 표시
    display_start_screen()

    # 화면 업데이트
    pygame.display.update()


pygame.quit()
