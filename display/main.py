
import pygame
import sys
import os

SCREEN_SIZE = (700, 570)
BACKGROUND_COLOR = (228, 228, 228)  # (R, G, B)
TITLE_COLOR = (20, 33, 67)
TITLE = "Hit & Blow"
FONT_FILE_PATH = os.path.dirname(__file__) + r"\mgenplus-1p-regular.ttf"
BUTTON_COLOR = (26, 93, 148)


def main():
    pygame.init()    # Pygameを初期化
    screen = pygame.display.set_mode(SCREEN_SIZE)    # 画面を作成
    pygame.display.set_caption(TITLE)    # タイトルを作成

    font = pygame.font.SysFont("gothicg", 110)
    button_font = pygame.font.Font(FONT_FILE_PATH, 30)

    # 左上の頂点ｘ座標、左上ｙ座標、横幅（px）、高さ（px）
    show_info_button = pygame.Rect(250, 200, 200, 65)
    show_three_button = pygame.Rect(250, 285, 200, 65)
    show_four_button = pygame.Rect(250, 370, 200, 65)

    title = font.render(TITLE, True, TITLE_COLOR)
    show_info_test = button_font.render("遊び方", True, BACKGROUND_COLOR)
    show_three_test = button_font.render("3桁モード", True, BACKGROUND_COLOR)
    show_four_test = button_font.render("4桁モード", True, BACKGROUND_COLOR)

    running = True
    # メインループ
    while running:
        screen.fill(BACKGROUND_COLOR)

        pygame.draw.rect(screen, BUTTON_COLOR, show_info_button)
        pygame.draw.rect(screen, BUTTON_COLOR, show_three_button)
        pygame.draw.rect(screen, BUTTON_COLOR, show_four_button)

        screen.blit(title, (150, 70))  # タイトルを描画
        screen.blit(show_info_test, (300, 210))  # 遊び方ボタンを描画
        screen.blit(show_three_test, (285, 295))  # 3桁モードボタンを描画
        screen.blit(show_four_test, (285, 380))  # 4桁モードボタンを描画

        pygame.display.update()  # 描画処理を実行

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 終了イベント
                running = False
                pygame.quit()  # pygameのウィンドウを閉じる
                sys.exit()  # システム終了


if __name__ == "__main__":
    main()
