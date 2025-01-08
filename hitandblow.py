# オプション実装

import sys
from display.main import DisplayMain
from sound import set_file
from main_menu import execute
import asyncio


def usage():
    print("""

Usage: hitandblow [options]

Description:
    A "Hit & Blow" game application. You can play the game using the CUI (Command Line Interface) or GUI (Graphical User Interface).

Features:
    - Test your logic and deduction skills in this classic code-breaking game.
    - Choose your preferred interface: CUI or GUI.

Arguments:
    No positional arguments are required.

Options:
    -h|--help           Display this help message and exit.
    -c|--cui            Launch the game in Command Line Interface (CUI) mode.
    -g|--gui            Launch the game in Graphical User Interface (GUI) mode.

Examples:
    Launch the game in CUI mode:
        hitandblow --cui

    Launch the game in GUI mode:
        hitandblow --gui

""")


options = set()  # 使用されたオプションを格納するための集合
i = 1  # 始まりは0ではなく、1とすること
while i < len(sys.argv):
    if sys.argv[i] in ["-h", "--help"]:
        # 引数が「-h」もしくは「--help」だったら「usage()」を実行して正常終了する
        usage()
        sys.exit(0)  # 正常終了する
    elif sys.argv[i] in ["-c", "--cui"]:
        options.add("cui")
        i += 1  # 処理を実行した後は、次の引数を処理するためにiに1を足す
    elif sys.argv[i] in ["-g", "--gui"]:
        options.add("gui")
        i += 1
    elif sys.argv[i].startswith("--"):
        print("\033[91mError: Invalid Option\n無効なオプションです。--help を使用してください。\033[0m")
        sys.exit(1)  # 異常終了する
    elif sys.argv[i].startswith("-"):
        # オプションが複数組み合わさっている場合も考慮して、一文字ずつ分割
        for char in sys.argv[i][1:]:
            if char in "cg":
                options.add(char)
            else:
                print(f"\033[91mError: Invalid Option -{char}\n無効なオプションです。--help を使用してください。\033[0m")
                sys.exit(1)  # 異常終了する
        i += 1
    else:
        i += 1  # ハイフンが先頭に無い引数を無視する

if "cui" in options or "c" in options:
    print("Launching Hit & Blow in CUI mode...")
    set_file()
    asyncio.run(execute())
if "gui" in options or "g" in options:
    print("Launching Hit & Blow in GUI mode...")
    display = DisplayMain('root_back.png')
    display.main()
