from flet import *
import flet as ft

from src.Authorization import interfase as auth_interfase

def registration_page(page: ft.Page):
    page.title = "Регистрация"
    page.window.width = 525
    page.window.height = 725
    page.window.max_width = 525
    page.window.max_height = 725
    page.window.resizable = False
    page.padding = 0
    page.window.center()

    # Элементы интерфейса страницы регистрации
    username_field = TextField(
        label="Введите имя пользователя",
        width=280,
        border_color="#a0f4fe",
        color="white",
    )

    email_field = TextField(
        label="Введите email",
        width=280,
        border_color="#a0f4fe",
        color="white",
    )

    password_field = TextField(
        label="Введите пароль",
        password=True,
        width=280,
        border_color="#a0f4fe",
    )

    register_button = ElevatedButton(
        text="Зарегистрироваться",
        width=280,
        on_click=lambda e: print("Регистрация прошла успешно!"),  # Логика регистрации
    )

    back_button = TextButton(
        text="Назад к авторизации",
        on_click=lambda e: page.add(auth_interfase.main(page)),  # Переход обратно на страницу авторизации
    )

    page.add(
        Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                Text("Регистрация", size=26, color="#a0f4fe"),
                username_field,
                email_field,
                password_field,
                register_button,
                back_button,
            ],
        )
    )
