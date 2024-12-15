# メニュー表示

from quiz import Quiz
from how_to import main
from sound import create_volume_file, delete_volume_file, volume
from keyboard import input_int
import asyncio

# 装飾とタイトル
DECO = '=' * 70
TITLE = '                            Hit&Blow'

# メニュー番号
menu_how_to = 1  # 遊び方
volume_setting = 2  # 音量の設定
show_log = 3  # ログの表示
menu_3_digit = 4  # 3桁モード
menu_4_digit = 5  # 4桁モード
menu_exit = 9  # 終了


async def execute():
    while True:
        # メニューを表示
        print_menu()

        # メニュー番号の入力
        num = input_int('メニュー番号を入力してください: ')

        # メニュー番号の機能を実行
        await execute_menu(num)


def print_menu():
    print(DECO)
    print(TITLE)
    print(f'{DECO}\n')
    print(f'{menu_how_to}. 遊び方')
    print(f'{volume_setting}. 音量の設定')
    print(f'{show_log}. ログを表示')
    print(f'{menu_3_digit}. 3桁モード')
    print(f'{menu_4_digit}. 4桁モード')
    print(f'{menu_exit}. 終了')
    print(f'\n{DECO}\n')


async def execute_menu(menu_no):
    if menu_no == menu_how_to:
        main()
    elif menu_no == volume_setting:
        volume()
    elif menu_no == show_log:
        with open(r'log_data\guest.txt', 'r') as f:
            print(f.read())
        print('~' * 70)
    elif menu_no == menu_3_digit:
        quiz_mode3 = Quiz(digit=3)
        # quiz_mode3.main()
        await quiz_mode3.main()
    elif menu_no == menu_4_digit:
        quiz_mode4 = Quiz(digit=4)
        # quiz_mode4.main()
        await quiz_mode4.main()
    elif menu_no == menu_exit:
        print('遊んでくれてありがとう!またね！')
        delete_volume_file()
        exit()
    else:
        print('[エラー!!] もう一度入力してください')


if __name__ == '__main__':
    create_volume_file()
    asyncio.run(execute())
