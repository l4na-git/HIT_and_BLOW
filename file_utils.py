# ファイルの操作に関するもの
import os


# ファイルがあるかどうかを確認
def search_file(filename: str) -> bool:
    if not os.path.exists(filename):
        print(f"ファイルが見つかりません: {filename}")
        return False
