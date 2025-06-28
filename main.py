# === PROYECTO FINAL - JUEGO DEL AHORCADO EN PYGAME ===
# Instrucciones:
# - Usar funciones, listas, diccionarios y archivos.
# - No usar clases ni programación orientada a objetos.
# - El juego debe leer palabras desde un archivo de texto externo (palabras.txt).
# - Mostrar la palabra oculta en pantalla, los intentos y las letras ingresadas.
# - Dibujar el muñeco del ahorcado a medida que se cometen errores (cabeza, cuerpo, brazos, piernas).
# - Mostrar mensaje final al ganar o perder.
# - Organizar el código con funciones bien nombradas.
# - El código debe estar comentado línea por línea.
# - Solo las partes del cuerpo deben contar como errores, no el soporte del ahorcado.

import pygame
from funciones import *
import sys, time


pygame.init()

# ----------------- CONFIGURACIÓN DE PANTALLA -----------------

titulo = 'Ahorcado by Rocket League'
descripcion = 'Adiviná la palabra. Tenés 6 intentos para completar la palabra. Elige una letra, cada letra errónea será un error.'

ANCHO = 800
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
#completar con nombre del equipo
pygame.display.set_caption("Juego del Ahorcado")
clock = pygame.time.Clock()

# ----------------- COLORES  se pueden modificar por los que elija el equipo-----------------
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (37, 36, 64)

# ----------------- FUENTE -----------------
FUENTE = pygame.font.SysFont(None, 48)

# ----------------- SONIDO -----------------
pygame.mixer.init()  # Inicializa el motor de sonido
sonido_error = pygame.mixer.Sound("error.wav")  # Asegurate de tener este archivo

# ----------------- BUCLE PRINCIPAL -----------------
def jugar():
    # 1. Cargar palabras desde archivo y elegir una al azar
    # 2. Inicializar estructuras necesarias: letras_adivinadas, errores, reloj, banderas
    # 3. Crear un bucle while que termine al cerrar el juego o al ganar/perder
    # 4. Dentro del bucle:
    #     - Capturar eventos (teclas)
    #     - Verificar letras
    #     - Incrementar errores si corresponde
    #     - Dibujar estado del juego en pantalla
    #     - Verificar condiciones de fin (victoria o derrota)
    #     - Actualizar pantalla
    #     - Controlar FPS

    # Instrucción: este bloque debe ser completado por el estudiante según las consignas
    

    while True:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pantalla.fill(AZUL)

        mostrar_texto(descripcion, 15, 15, BLANCO, 20)

        dibujar_estructura()
        
        pygame.display.update()
        

        

# No ejecutar el juego automáticamente: solo se invoca desde consola o importación
# Descomentar la línea siguiente para probar el juego terminado:
jugar()
