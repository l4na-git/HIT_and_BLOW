
import pygame
import sys

SCREEN_SIZE = (700, 570)
BACKGROUND_COLOR = (228, 228, 228)  # (R, G, B)
TITLE_COLOR = (20, 33, 67)
TITLE = "Hit & Blow"


def main():
    pygame.init()    # Pygameを初期化
    screen = pygame.display.set_mode(SCREEN_SIZE)    # 画面を作成
    pygame.display.set_caption(TITLE)    # タイトルを作成

    font = pygame.font.SysFont("gothicg", 110)
    text = font.render(TITLE, True, TITLE_COLOR)

    running = True
    # メインループ
    while running:
        screen.fill(BACKGROUND_COLOR)
        screen.blit(text, (150, 70))  # タイトルを描画
        pygame.display.update()  # 描画処理を実行

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 終了イベント
                running = False
                pygame.quit()  # pygameのウィンドウを閉じる
                sys.exit()  # システム終了


if __name__ == "__main__":
    main()
