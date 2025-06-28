import random
import pygame

ancho_y_alto = (800, 600)
BLANCO = (255, 255, 255)
AZUL = (37, 36, 64)
pantalla = pygame.display.set_mode(ancho_y_alto)

descripcion = 'Adiviná la palabra. Tenés 6 intentos para completar la palabra. Elige una letra, cada letra errónea será un error.'

# ----------------- CARGAR PALABRAS DESDE ARCHIVO -----------------
def cargar_palabras():
    # Leer las palabras desde un archivo de texto y devolver una lista
    # Asegurate de tener un archivo llamado palabras.txt con una palabra por línea

    lista_palabras = []

    with open("palabras.txt", 'r') as archivo:
        lista_de_lineas = archivo.readlines() 
        for linea in lista_de_lineas:
            lista_palabras.append(linea.strip())
               
    return lista_palabras

# ----------------- ELEGIR PALABRA AL AZAR -----------------
def elegir_palabra(lista_palabras: list):
    # Elegir una palabra aleatoria de la lista y convertirla a mayúsculas

    numero_aleatorio = random.randint(1, len(lista_palabras))

    palabra_aleatoria = lista_palabras[numero_aleatorio].upper()

    return palabra_aleatoria

def mostrar_texto(texto, x, y, color, tamanio_fuente):

    fuente = pygame.font.SysFont('freesansbold.ttf', tamanio_fuente)

    text = fuente.render(texto, False, color)

    textRect = text.get_rect()

    textRect.x = x
    textRect.y = y

    pantalla.blit(text, textRect)

# ----------------- DIBUJAR ESTRUCTURA DEL AHORCADO -----------------
def dibujar_estructura():
    
        # Base más chica (cerca del borde izquierdo)
    pygame.draw.rect(pantalla, BLANCO, (50, 520, 150, 15))  # base al borde

    # Palo vertical
    pygame.draw.line(pantalla, BLANCO, (125, 520), (125, 200), 8)

    # Palo superior
    pygame.draw.line(pantalla, BLANCO, (125, 200), (250, 200), 8)

    # Cuerda
    pygame.draw.line(pantalla, BLANCO, (250, 200), (250, 240), 3)
        

# ----------------- DIBUJAR PARTES DEL CUERPO -----------------
def dibujar_cuerpo(errores):
    # Dibujar cabeza, tronco, brazos y piernas en base a la cantidad de errores
    pass

# ----------------- DIBUJAR JUEGO EN PANTALLA -----------------
def dibujar_juego(palabra, letras_adivinadas, errores):
    # Llenar fondo, mostrar palabra oculta, letras ingresadas y dibujar estructura y cuerpo
    pantalla.fill(AZUL)

    for i, caracter in enumerate(palabra):

        pygame.draw.line(pantalla, BLANCO, (350 + i * 40, 500), (380 + i * 40, 500), 3)

    mostrar_texto(descripcion, 15, 15, BLANCO, 20)

    dibujar_estructura()

    

# ----------------- VERIFICAR LETRA -----------------
def verificar_letra(letra, palabra: str, letras_adivinadas): ## letras adivinadas = letras incorrectas
    # Agregar la letra a letras_adivinadas si no estaba
    # Retornar True si la letra está en la palabra, False si no
    if letra in palabra:
        return True
    else:
        if letra not in letras_adivinadas:
            letras_adivinadas.append(letra)
            return False