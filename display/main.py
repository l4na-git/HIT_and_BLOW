# 起動時の画面表示を行う

from . import base
from . import how_to
from . import sound
import pygame
import sys


class DisplayMain(base.DisplayBase):
    def create_info_sound(self, screen):
        """ 遊び方と音量調整ボタンの作成 """
        info_img = pygame.image.load('images/info_button.png')
        sound_img = pygame.image.load('images/sound_button.png')

        info_img = pygame.transform.scale(info_img, (70, 70))
        sound_img = pygame.transform.scale(sound_img, (70, 85))

        info_rect = pygame.Rect((830, 30), info_img.get_rect().size)
        sound_rect = pygame.Rect((40, 25), sound_img.get_rect().size)

        screen.blit(info_img, info_rect)
        screen.blit(sound_img, sound_rect)

        return info_rect, sound_rect

    def key_info_sound(self, event, info_button, sound_button):
        """ 遊び方と音量調整ボタンの処理 """
        if info_button.collidepoint(event.pos):
            display = how_to.DisplayInfo('info_back.png')
            display.main()
        if sound_button.collidepoint(event.pos):
            display = sound.DisplaySound('sound_back.png')
            display.main()

    def create_button(self, screen):
        """ ボタンの作成 """
        digit3_img = pygame.image.load('images/3digit_button.png')
        digit4_img = pygame.image.load('images/4digit_button.png')

        digit3_img = pygame.transform.scale(digit3_img, (200, 65))
        digit4_img = pygame.transform.scale(digit4_img, (200, 65))

        digit3_rect = pygame.Rect((360, 215), digit3_img.get_rect().size)
        digit4_rect = pygame.Rect((360, 325), digit4_img.get_rect().size)

        screen.blit(digit3_img, digit3_rect)
        screen.blit(digit4_img, digit4_rect)

        return digit3_rect, digit4_rect

    def key_event(self, event, digit3_button, digit4_button):
        """ キーイベントの処理 """
        from play import DisplayGame
        if digit3_button.collidepoint(event.pos):
            display = DisplayGame('3digit_back.png')
            display.main()
        if digit4_button.collidepoint(event.pos):
            display = DisplayGame('4digit_back.png')
            display.main()

    def event_loop(self, screen, back_img, rect_back):
        """ イベントのループ処理 """
        running = True
        while running:
            screen.fill((255, 255, 255))
            screen.blit(back_img, rect_back)  # 背景画像の描画

            digit3_button, digit4_button = self.create_button(screen)
            info_button, sound_button = self.create_info_sound(screen)

            pygame.display.update()  # 描画処理を実行

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 閉じるボタンが押されたとき
                    running = False
                    pygame.quit()  # ウィンドウを閉じる
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.key_info_sound(event, info_button, sound_button)
                    self.key_event(event, digit3_button, digit4_button)


if __name__ == "__main__":
    display = DisplayMain('root_back.png')
    display.main()
