import flet as ft

#Se importa la libreria random
import random 

def main(page: ft.Page):
    #Se crean las variables globales
    global numero_Secreto,entrada_numero,text_resultado,boton_adivinar
    
    page.title = "Adivina el numero"
    #se enera un numero aleatoria entre 1 y 100
    numero_Secreto = random.randint(1,100)
    
    titulo=ft.Text("Adivina el numero",size= 25,color="white")
    entrada_numero=ft.TextField(label="Tu Adivinanza",width=150)
    boton_adivinar=ft.ElevatedButton("Adivinar")
    text_resultado=ft.Text("",color="white")
    
    #Se crea el contenedorde la interfaz grafica
    
    contenedor_principal=ft.Container(
        content=ft.column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                text_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=300
                )   
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="blue",
        width=page.window.width,
        height=page.window.height,
        padding=20
        
        
    )
    page.add(contenedor_principal)
    
    
    
    
    ft.app(main)
