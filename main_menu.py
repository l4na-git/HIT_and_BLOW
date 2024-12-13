# メニュー表示

from quiz import Quiz
from how_to import how_to
from keyboard import input_int

# 始めと最後の表示
print_first = """
======================================================================
                            Hit&Blow
======================================================================
"""
print_end = """
======================================================================
"""

# メニュー番号
menu_how_to = 1  # 遊び方
menu_3_digit = 2  # 3桁モード
menu_4_digit = 3  # 4桁モード
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
    print(print_first)
    print(f'{menu_how_to}. 遊び方')
    print(f'{menu_3_digit}. 3桁モード')
    print(f'{menu_4_digit}. 4桁モード')
    print(f'{menu_exit}. 終了')
    print(print_end)


def execute_menu(menu_no):
    if menu_no == menu_how_to:
        how_to()
    elif menu_no == menu_3_digit:
        quiz_mode3 = Quiz(digit=3)
        quiz_mode3.main()
    elif menu_no == menu_4_digit:
        quiz_mode4 = Quiz(digit=4)
        quiz_mode4.main()
    elif menu_no == menu_exit:
        print('遊んでくれてありがとう!')
        exit()
    else:
        print('エラー!! もう一度入力してください')


if __name__ == '__main__':
    execute()
