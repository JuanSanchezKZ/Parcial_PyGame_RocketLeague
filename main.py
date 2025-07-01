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

import pygame # improtamos pygame
from funciones import * # improtamos todo de funciones.py (todas las funciones y variables)
import sys, time # importamos sys para el cierre del juego y time para esperar 3 segundos antes de cerrar el juego
from personaje import * # importamos todo de personaje.py (todas las funciones y variables)


pygame.init() ## Inicializamos pygame

# ----------------- CONFIGURACIÓN DE PANTALLA -----------------

ANCHO = 800 # Definimos ancho de pantalla
ALTO = 600 # Definimos alto de pantalla

# --------------------- SONIDOS ------------------------ #

pygame.mixer.init()  # Inicializa el motor de sonido
ganar_sonido = pygame.mixer.Sound("ganar_sonido.wav")  # Cargamos sonido de victoria
pygame.mixer.Sound.set_volume(ganar_sonido, 0.2) # Bajamos un poco el volumen
perder_sonido = pygame.mixer.Sound("perder_sonido.mp3")  # Cargamos sonido de victoria
pygame.mixer.Sound.set_volume(perder_sonido, 0.2) # Bajamos un poco el volumen

titulo = 'Ahorcado by Rocket League' # Definimos el título del juego

pantalla = pygame.display.set_mode((ANCHO, ALTO)) # Creamos la variable pantalla con set_mode con su ancho y alto

pygame.display.set_caption(titulo) # Seteamos el titulo del juego con set_caption 

icono = pygame.image.load("logo.png") # Cargamos la imagen de nuestro logo

pygame.display.set_icon(icono) # Setaeamos nuestro logo con set_icon

clock = pygame.time.Clock() # Definimos la variable clock para luego controlar los fps

# ----------------- COLORES  se pueden modificar por los que elija el equipo-----------------

BLANCO = (255, 255, 255) # Color blanco RGB
NEGRO = (0, 0, 0) # Color negro RGB

# ---------------- PERSONAJE PRINCIPAL (AUTO ROCKET LEAGUE) --------------- 

ancho_auto = 125 # Ancho del auto
altura_auto = 125 # Alto del auto

rect_rocket_league = pygame.Rect((ANCHO / 2) + 200, 300, 100, 50) ## Rectangulo para colisionar
# (ANCHO / 2) + 50 = La mitad del ancho de la pantalla mas un poco a la derecha (eje X)
# 100 = eje Y
# 300 ANCHO rectangulo
# 200 ALTO rectangulo

personaje_x = 250 # posicion x del personaje
personaje_y = 200 # posicion y del personaje

