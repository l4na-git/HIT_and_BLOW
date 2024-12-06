# メニュー表示

from quiz import Quiz
from how_to import how_to
from keybord import input_int

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
    print('=== Hit&Blow ===')
    print(f'{menu_how_to}. 遊び方')
    print(f'{menu_3_digit}. 3桁モード')
    print(f'{menu_4_digit}. 4桁モード')
    print(f'{menu_exit}. 終了')


def execute_menu(menu_no):
    if menu_no == menu_how_to:
        how_to()
    elif menu_no == menu_3_digit:
        print('*** 3桁モード ***')
        quiz_mode3 = Quiz(digit=3, max_num=999)
        ans = quiz_mode3.ans_str
        print(f'テスト用: 正解は{ans}')
        quiz_mode3.quiz()
    elif menu_no == menu_4_digit:
        print('*** 4桁モード ***')
        quiz_mode4 = Quiz(digit=4, max_num=9999)
        ans = quiz_mode4.ans_str
        print(f'テスト用: 正解は{ans}')
        quiz_mode4.quiz()
    elif menu_no == menu_exit:
        print('遊んでくれてありがとう!')
        exit()
    else:
        print('エラー!! もう一度入力してください')


if __name__ == '__main__':
    execute()
