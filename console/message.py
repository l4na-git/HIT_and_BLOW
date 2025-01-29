"""
ゲームの結果に応じてメッセージを表示する
"""
import asyncio
import os
import sys
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils.file_utils import read_file
from console.sound import play

DELAY = 0.23  # フレーム間の遅延時間


async def show_message(filename: str) -> None:
    """一定の間隔でメッセージを表示する

    Args:
        filename (str): メッセージが記載されているファイル名
    """
    file_path = Path('config/' + filename).resolve()
    text_list = read_file(file_path)
    for line in text_list:
        print(line)
        await asyncio.sleep(DELAY)


async def show_message_with_sound(text_file: str, sound_file: str) -> None:
    """メッセージと音源を同時に再生する

    Args:
        text_file (str): メッセージが記載されているファイル名
        sound_file (str): 音源のファイル名
    """
    try:
        async with asyncio.TaskGroup() as tk:
            tk.create_task(show_message(text_file))
            tk.create_task(play(sound_file))
    except* ValueError as e:
        for _e in e.exceptions:
            print(_e)

if __name__ == "__main__":
    asyncio.run(show_message_with_sound('correct_message.txt', "happy.mp3"))
