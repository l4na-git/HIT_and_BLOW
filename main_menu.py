# メニュー表示

from quiz import Quiz
from how_to import how_to
from sound import create_volume_file, delete_volume_file, volume
from keyboard import input_int

# 装飾とタイトル
DECO = '=' * 70
TITLE = '                            Hit&Blow'

# メニュー番号
menu_how_to = 1  # 遊び方
volume_setting = 2  # 音量の設定
menu_3_digit = 3  # 3桁モード
menu_4_digit = 4  # 4桁モード
menu_exit = 9  # 終了


def execute():
    while True:
        # メニューを表示
        print_menu()

        # メニュー番号の入力
        num = input_int('メニュー番号を入力してください: ')

        # メニュー番号の機能を実行
        execute_menu(num)


def print_menu():
    print(DECO)
    print(TITLE)
    print(f'{DECO}\n')
    print(f'{menu_how_to}. 遊び方')
    print(f'{volume_setting}. 音量の設定')
    print(f'{menu_3_digit}. 3桁モード')
    print(f'{menu_4_digit}. 4桁モード')
    print(f'{menu_exit}. 終了')
    print(f'\n{DECO}\n')


def execute_menu(menu_no):
    if menu_no == menu_how_to:
        how_to()
    elif menu_no == volume_setting:
        volume()
    elif menu_no == menu_3_digit:
        quiz_mode3 = Quiz(digit=3)
        quiz_mode3.main()
    elif menu_no == menu_4_digit:
        quiz_mode4 = Quiz(digit=4)
        quiz_mode4.main()
    elif menu_no == menu_exit:
        print('遊んでくれてありがとう!')
        delete_volume_file()
        exit()
    else:
        print('エラー!! もう一度入力してください')


if __name__ == '__main__':
    create_volume_file()
    execute()
