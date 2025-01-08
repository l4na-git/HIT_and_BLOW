# ゲームの処理

from main import DisplayMain
import pygame
import sys
import os

img_list = [
    'number0.png', 'number1.png', 'number2.png', 'number3.png', 'number4.png',
    'number5.png', 'number6.png', 'number7.png', 'number8.png', 'number9.png'
]


class DisplayGame(DisplayMain):
    def get_data(self):
        """ ファイルからデータを取得 """
        FONT_FILE_PATH = os.path.dirname(__file__) + r"\mgenplus-1p-regular.ttf"
        text_font = pygame.font.Font(FONT_FILE_PATH, 20)
        return text_font

    def create_button(self, screen):
        button_list = []
        """ ボタンの作成 """
        for i, img in enumerate(img_list):
            img = pygame.image.load('images/' + img)
            img = pygame.transform.scale(img, (65, 65))
            rect = pygame.Rect((45 + i * 87, 450), img.get_rect().size)
            screen.blit(img, rect)
            button_list.append(rect)

        return button_list

    def key_event(self, event, button_list, screen, text_font):
        """ キーイベントの処理 """
        for i, button in enumerate(button_list):
            if button.collidepoint(event.pos):
                show_text = text_font.render(str(i), True, (20, 33, 67))
                screen.blit(show_text, (300, 300))
                print(i)

    def event_loop(self, screen, back_img, rect_back, text_font):
        """ イベントのループ処理 """
        running = True
        while running:
            screen.fill((255, 255, 255))
            screen.blit(back_img, rect_back)  # 背景画像の描画

            button_list = self.create_button(screen)
            info_button, sound_button = self.create_info_sound(screen)

            pygame.display.update()  # 描画処理を実行

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 閉じるボタンが押されたとき
                    running = False
                    pygame.quit()  # ウィンドウを閉じる
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.key_info_sound(event, info_button, sound_button)
                    self.key_event(event, button_list, screen, text_font)

    def main(self):
        """ メインの関数 """
        pygame.init()  # 初期化

        screen, back_img, rect_back = self.create_screen(pygame)

        pygame.display.set_caption(self.TITLE)  # タイトルを作成

        text_font = self.get_data()

        self.event_loop(screen, back_img, rect_back, text_font)


if __name__ == "__main__":
    display = DisplayGame('3digit_back.png')
    display.main()
