# 遊び方を表示
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from . import base
from utils.file_utils import read_all_file
import pygame


class DisplayInfo(base.DisplayBase):
    def create_button(self, screen):
        """ ボタンの作成 """
        back_img = pygame.image.load('images/back_button.png')
        back_img = pygame.transform.scale(back_img, (50, 50))
        back_rect = pygame.Rect((445, 450), back_img.get_rect().size)
        screen.blit(back_img, back_rect)
        return back_rect

    def key_event(self, event, back_button):
        """ キーイベントの処理 """
        if back_button.collidepoint(event.pos):
            from main import DisplayMain
            display = DisplayMain('root_back.png')
            display.main()

    def get_data(self):
        """ ファイルからデータを取得 """
        line_data = read_all_file(os.path.dirname(__file__) + r'\..\conf\how_to.txt')
        FONT_FILE_PATH = os.path.dirname(__file__) + r"\mgenplus-1p-regular.ttf"
        text_font = pygame.font.Font(FONT_FILE_PATH, 15)
        return line_data, text_font

    def display_info(self, screen, line_data, text_font):
        num = 0
        for line in line_data:
            show_info_text = text_font.render(line, True, (20, 33, 67))
            screen.blit(show_info_text, (285, 110 + num))
            num += 20

    def event_loop(self, screen, back_img, rect_back, line_data, text_font):
        """ イベントのループ処理 """
        running = True
        while running:
            screen.fill((255, 255, 255))
            screen.blit(back_img, rect_back)  # 背景画像の描画

            back_button = self.create_button(screen)
            self.display_info(screen, line_data, text_font)  # テキストの描画

            pygame.display.update()  # 描画処理を実行

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 閉じるボタンが押されたとき
                    running = False
                    pygame.quit()  # ウィンドウを閉じる
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.key_event(event, back_button)

    def main(self):
        """ メインの関数 """
        pygame.init()  # 初期化

        screen, back_img, rect_back = self.create_screen(pygame)

        pygame.display.set_caption(self.TITLE)  # タイトルを作成

        line_data, text_font = self.get_data()

        self.event_loop(screen, back_img, rect_back, line_data, text_font)


if __name__ == "__main__":
    display = DisplayInfo('info_back.png')
    display.main()
