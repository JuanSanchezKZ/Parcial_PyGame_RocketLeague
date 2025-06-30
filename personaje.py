import pygame ## Cargamos la librería pygame

pygame.mixer.init()  # Inicializa el motor de sonido
colision_sonido = pygame.mixer.Sound("colision.wav")  # Cargamos el archivo para el sonido de colision
pygame.mixer.Sound.set_volume(colision_sonido, 0.2) # Bajamos un poco el volumen

def crear_personaje(x, y, ancho, alto,nombre_archivo):

    imagen = pygame.image.load(nombre_archivo)
    personaje = {
        "surface": pygame.transform.scale(imagen, (ancho, alto)),
        "rect_pos": pygame.Rect(x, y, ancho, alto),
    }

    return personaje

def update(personaje, incremento_x, rect):

    personaje["rect_pos"].x += incremento_x

    if personaje["rect_pos"].left < rect.left:
        personaje["rect_pos"].left = rect.left
        pygame.mixer.Sound.play(colision_sonido)
    
    if personaje["rect_pos"].right > rect.right:
        personaje["rect_pos"].right = rect.right
        pygame.mixer.Sound.play(colision_sonido)
