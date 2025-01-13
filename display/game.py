# 画面

import flet as ft
import random
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils import file_utils
from datetime import datetime
from pathlib import Path


class CalcButton(ft.ElevatedButton):
    def __init__(self, text, btn_click, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = btn_click
        self.data = text


class QuizApp(ft.Container):
    def __init__(self):
        super().__init__()
        self.reset()
        self.clear = False
        self.log = []
        self.create_ans()
        self.count = 1

        self.result = ft.Text(value="0", size=20)
        self.content = ft.Column(
            controls=[

                ft.Row(
                        [
                            ft.Text(
                                "Hit and Blow!",
                                color="blue",
                                size=40,
                                weight="bold",
                                opacity=0.5,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ft.Row(
                        [
                            ft.Text(
                                "ー 3桁モード ー",
                                color="blue",
                                size=30,
                                opacity=0.5,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER, height=70
                    ),

                ft.Row(controls=[self.result], alignment="end"),
                ft.Row(
                    controls=[
                        CalcButton(text="0", btn_click=self.btn_click),
                        CalcButton(text="1", btn_click=self.btn_click),
                        CalcButton(text="2", btn_click=self.btn_click),
                        CalcButton(text="3", btn_click=self.btn_click),
                        CalcButton(text="4", btn_click=self.btn_click),
                    ], alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        CalcButton(text="5", btn_click=self.btn_click),
                        CalcButton(text="6", btn_click=self.btn_click),
                        CalcButton(text="7", btn_click=self.btn_click),
                        CalcButton(text="8", btn_click=self.btn_click),
                        CalcButton(text="9", btn_click=self.btn_click),
                    ], alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        CalcButton(text="Clear", btn_click=self.btn_click),
                        CalcButton(text="Go!", btn_click=self.btn_click),
                    ], alignment=ft.MainAxisAlignment.CENTER,
                ),
            ]
        )

    def btn_click(self, e):
        data = e.control.data
        print(f"Button clicked with data = {data}")
        if self.result.value == "Error" or data == "Clear":
            self.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand is True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        elif data in ("Go!"):
            if self.count > 10:
                self.result.value = "Game Over"
                self.update()
                return

            self.hit = self.hit_count()
            self.blow = self.blow_count()
            self.append_log()
            if self.hit == 3:
                self.clear = True
                self.write_log()
            else:
                self.write_log()
            self.result.value = "0"
            self.reset()
            self.count += 1
        self.update()

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True

    def create_ans(self) -> str:
        """ 正解の生成をするメソッド """
        self.ans_str = ""
        while True:
            ans_num = random.randint(0, 9)
            # 数字が重複していないか
            if str(ans_num) in self.ans_str:
                continue
            self.ans_str += str(ans_num)
            # 指定した桁数分生成したか
            if len(self.ans_str) == 3:
                break
        print(self.ans_str)  # テスト用
        return self.ans_str

    def hit_count(self) -> int:
        """ hit(数字と桁位置の両方が同じ)の回数をカウントするメソッド """
        self.hit = 0
        for answer, user in zip(self.ans_str, self.result.value):
            if answer == user:
                self.hit += 1  # hitの回数をカウントアップ
        return self.hit

    def blow_count(self) -> int:
        """ blow(数字のみ同じ)の回数をカウントするメソッド """
        self.blow = 0
        for digit in self.result.value:
            if digit in self.ans_str:
                self.blow += 1  # blowの回数をカウントアップ
        self.blow -= self.hit  # hitの回数分を引く
        return self.blow

    def append_log(self) -> None:
        """ ファイルに記録(hitとblowの回数)するメソッド """
        log_data = {"input": self.result.value, "hit": self.hit, "blow": self.blow}
        self.log.append(log_data)

    def write_log(self) -> None:
        """ ファイルに記録をするメソッド """
        name = 'guest'
        filename = f'{name}.json'
        create_path = Path('log_data/') / filename
        log = {}
        log["datetime"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log["answer"] = int(self.ans_str)
        log["clear"] = self.clear
        log["log"] = self.log
        file_utils.add_log(create_path, log)  # 途中


def main(page: ft.Page):
    page.title = "Hit and Blow!"
    # アプリのインスタンス作成
    quiz = QuizApp()

    # コントローラー作成
    page.add(quiz)


if __name__ == "__main__":
    ft.app(target=main)
