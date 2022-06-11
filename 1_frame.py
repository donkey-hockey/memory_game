import pygame
# 초기화
pygame.init()
screen_width = 1280  # 가로크기
screen_height = 720  # 세로 크기
screen = pygame.display.set_mode(
    (screen_width, screen_height))  # 가로세로 크기 값을 스크린에 저장

pygame.display.set_caption("memory game")  # 게임 제목

# 게임 루프
running = True  # 게임이 실행중인가를 확인하는 변수
while running:
    # 이벤트루프
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트인가?
            running = False  # 게임 종료


pygame.quit()  # 게임 종료
