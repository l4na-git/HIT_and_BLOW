"""
このファイルはHit & Blowのゲームを起動します。
Pygameがインストールされていることを確認してから実行してください。
"""
import sys
import os
import asyncio
# import flet as ft
# from display.game import main as gui_main
from console.main_menu import execute as cui_execute
from utils.file_utils import read_file, change_username, change_volume


def get_option():
    """ オプションを取得する関数 """
    DIR = os.path.dirname(__file__)
    SEARCH_FILE_PATH = DIR + r'\config\help_message.txt'
    options = set()  # 取得したオプションを格納
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] in ["-h", "--help"]:
            message_list = read_file(SEARCH_FILE_PATH)
            print()
            for message in message_list:
                print(message)
            print()
            sys.exit(0)  # 正常終了する
        elif sys.argv[i] in ["-c", "--cui"]:
            options.add("cui")
            i += 1
            return options
        elif sys.argv[i] in ["-g", "--gui"]:
            options.add("gui")
            i += 1
            return options
        elif sys.argv[i].startswith("--"):
            print("\033[91mError: Invalid Option\
                \n無効なオプションです。--help を使用してください。\033[0m")
            sys.exit(1)  # 異常終了
        elif sys.argv[i].startswith("-"):
            print(f"\033[91mError: Invalid Option -{sys.argv[i]}\
                \n無効なオプションです。--help を使用してください。\033[0m")
            sys.exit(1)  # 異常終了
            i += 1
        else:  # ハイフンが先頭に無い場合
            print("\033[91mError: Invalid Option\
                \n無効なオプションです。--help を使用してください。\033[0m")
            sys.exit(1)  # 異常終了
            i += 1

    if not options:  # オプションが指定されていないときはCUIで実行
        options.add("cui")
        return options


def execute(options):
    """ 取得したオプションをもとに実行する """
    if "cui" in options or "c" in options:  # CUIで実行
        print("Launching Hit & Blow in CUI mode...")
        change_volume(file_path, 0.3)
        asyncio.run(cui_execute())
    if "gui" in options or "g" in options:  # GUIで実行
        print("Launching Hit & Blow in GUI mode...")
        ft.app(target=gui_main)


if __name__ == '__main__':
    options = get_option()
    file_path = os.path.join(os.path.dirname(__file__), 'config', 'setting.json')
    change_username(file_path, 'guest')
    execute(options)
