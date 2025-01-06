# 遊び方を表示
import os
import sys
import pygame
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils.file_utils import read_all_file
import pygame
import sys
import os

SCREEN_SIZE = (700, 570)
BACKGROUND_COLOR = (228, 228, 228)  # (R, G, B)
TITLE_COLOR = (20, 33, 67)
TITLE = "Hit & Blow"
FONT_FILE_PATH = os.path.dirname(__file__) + r"\mgenplus-1p-regular.ttf"
BUTTON_COLOR = (26, 93, 148)
line_data = read_all_file(os.path.dirname(__file__) + r'\..\conf\how_to.txt')


def main():
    pygame.init()    # Pygameを初期化
    screen = pygame.display.set_mode(SCREEN_SIZE)    # 画面を作成
    pygame.display.set_caption(TITLE)    # タイトルを作成

    font = pygame.font.Font(FONT_FILE_PATH, 45)
    button_font = pygame.font.Font(FONT_FILE_PATH, 25)
    text_font = pygame.font.Font(FONT_FILE_PATH, 15)

    # 左上の頂点ｘ座標、左上ｙ座標、横幅（px）、高さ（px）
    back_button = pygame.Rect(295, 470, 130, 50)

    title = font.render("遊び方", True, TITLE_COLOR)
    back_test = button_font.render("戻る", True, BACKGROUND_COLOR)

    running = True
    # メインループ
    while running:
        screen.fill(BACKGROUND_COLOR)

        pygame.draw.rect(screen, BUTTON_COLOR, back_button)

        screen.blit(title, (290, 40))  # タイトルを描画
        screen.blit(back_test, (335, 477))  # 戻るボタンを描画

        num = 0
        for line in line_data:
            show_info_test = text_font.render(line, True, TITLE_COLOR)
            screen.blit(show_info_test, (145, 120 + num))
            num += 20

        pygame.display.update()  # 描画処理を実行

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 終了イベント
                running = False
                pygame.quit()  # pygameのウィンドウを閉じる
                sys.exit()  # システム終了

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    import main
                    main.main()
                    print("back to main menu")


if __name__ == "__main__":
    main()
