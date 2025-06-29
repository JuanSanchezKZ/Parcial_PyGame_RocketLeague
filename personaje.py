import pygame

def crear_personaje(x, y, ancho, alto,nombre_archivo):

    imagen = pygame.image.load(nombre_archivo)
    personaje = {
        "surface": pygame.transform.scale(imagen, (ancho, alto)),
        "rect_pos": pygame.Rect(x, y, ancho, alto),
        "rect": pygame.Rect((x+ancho/2)- 10, y+90, 40, 20)
    }

    return personaje

def update(personaje, incremento_x, rect):

    personaje["rect_pos"].x += incremento_x

    if personaje["rect_pos"].left < rect.left:
        personaje["rect_pos"].left = rect.left
    
    if personaje["rect_pos"].right > rect.right:
        personaje["rect_pos"].right = rect.right
