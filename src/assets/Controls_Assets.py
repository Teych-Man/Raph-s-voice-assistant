from flet import Image, ImageFit
import flet as ft

image_layer_1 = Image(
    "src/assets/images/Layer_1.png",
    width=525,
    height=725,
    fit=ImageFit.COVER,
    animate_scale=ft.Animation(600, "ease"),
)

image_layer_2 = Image(
    "src/assets/images/Layer_2.png",
    width=525,
    height=725,
    fit=ImageFit.COVER,
    animate_scale=ft.Animation(600, "ease"),
)