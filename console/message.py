# 結果に応じてメッセージを表示する
import asyncio
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.file_utils import read_all_file
from console.sound import play

DELAY = 0.23  # フレーム間の遅延時間


async def print_text(file_name: str) -> None:
    """ 一定の間隔でメッセージを表示する関数 """
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                r'..\config', file_name))
    text_list = read_all_file(file_path)
    for num in range(len(text_list)):
        print(text_list[num])
        await asyncio.sleep(DELAY)
    await asyncio.sleep(1)


async def print_with_sound(text_file: str, sound_file: str) -> None:
    """ メッセージと音声を同時に再生する関数 """
    try:
        async with asyncio.TaskGroup() as tk:
            tk.create_task(print_text(text_file))
            tk.create_task(play(sound_file))
    except* ValueError as e:
        for _e in e.exceptions:
            print(_e)

if __name__ == "__main__":
    asyncio.run(print_with_sound('correct_message.txt', "happy.mp3"))
