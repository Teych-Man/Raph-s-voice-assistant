from flet import *
import flet as ft

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.assets.Controls_Assets import image_layer_1, image_layer_2
from src.Authorization import logic
from src.Registration import interfase as reg_interfase

def main(page: ft.Page):
    page.title = "Авторизация"
    page.window.width = 525
    page.window.height = 725
    page.window.max_width = 525
    page.window.max_height = 725
    page.window.resizable = False
    page.padding = 0
    page.window.center()

    def validate(e):
        logic.validate(e, login_field, password_field, join_button)

    def check_account_user(e): 
        logic.check_account_user(e, join_button, login_field, password_field)

    def toggle_password(e):
        logic.toggle_password(e, password_field) 

    def on_hover_blackbox(e):
        logic.on_hover_blackbox(e, image_layer_1, image_layer_2)

    login_field = TextField(
        label="Введите логин",
        width=280,
        border_color="#a0f4fe",
        color="white",
        on_change=lambda e: validate(e),
    )

    password_field = TextField(
        label="Введите пароль",
        password=True,
        width=280,
        border_color="#a0f4fe",
        on_change=lambda e: validate(e),
        suffix=IconButton(
            icon=ft.Icons.REMOVE_RED_EYE_OUTLINED,
            on_click=lambda e: toggle_password(e),
        ),
    )

    join_button = OutlinedButton(
        text="Войти",
        width=280,
        style=ButtonStyle(
            color={},
            side={  # Стили для кнопки
                ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.GREY_500),
                ft.ControlState.HOVERED: ft.BorderSide(2, ft.Colors.GREY_500),
            }
        ),
        disabled=True,
        on_click=lambda e: check_account_user(e),
    )

    overlay_stack = Stack(
        controls=[
            image_layer_1,
            image_layer_2,
            Container(
                width=368,
                height=580,
                bgcolor="black",
                opacity=0.7,
                border_radius=20,
                on_hover=lambda e: on_hover_blackbox(e),
                content=Column(
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        Container(  # Для наглядности
                            padding=padding.only(top=40),  # Отступ сверху для заголовка
                            content=Text(
                                "Авторизация",
                                text_align=ft.TextAlign.CENTER,
                                size=26,
                                color="#a0f4fe"
                            ),
                        ),
                        Container(
                            padding=padding.only(top=80),  # Отступ до логина
                            content=login_field,
                        ),
                        Container(
                            padding=padding.only(top=20),  # Отступ до пароля
                            content=password_field,
                        ),
                        Container(
                            padding=padding.only(top=20),  # Отступ до кнопки войти
                            content=join_button,
                        ),
                        Container(
                            padding=padding.only(top=10),  # Отступ до кнопки "Забыли пароль"
                            content=TextButton(
                                content=Text(
                                    "Забыли пароль?",
                                    size=12,
                                    color="#a0f4fe",
                                ),
                                on_click=lambda _: print("Забыли пароль"),
                            ),
                        ),
                        Container(
                            expand=True  # Пустое пространство, чтобы кнопка регистрации оказалась внизу
                        ),
                        Container(
                            padding=padding.only(bottom=20),  # Отступ снизу для кнопки регистрации
                            content=TextButton(
                                content=Text(
                                    "Нет аккаунта? Зарегистрироваться",
                                    size=12,
                                    color="#a0f4fe",
                                ),
                                on_click=lambda _: page.add(reg_interfase.registration_page(page)),  # Переход на страницу регистрации
                            ),
                        ),
                    ],
                ),
            ),
        ],
        width=525,
        height=725,
        alignment=ft.alignment.center,
    )

    page.add(overlay_stack)