personaje = crear_personaje(personaje_x ,personaje_y ,ancho_auto ,altura_auto ,"rocketleague.png")



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

    keys = { ## guardamos todas los eventos de letras de pygame como clave con su respectiva letra como valor
    pygame.K_a: 'a', pygame.K_b: 'b', pygame.K_c: 'c', pygame.K_d: 'd',
    pygame.K_e: 'e', pygame.K_f: 'f', pygame.K_g: 'g', pygame.K_h: 'h',
    pygame.K_i: 'i', pygame.K_j: 'j', pygame.K_k: 'k', pygame.K_l: 'l',
    pygame.K_m: 'm', pygame.K_n: 'n', pygame.K_o: 'o', pygame.K_p: 'p',
    pygame.K_q: 'q', pygame.K_r: 'r', pygame.K_s: 's', pygame.K_t: 't',
    pygame.K_u: 'u', pygame.K_v: 'v', pygame.K_w: 'w', pygame.K_x: 'x',
    pygame.K_y: 'y', pygame.K_z: 'z',
}
    
    lista_palabras = cargar_palabras()  # Ejecuta la función para obtener las palabras
 
    eventos_juego = {  ## Diccionario con nuestros eventos de juego
    'palabra_random' : elegir_palabra(lista_palabras), ## Llamado a la función para guardar la palabra a adivinar
    'letras_adivinadas' : [], ## lista con letras incorrectas
    'letras_correctas' : [], ## lista con letras correctas
    'errores' : 0, ## Cantidad de errores
    "juego_terminado":False, ## boolean que define si terminó el juego
    }

    for x in eventos_juego['palabra_random']: ## Recorremos la palabra a adivinar
        eventos_juego['letras_correctas'].append("") ## Llenamos de strings vacíos la lista de letras correctas
        ## con la misma cantidad de letras que contenga la palabra a adivinar
 
    while True: ## Inciializamos el bucle principal

        clock.tick(30) ## Seteamos los fps a 30

        for event in pygame.event.get(): ## Recorremos los eventos de pygame
            if event.type == pygame.QUIT: ## Si el evento es igual a QUIT
                pygame.quit() ## Cerramos el juego
                quit()
            elif event.type == pygame.KEYDOWN: ## Si el evento es igual a presión de tecla
                if event.key in keys: ## Si el evento está en nuestro diccionario de teclas de pygame
                    letra = keys[event.key].upper() ## letra es igual al valor de nuestro diccionario con la clave que tomamos del input del usuario
                    if letra not in eventos_juego['letras_adivinadas']:  ## Si la letra no está en letras adivinadas (es decir en letras equivocadas)
                        resultado = verificar_letra(letra, eventos_juego['palabra_random'], eventos_juego['letras_adivinadas']) ## verificamos si la letra es correcta
                        if not resultado and eventos_juego['errores'] < 6: ## Si verificar_letra devuelve false y hay menos de 6 errores   
                            eventos_juego['errores'] += 1 ## Sumamos un error
                            dibujar_cuerpo(eventos_juego['errores']) ## Diujamos la parte del cuerpo que corresponde
                        else: # Sino
                            for i, x in enumerate(eventos_juego['palabra_random']): ## utilizamos enumerate para obtener los indices de la palabra random
                                if letra == x: 
                                    eventos_juego['letras_correctas'][i] = letra
                                    

                                    ## ["", "", ""], [S,"", L]

        keys_pressed = pygame.key.get_pressed() ## Obtenemos las keys presionadas

        if keys_pressed[pygame.K_LEFT]: ## Si aprieta la flecha para la izquierda
            ## Llamamos a update con nuestro personaje y un movimiento sobre el eje x de -10
            update(personaje, -10, 0, rect_rocket_league)
        if keys_pressed[pygame.K_RIGHT]: ## Si aprieta la flecha para la derecha
            ## Llamamos a update con nuestro personaje y un movimiento sobre el eje x de 10
            update(personaje, 10, 0, rect_rocket_league) 
        if keys_pressed[pygame.K_DOWN]: ## Si aprieta la flecha para abajo
            update(personaje, 0, 10, rect_rocket_league) 
            ## Llamamos a update con nuestro personaje y un movimiento sobre el eje y de 10
        if keys_pressed[pygame.K_UP]: # Si aprieta la flecha para arriba
            update(personaje, 0, -10, rect_rocket_league) 
            ## Llamamos a update con nuestro personaje y un movimiento sobre el eje y de -10

        ## Llamamos a dibujar_juego con los eventos del ahorcado como argumentos.
        dibujar_juego(eventos_juego['palabra_random'], eventos_juego['letras_adivinadas'], eventos_juego['errores'], eventos_juego['letras_correctas'])    
        
        ## Dibujamos el personaje en pantalla llamando utilizando blit
        pantalla.blit(personaje['surface'], personaje['rect_pos'])

        ## Si los errores son mayores o iguales a 6 o no hay más letras adivinar en letras_correctas
        ## entonces el juego terminó
        if eventos_juego['errores'] >= 6 or "" not in eventos_juego['letras_correctas']:
            eventos_juego['juego_terminado'] = True

        if eventos_juego['juego_terminado']: ## Si el juego terminó

            pantalla.fill(AZUL) ## Dibujamos toda la pantalla de azul si perdió o ganó para dibujar el texto del resultado del juego

            if eventos_juego['errores'] >= 6: ## Si los errrores son iguales o mayores a 6
                # mostramos el texto de perdiste con la palabra que era
                mostrar_texto(f"¡Perdiste, la palabra era {eventos_juego['palabra_random']}!", 125, 300, BLANCO, 50)
                # Reproducimos sonido de derrota
                pygame.mixer.Sound.play(perder_sonido)

            if "" not in eventos_juego['letras_correctas']: # Si no hay más letras por adivinar significa que gano

                mostrar_texto(f"¡Ganaste!", 325, 300, BLANCO, 50) # mostramos el texto de victoria
                pygame.mixer.Sound.play(ganar_sonido) # Reproducimos el sonido de victoria
     
            pygame.display.flip() ## Actualizamos el juego si gano o perdió
            time.sleep(5) ## Pausamos el juego 5 segundos antes de cerrar el juego
            pygame.quit() ## Cerramos pygame
            sys.exit() ## Cerramos el juego finalmente en cualquiera de los dos casos si perdió o ganó            

        pygame.display.update() ## Updateamos constantemente en el bucle while nuestro juego
        

        

# No ejecutar el juego automáticamente: solo se invoca desde consola o importación
# Descomentar la línea siguiente para probar el juego terminado:
jugar()
