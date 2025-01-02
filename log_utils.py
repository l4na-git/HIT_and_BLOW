import file_utils


INDENT_SPACE = " " * 2
LINE_LENGTH = 30

def print_log(data):
    for i in data:
        print(f"日時: {i["datetime"]}")
        print(f"答え: {i["answer"]}")
        print(f"クリア: {"yes" if i["clear"] else "no"}")
        print(f"入力回数: {len(i["log"])}")
        print("-" * 20)
        for j in i["log"]:
            print(f"{INDENT_SPACE}入力: {j["input"]}, ヒット: {j["hit"]}, ブロー: {j["blow"]}")
            if j != i["log"][-1]:
                print(f"{INDENT_SPACE}" + "~" * LINE_LENGTH)
        print("=" * LINE_LENGTH)
