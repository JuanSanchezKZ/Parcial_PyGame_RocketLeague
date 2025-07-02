import pygame ## Cargamos la librería pygame

pygame.mixer.init()  # Inicializa el motor de sonido
colision_sonido = pygame.mixer.Sound("archivos/colision.wav")  # Cargamos el archivo para el sonido de colision
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


    ## Declaramos los limites donde se va a poder mover el personaje
    hitbox_left = 310
    hitbox_right = 800
    hitbox_top = 70
    hitbox_bottom = 450

    personaje["rect_pos"].x += incremento_x # Mvemos el personaje sobre el eje x

    personaje["rect_pos"].y += incremento_y # Movemos el personaje sobre el eje y

    if personaje["rect_pos"].colliderect(rect): # Si colisionó con un rectangulo
        personaje["rect_pos"].x = original_x # Generamos un efecto de choque evitando movimiento "trabando" el eje x del personaje
        personaje["rect_pos"].y = original_y # Lo mismo con el eje y
        pygame.mixer.Sound.play(colision_sonido)
    ## Generamos una hitbox invisible para que no interfiera como el juego en si
    if personaje["rect_pos"].left < hitbox_left:  # hitbox del lado izquierdo (ahorcado)   
        personaje["rect_pos"].left = hitbox_left
    if personaje["rect_pos"].right > hitbox_right: # hitbox del lado derecho (extremo derecho de la pantalla)
        personaje["rect_pos"].right = hitbox_right
    if personaje["rect_pos"].top < hitbox_top: # hitbox de arriba (descripcion)
        personaje["rect_pos"].top = hitbox_top
    if personaje["rect_pos"].bottom > hitbox_bottom: # hitbox de abajo (texto a adivinar)
        personaje["rect_pos"].bottom = hitbox_bottom    