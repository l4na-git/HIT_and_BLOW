# 音量調整する画面

import os
import sys
from . import info
import pygame

text_line = [
    '矢印キーで音量を調整できます。',
    '↑: ボリュームアップ',
    '↓: ボリュームダウン',
    '←: 再生中止',
    '→: 再生'
]


class DisplaySound(info.DisplayInfo):
    def get_data(self):
        """ ファイルからデータを取得 """
        FONT_FILE_PATH = os.path.dirname(__file__) + r"\mgenplus-1p-regular.ttf"
        text_font = pygame.font.Font(FONT_FILE_PATH, 20)
        return text_font

    def display_text(self, screen, text_font):
        """ 案内 """
        num = 0
        for line in text_line:
            show_info_text = text_font.render(line, True, (20, 33, 67))
            screen.blit(show_info_text, (350, 160 + num))
            num += 45

    def change_volume(self, event):
        if event.type == pygame.KEYDOWN:
            # 「↑」キーを押下するとボリュームを上げることができる
            if event.key == pygame.K_UP:
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v + 0.1)
                print("volume up")
            # 「↓」キーを押下するとボリュームを下げることができる
            if event.key == pygame.K_DOWN:
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v - 0.1)
                print("volume down")
            # 「←」キーを押下すると再生されるMP3中止される
            if event.key == pygame.K_LEFT:
                pygame.mixer.music.pause()
                print("stop")
            # 「→」キーを押下するとサンプルファイルが再生できる
            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.unpause()
                print("re-play")

    def event_loop(self, screen, back_img, rect_back, text_font):
        """ イベントのループ処理 """
        running = True
        while running:
            screen.fill((255, 255, 255))
            screen.blit(back_img, rect_back)  # 背景画像の描画

            back_button = self.create_button(screen)
            self.display_text(screen, text_font)  # テキストの描画

            pygame.display.update()  # 描画処理を実行

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 閉じるボタンが押されたとき
                    running = False
                    pygame.quit()  # ウィンドウを閉じる
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.key_event(event, back_button)
                    self.change_volume(event)

    def main(self):
        """ メインの関数 """
        pygame.init()  # 初期化

        screen, back_img, rect_back = self.create_screen(pygame)

        pygame.display.set_caption(self.TITLE)  # タイトルを作成

        text_font = self.get_data()

        self.event_loop(screen, back_img, rect_back, text_font)


if __name__ == "__main__":
    display = DisplaySound('sound_back.png')
    display.main()
