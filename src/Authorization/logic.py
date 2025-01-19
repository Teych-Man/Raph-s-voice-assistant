from flet import *
import flet as ft

import sqlite3
import time

def validate(e, login_field, password_field, join_button): #
    if login_field.value.strip() == "" or password_field.value.strip() == "":
        join_button.text = "Войти"
        join_button.disabled = True
        join_button.style=ButtonStyle(
        color={
            "": ft.Colors.GREY_500,
        },
        side={
            ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.GREY_500),
            ft.ControlState.HOVERED: ft.BorderSide(2, ft.Colors.GREY_500),
            })
    else:
        join_button.text = "Войти"
        join_button.disabled = False
        join_button.style=ButtonStyle(
        color={
            "": "#a0f4fe",
        },
        side={
            ft.ControlState.DEFAULT: ft.BorderSide(1, "#a0f4fe"),
            ft.ControlState.HOVERED: ft.BorderSide(2, "#a0f4fe"),
            })

    join_button.update()

def check_account_user(e, join_button, login_field, password_field): # Проверка пользователя в базе данных
    conn = sqlite3.connect('src/Databases/users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user WHERE login = ? AND password = ?", (login_field.value, password_field.value))
    user = cursor.fetchone()
    conn.close()

    if user:
        join_button.text = "Выполняется вход..."
        join_button.style=ButtonStyle(
                        color={
                            "": ft.Colors.GREEN_900,
                        },
                        side={
                            ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.GREEN_900)
                        })
        
        login_field.value, password_field.value = "", ""
        join_button.disabled = True

        join_button.update() 
        login_field.update()
        password_field.update()
        time.sleep(1)
            
    else:
        join_button.text = "Неверный логин или пароль"
        join_button.style=ButtonStyle(
                        color={
                            "": ft.Colors.RED_900,
                        },
                        side={
                            ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.RED_900)
                        })
        
        login_field.value, password_field.value = "", ""
        join_button.disabled = True
    
        join_button.update() 
        login_field.update()
        password_field.update()
        
        time.sleep(2)
        
        join_button.text = "Войти"
        join_button.style=ButtonStyle(
                        color={
                            "": ft.Colors.GREY_500,
                        },
                        side={
                            ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.GREY_500)
                        })
        join_button.update()

def toggle_password(e, password_field):
    password_field.password = not password_field.password  
    password_field.update() 

def on_hover_blackbox(e, image_layer_1, image_layer_2):
    if e.data == "true":
        image_layer_1.scale = 1.1
        image_layer_2.scale = 1.1
    else:
        image_layer_1.scale = 1.0
        image_layer_2.scale = 1.0

    image_layer_1.update()
    image_layer_2.update()