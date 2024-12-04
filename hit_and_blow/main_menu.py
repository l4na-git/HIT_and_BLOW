# メニュー表示

from quiz import Quiz
from keybord import input_int


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
    print('1. 3桁モード')
    print('2. 4桁モード')
    print('9. 終了')


def execute_menu(menu_no):
    if menu_no == 1:
        print('*** 3桁モード ***')
        quiz_mode3 = Quiz(digit=3, max_num=999)
        ans = quiz_mode3.ans_str
        print(f'テスト用: 正解は{ans}')
        quiz_mode3.quiz()
    elif menu_no == 2:
        print('*** 4桁モード ***')
        quiz_mode4 = Quiz(digit=4, max_num=9999)
        ans = quiz_mode4.ans_str
        print(f'テスト用: 正解は{ans}')
        quiz_mode4.quiz()
    elif menu_no == 9:
        exit()


if __name__ == '__main__':
    execute()
