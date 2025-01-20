from flet import *


def registration_page(page):
    return Column(
        controls=[
            Text("Регистрация", size=26, color="blue"),
            TextField(label="Введите логин", width=300),
            TextField(label="Введите email", width=300),
            TextField(label="Введите пароль", password=True, width=300),
            ElevatedButton(
                "Зарегистрироваться", 
                on_click=lambda _: print("Регистрация завершена")
            ),
            ElevatedButton(
                "Назад", 
                on_click=lambda _: page.go("/")
            ),
        ],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )
