from flet import *
import flet as ft

from Authorization import interfase as auth_interfase
from Registration import interfase as reg_interfase 

def main(page: ft.Page):
    # Устанавливаем начальную страницу (страница авторизации)
    page.add(auth_interfase.main(page))

ft.app(target=main)
