import pygame

def crear_personaje(x, y, ancho, alto,nombre_archivo):

    imagen = pygame.image.load(nombre_archivo)
    personaje = {
        "surface": pygame.transform.scale(imagen, (ancho, alto)),
        "rect_pos": pygame.Rect(x, y, 200, 200),
        "rect": pygame.Rect((x+ancho/2)- 10, y+90, 40, 20)
    }

    return personaje

def update(personaje, incremento_x):

    nueva_x = personaje["rect_pos"].x + incremento_x

    if nueva_x > 0 and nueva_x < 600:
        personaje["rect_pos"].x = personaje["rect_pos"].x + incremento_x
        personaje["rect"].x = personaje["rect"].x + incremento_x