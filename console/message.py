# 表示するメッセージ
import asyncio
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.file_utils import read_all_file


DELAY = 0.23  # フレーム間の遅延時間


async def animation(art_lines):
    """ 一定の間隔でメッセージを表示する関数 """
    for i in range(len(art_lines)):
        print(art_lines[i])
        await asyncio.sleep(DELAY)
    await asyncio.sleep(1)


async def animation_correct():
    """ 正解のときに呼び出す関数 """
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                r'..\config\correct_message.txt'))
    art_list = read_all_file(file_path)
    await animation(art_list)


async def animation_wrong():
    """ 正解できなかったときに呼び出す関数 """
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                r'..\config\wrong_message.txt'))
    art_list = read_all_file(file_path)
    await animation(art_list)

if __name__ == "__main__":
    # asyncio.run(animation_correct())
    asyncio.run(animation_wrong())
