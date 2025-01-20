from flet import *
import flet as ft

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.assets.Controls_Assets import image_layer_1, image_layer_2
from src.Authorization import logic

def get_auth_interface(page):
    login_field = TextField(
        label="Введите логин",
        width=280,
        border_color="#a0f4fe",
        color="white",
        on_change=lambda e: logic.validate(e, login_field, password_field, join_button),
    )

    password_field = TextField(
        label="Введите пароль",
        password=True,
        width=280,
        border_color="#a0f4fe",
        on_change=lambda e: logic.validate(e, login_field, password_field, join_button),
        suffix=IconButton(
            icon=ft.Icons.REMOVE_RED_EYE_OUTLINED,
            on_click=lambda e: logic.toggle_password(e, password_field),
        ),
    )

    join_button = OutlinedButton(
        text="Войти",
        width=280,
        style=ButtonStyle(
            color={},
            side={
                ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.GREY_500),
                ft.ControlState.HOVERED: ft.BorderSide(2, ft.Colors.GREY_500),
            }
        ),
        disabled=True,
        on_click=lambda e: logic.check_account_user(e, join_button, login_field, password_field),
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
                content=Column(
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        Container(
                            padding=padding.only(top=40),
                            content=Text(
                                "Авторизация",
                                text_align=ft.TextAlign.CENTER,
                                size=26,
                                color="#a0f4fe"
                            ),
                        ),
                        Container(
                            padding=padding.only(top=80),
                            content=login_field,
                        ),
                        Container(
                            padding=padding.only(top=20),
                            content=password_field,
                        ),
                        Container(
                            padding=padding.only(top=20),
                            content=join_button,
                        ),
                        Container(
                            padding=padding.only(top=10),
                            content=TextButton(
                                content=Text(
                                    "Забыли пароль?",
                                    size=12,
                                    color="#a0f4fe",
                                ),
                                on_click=lambda _: page.go("/reset_password"),
                            ),
                        ),
                        Container(
                            expand=True
                        ),
                        Container(
                            padding=padding.only(bottom=20),
                            content=TextButton(
                                content=Text(
                                    "Нет аккаунта? Зарегистрироваться",
                                    size=12,
                                    color="#a0f4fe",
                                ),
                                on_click=lambda _: page.go("/registration"),
                            ),
                        ),
                    ],
                ),
            ),
        ],
        width=525,
        height=725,
        expand=True,
        alignment=ft.alignment.center,
    )

    return overlay_stack
