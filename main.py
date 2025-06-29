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
from personaje import *


pygame.init()

# ----------------- CONFIGURACIÓN DE PANTALLA -----------------

ANCHO = 800
ALTO = 600

titulo = 'Ahorcado by Rocket League'

pantalla = pygame.display.set_mode((ANCHO, ALTO))

pygame.display.set_caption(titulo)

icono = pygame.image.load("logo.png")

pygame.display.set_icon(icono)

clock = pygame.time.Clock()

# ----------------- COLORES  se pueden modificar por los que elija el equipo-----------------
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


# ----------------- FUENTE -----------------
FUENTE = pygame.font.SysFont('freesansbold.ttf', 20)

rect_rocket_league = pygame.Rect((ANCHO / 2) + 50, 100, 300, 200)

personaje_x = rect_rocket_league.centerx - 75
personaje_y = rect_rocket_league.bottom - 125

personaje = crear_personaje(personaje_x ,personaje_y ,125 ,125 ,"rocketleague.png")



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

    keys = {
    pygame.K_a: 'a', pygame.K_b: 'b', pygame.K_c: 'c', pygame.K_d: 'd',
    pygame.K_e: 'e', pygame.K_f: 'f', pygame.K_g: 'g', pygame.K_h: 'h',
    pygame.K_i: 'i', pygame.K_j: 'j', pygame.K_k: 'k', pygame.K_l: 'l',
    pygame.K_m: 'm', pygame.K_n: 'n', pygame.K_o: 'o', pygame.K_p: 'p',
    pygame.K_q: 'q', pygame.K_r: 'r', pygame.K_s: 's', pygame.K_t: 't',
    pygame.K_u: 'u', pygame.K_v: 'v', pygame.K_w: 'w', pygame.K_x: 'x',
    pygame.K_y: 'y', pygame.K_z: 'z',
}
    lista_palabras = cargar_palabras()  # Ejecuta la función para obtener las palabras

    eventos_juego = { 
    'palabra_random' : elegir_palabra(lista_palabras),
    'letras_adivinadas' : [],
    'letras_correctas' : [],
    'errores' : 0,
    "juego_terminado":False,
    }

    for x in eventos_juego['palabra_random']:
        eventos_juego['letras_correctas'].append("")
 
    while True:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key in keys:
                    letra = keys[event.key].upper()
                    if letra not in eventos_juego['letras_adivinadas']:  
                        resultado = verificar_letra(letra, eventos_juego['palabra_random'], eventos_juego['letras_adivinadas'])
                        if not resultado and eventos_juego['errores'] <= 6:   
                            eventos_juego['errores'] += 1
                            dibujar_cuerpo(eventos_juego['errores'])
                        else:
                            for i, x in enumerate(eventos_juego['palabra_random']):
                                if letra == x:
                                    eventos_juego['letras_correctas'][i] = eventos_juego['palabra_random'][i]
                    

                                    ## ["", "", ""], [S, O, ""]

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            update(personaje, -10, rect_rocket_league)
        if keys_pressed[pygame.K_RIGHT]:
            update(personaje, 10, rect_rocket_league)  

        dibujar_juego(eventos_juego['palabra_random'], eventos_juego['letras_adivinadas'], eventos_juego['errores'], eventos_juego['letras_correctas'])    
        

        pantalla.blit(personaje['surface'], personaje['rect_pos'])

        if eventos_juego['errores'] >= 6 or "" not in eventos_juego['letras_correctas']:
            eventos_juego['juego_terminado'] = True

        if eventos_juego['juego_terminado']:

            pantalla.fill(AZUL)

            if eventos_juego['errores'] >= 6 or "":
                
                mostrar_texto(f"¡Perdiste, la palabra era {eventos_juego['palabra_random']}!", 125, 300, BLANCO, 50)
                         
            if "" not in eventos_juego['letras_correctas']:

                mostrar_texto(f"¡Ganaste!", 325, 300, BLANCO, 50)
     
            pygame.display.flip()
            time.sleep(3)
            pygame.quit()
            sys.exit()            

        pygame.display.update()
        

        

# No ejecutar el juego automáticamente: solo se invoca desde consola o importación
# Descomentar la línea siguiente para probar el juego terminado:
jugar()
