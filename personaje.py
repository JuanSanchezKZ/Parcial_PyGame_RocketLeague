import pygame ## Cargamos la librería pygame

pygame.mixer.init()  # Inicializa el motor de sonido
colision_sonido = pygame.mixer.Sound("colision.wav")  # Cargamos el archivo para el sonido de colision
pygame.mixer.Sound.set_volume(colision_sonido, 0.2) # Bajamos un poco el volumen

def crear_personaje(x, y, ancho, alto,nombre_archivo):

    imagen = pygame.image.load(nombre_archivo).convert_alpha()

    personaje = {
        "surface": pygame.transform.scale(imagen, (ancho, alto)),
        "rect_pos": pygame.Rect(x, y, ancho, alto),
    }

    return personaje

def update(personaje, incremento_x, incremento_y,  rect):
    
    original_x = personaje["rect_pos"].x

    original_y = personaje["rect_pos"].y

    personaje["rect_pos"].x += incremento_x

    personaje["rect_pos"].y += incremento_y

    if personaje["rect_pos"].colliderect(rect):
        personaje["rect_pos"].x = original_x
        personaje["rect_pos"].y = original_y