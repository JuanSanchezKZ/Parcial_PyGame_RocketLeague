import pygame ## Cargamos la librería pygame

pygame.mixer.init()  # Inicializa el motor de sonido
colision_sonido = pygame.mixer.Sound("colision.wav")  # Cargamos el archivo para el sonido de colision
pygame.mixer.Sound.set_volume(colision_sonido, 0.2) # Bajamos un poco el volumen

def crear_personaje(x, y, ancho, alto,nombre_archivo):

    imagen = pygame.image.load(nombre_archivo).convert_alpha() ## Cargamos la imagen del personaje y la pasamos a alpha

    personaje = { ## Diccionario de personaje
        "surface": pygame.transform.scale(imagen, (ancho, alto)), ## Seteamos la surface del personaje para poder renderizarlo en pantalla
        "rect_pos": pygame.Rect(x, y, ancho, alto), ## Seteamos el rectangulo del personaje para generar colisiones y renderizarlo en pantalla
    }

    return personaje ## Retornamos el diccionario con el personaje

def update(personaje, incremento_x, incremento_y,  rect):
    
    original_x = personaje["rect_pos"].x ## La x original del personaje para generar la colision

    original_y = personaje["rect_pos"].y # La y original del personaje para generar la colision

    personaje["rect_pos"].x += incremento_x # Mvemos el personaje sobre el eje x

    personaje["rect_pos"].y += incremento_y # Movemos el personaje sobre el eje y

    if personaje["rect_pos"].colliderect(rect): # Si colisionó con un rectangulo
        personaje["rect_pos"].x = original_x # Generamos un efecto de choque evitando movimiento "trabando" el eje x del personaje
        personaje["rect_pos"].y = original_y # Lo mismo con el eje y