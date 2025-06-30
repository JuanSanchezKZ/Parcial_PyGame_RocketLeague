import random
import pygame

ancho_y_alto = (800, 600)
BLANCO = (255, 255, 255)
AZUL = (37, 36, 64)
pantalla = pygame.display.set_mode(ancho_y_alto)

# ----------------- SONIDO -----------------
pygame.mixer.init()  # Inicializa el motor de sonido
sonido_error = pygame.mixer.Sound("error.wav")  # Asegurate de tener este archivo
pygame.mixer.Sound.set_volume(sonido_error, 0.2)

descripcion_1 = 'Adiviná la palabra. Tenés 6 intentos para completar la palabra.'
descripcion_2 = 'Elige una letra, cada letra errónea será un error.'


# ----------------- CARGAR PALABRAS DESDE ARCHIVO -----------------
def cargar_palabras():
    # Leer las palabras desde un archivo de texto y devolver una lista
    # Asegurate de tener un archivo llamado palabras.txt con una palabra por línea

    lista_palabras = []

    with open("palabras.txt", 'r') as archivo:
        lista_de_lineas = archivo.readlines() 
        for linea in lista_de_lineas:
            lista_palabras.append(linea.strip()) ## Recorremos la lista que devuelve readlines para utilizar strip() y sacar los espacios en blanco o saltos de linea.
               
    return lista_palabras

# ----------------- ELEGIR PALABRA AL AZAR -----------------
def elegir_palabra(lista_palabras: list):
    # Elegir una palabra aleatoria de la lista y convertirla a mayúsculas

    numero_aleatorio = random.randint(0, len(lista_palabras) - 1)

    palabra_aleatoria = lista_palabras[numero_aleatorio].upper()

    return palabra_aleatoria

def mostrar_texto(texto, x, y, color, tamanio_fuente):# Definimos la función mostrar_texto que recibe el texto, coordenadas x e y, color y tamaño de fuente

    fuente = pygame.font.SysFont('freesansbold.ttf', tamanio_fuente) # Cargamos la fuente con el tamaño especificado

    text = fuente.render(texto, True, color) # Renderizamos el texto con la fuente y el color especificado

    textRect = text.get_rect() # Obtenemos el rectángulo del texto renderizado

    textRect.x = x # Asignamos la coordenada x al rectángulo del texto
    textRect.y = y # Asignamos la coordenada y al rectángulo del texto

    pantalla.blit(text, textRect) # Dibujamos el texto en la pantalla en la posición especificada

# ----------------- DIBUJAR ESTRUCTURA DEL AHORCADO -----------------
def dibujar_estructura(): # Dibujamos la estructura del ahorcado
    
    pygame.draw.rect(pantalla, BLANCO, (50, 520, 150, 15))  # Dibujamos la Base del ahorcado con su color su eje x e y y su ancho y alto

    # Palo vertical
    pygame.draw.line(pantalla, BLANCO, (125, 520), (125, 200), 8) # Dibujamos el Palo Vertical del ahorcado con su color su eje x e y y su ancho y alto

    # Palo superior
    pygame.draw.line(pantalla, BLANCO, (125, 200), (250, 200), 8) # Dibujamos el Palo superior del ahorcado con su color su eje x e y y su ancho y alto

    # Cuerda
    pygame.draw.line(pantalla, BLANCO, (250, 200), (250, 240), 3) # Dibujamos la cuerda con su color su eje x e y y su ancho y alto
        

# ----------------- DIBUJAR PARTES DEL CUERPO -----------------
def dibujar_cuerpo(errores):
    # Dibujar cabeza, tronco, brazos y piernas en base a la cantidad de errores
    if errores >= 1:
        pygame.draw.circle(pantalla, BLANCO, (250, 270), 30, 3)

    if errores >= 2:
        pygame.draw.line(pantalla, BLANCO, (250, 300), (250, 400), 3)

    if errores >= 3:
        pygame.draw.line(pantalla, BLANCO, (250, 320), (210, 360), 3)

    if errores >= 4:
        pygame.draw.line(pantalla, BLANCO, (250, 320), (290, 360), 3)

    if errores >= 5:
        pygame.draw.line(pantalla, BLANCO, (250, 400), (210, 460), 3)

    if errores >= 6:
        pygame.draw.line(pantalla, BLANCO, (250, 400), (290, 460), 3)

def dibujar_lineas_o_texto(letras_correctas):

    for i, caracter in enumerate(letras_correctas):

        if caracter == "":
            pygame.draw.line(pantalla, BLANCO, (350 + i * 40, 500), (380 + i * 40, 500), 3)
        else:
            mostrar_texto(caracter, 350 + i * 42, 480, BLANCO, 30)
        


# ----------------- DIBUJAR JUEGO EN PANTALLA -----------------
def dibujar_juego(palabra, letras_adivinadas, errores, letras_correctas):
    # Llenar fondo, mostrar palabra oculta, letras ingresadas y dibujar estructura y cuerpo
    pantalla.fill(AZUL) # Llenamos el fondo con el color azul

    mostrar_texto(descripcion_1, 15, 15, BLANCO, 25) 

    mostrar_texto(descripcion_2, 15, 38, BLANCO, 25)

    rect_x = (800 / 2) + 50 
    rect_y = 100 

    # Dibujamos el rectángulo
    pygame.draw.rect(pantalla, BLANCO, (rect_x, rect_y, 300, 200), 3)
    
    for i, palabra in enumerate(letras_adivinadas):
            mostrar_texto(palabra, 50 + i * 30, 100, BLANCO, 30) 

    dibujar_lineas_o_texto(letras_correctas)

    dibujar_cuerpo(errores)

    dibujar_estructura()


# ----------------- VERIFICAR LETRA -----------------
def verificar_letra(letra, palabra_random: str, letras_adivinadas): ## letras adivinadas = letras incorrectas
    # Agregar la letra a letras_adivinadas si no estaba
    # Retornar True si la letra está en la palabra, False si no
    if letra in palabra_random: #Iniamos la condicion de si la letra está en la palabra
        return True #Devolvemos True si la letra está en la palabra
    else: #Sino
        pygame.mixer.Sound.play(sonido_error) # Si la letra no está en la palabra, reproducimos el sonido de error
        letras_adivinadas.append(letra) # Agregamos la letra a letras adivinadas
        return False # Devolvemos False si la letra no está en la palabra¡