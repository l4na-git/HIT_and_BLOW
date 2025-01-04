# メニュー表示

from quiz import Quiz
from how_to import main
from sound import set_file, delete_volume_file, volume
from keyboard_utils import input_int
import log_utils
import file_utils
import asyncio

# 装飾とタイトル
DECO = '=' * 70
TITLE = '                            Hit&Blow'

# メニュー番号
MENU_HOW_TO = 1  # 遊び方
VOLUME_SETTING = 2  # 音量の設定
SHOW_LOG = 3  # ログの表示
MENU_3_DIGIT = 4  # 3桁モード
MENU_4_DIGIT = 5  # 4桁モード
MENU_EXIT = 9  # 終了


async def execute():
    """ メインの関数 """
    while True:
        # メニューを表示
        print_menu()

        # メニュー番号の入力
        num = input_int('メニュー番号を入力してください: ')

        # メニュー番号の機能を実行
        await execute_menu(num)


def print_menu():
    """ メニューの表示をする関数 """
    print(DECO)
    print(TITLE)
    print(f'{DECO}\n')
    print(f'{MENU_HOW_TO}. 遊び方')
    print(f'{VOLUME_SETTING}. 音量の設定')
    print(f'{SHOW_LOG}. ログを表示')
    print(f'{MENU_3_DIGIT}. 3桁モード')
    print(f'{MENU_4_DIGIT}. 4桁モード')
    print(f'{MENU_EXIT}. 終了')
    print(f'\n{DECO}\n')


async def execute_menu(menu_no):
    """ メニュー番号の機能を実行する """
    if menu_no == MENU_HOW_TO:
        await main()
    elif menu_no == VOLUME_SETTING:
        volume()
    elif menu_no == SHOW_LOG:
        log_utils.print_log(file_utils.read_log())
        print('~' * 70)
    elif menu_no == MENU_3_DIGIT:
        quiz_mode3 = Quiz(digit=3)
        await quiz_mode3.main()
    elif menu_no == MENU_4_DIGIT:
        quiz_mode4 = Quiz(digit=4)
        await quiz_mode4.main()
    elif menu_no == MENU_EXIT:
        print('遊んでくれてありがとう!またね！')
        delete_volume_file()
        exit()
    else:
        print('[エラー!!] もう一度入力してください')


if __name__ == '__main__':
    set_file()
    asyncio.run(execute())
