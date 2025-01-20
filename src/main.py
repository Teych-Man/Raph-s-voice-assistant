from flet import *
import flet as ft

from Authorization import interfase as auth_interfase
from Registration import interfase as reg_interfase


def main(page: ft.Page):
    page.title = "Авторизация"
    page.window.width = 525
    page.window.height = 725
    page.window.max_width = 525
    page.window.max_height = 725
    page.window.resizable = False
    page.padding = 0
    page.window.frameless = False

    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()

        if page.route == "/":
            page.views.append(
                View(
                    "/",
                    [
                        auth_interfase.get_auth_interface(page)
                    ],
                    padding=0,
                )
            )
        elif page.route == "/registration":
            page.views.append(
                View(
                    "/registration",
                    [
                        reg_interfase.registration_page(page)
                    ],
                    padding=0,
                )
            )
        elif page.route == "/reset_password":
            page.views.append(
                View(
                    "/reset_password",
                    [
                        Text("Восстановление пароля", size=20, color="blue"),
                        TextField(label="Введите ваш email", width=300),
                        ElevatedButton("Отправить", on_click=lambda _: print("Email отправлен")),
                        ElevatedButton("Назад", on_click=lambda _: page.go("/")),
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )

        page.update()

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


ft.app(target=main)
