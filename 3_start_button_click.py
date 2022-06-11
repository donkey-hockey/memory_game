# 시작버튼 클릭 - 클릭하면 게임화면으로 넘어가기.

import pygame


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center,
                       60, 5)


def display_game_screen():  # 게임화면 보여주기
    print("gaem start")


def check_buttons(pos):  # 포지션에 해당하는 버튼을 확인해서 필요한 동작 처리.
    global start
    if start_button.collidepoint(pos):  # 사용자가 클릭한 위치가 스타트버튼에 포함된다면,
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

# 게임 시작 여부 판단
start = False

running = True
while running:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:  # 사용자가 마우스를 클릭했을때
            click_pos = pygame.mouse.get_pos()  # 클릭 좌표정보를 확인
            print(click_pos)

    screen.fill(BLACK)

    if start:  # 게임 화면을 표시
        display_game_screen()
    else:
        # 시작화면 표시
        display_start_screen()

    # 사용자가 클릭한 좌표값이 있다면( 어딘가 클릭했다면 )
    if click_pos:
        check_buttons(click_pos)

    pygame.display.update()


pygame.quit()
