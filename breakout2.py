import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Breakout")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
# Colores del arcoíris para los bloques
COLORES_ARCOIRIS = [
    (255, 0, 0),    # Rojo
    (255, 127, 0),  # Naranja
    (255, 255, 0),  # Amarillo
    (0, 255, 0),    # Verde
    (0, 0, 255),    # Azul
]

# Configuración de la paleta
PALETA_ANCHO = 100
PALETA_ALTO = 10
paleta_x = ANCHO // 2 - PALETA_ANCHO // 2
paleta_y = ALTO - 40
paleta_vel = 5

# Configuración de la pelota
PELOTA_TAMANO = 10
pelota_x = ANCHO // 2
pelota_y = ALTO // 2
pelota_dx = 4
pelota_dy = -4

# Configuración de los bloques
BLOQUE_ANCHO = 80
BLOQUE_ALTO = 30
BLOQUE_FILAS = 5
BLOQUE_COLUMNAS = 10
bloques = []

# Crear los bloques con colores
for fila in range(BLOQUE_FILAS):
    for columna in range(BLOQUE_COLUMNAS):
        bloque = {
            'rect': pygame.Rect(columna * BLOQUE_ANCHO, fila * BLOQUE_ALTO + 50,
                              BLOQUE_ANCHO - 2, BLOQUE_ALTO - 2),
            'color': COLORES_ARCOIRIS[fila]
        }
        bloques.append(bloque)

# Bucle principal del juego
ejecutando = True
reloj = pygame.time.Clock()

while ejecutando:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Movimiento de la paleta
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and paleta_x > 0:
        paleta_x -= paleta_vel
    if teclas[pygame.K_RIGHT] and paleta_x < ANCHO - PALETA_ANCHO:
        paleta_x += paleta_vel

    # Movimiento de la pelota
    pelota_x += pelota_dx
    pelota_y += pelota_dy

    # Colisiones con paredes
    if pelota_x <= 0 or pelota_x >= ANCHO - PELOTA_TAMANO:
        pelota_dx *= -1
    if pelota_y <= 0:
        pelota_dy *= -1
    if pelota_y >= ALTO:  # Pelota perdida
        pelota_x = ANCHO // 2
        pelota_y = ALTO // 2
        pelota_dy = -4

    # Colisión con la paleta
    paleta = pygame.Rect(paleta_x, paleta_y, PALETA_ANCHO, PALETA_ALTO)
    pelota_rect = pygame.Rect(pelota_x, pelota_y, PELOTA_TAMANO, PELOTA_TAMANO)
    if paleta.colliderect(pelota_rect) and pelota_dy > 0:
        pelota_dy *= -1

    # Colisión con bloques
    for bloque in bloques[:]:
        if bloque['rect'].colliderect(pelota_rect):
            bloques.remove(bloque)
            pelota_dy *= -1
            break

    # Dibujar todo
    pantalla.fill(NEGRO)
    
    # Dibujar paleta
    pygame.draw.rect(pantalla, BLANCO, (paleta_x, paleta_y, PALETA_ANCHO, PALETA_ALTO))
    
    # Dibujar pelota
    pygame.draw.circle(pantalla, ROJO, (int(pelota_x), int(pelota_y)), PELOTA_TAMANO)
    
    # Dibujar bloques con sus colores
    for bloque in bloques:
        pygame.draw.rect(pantalla, bloque['color'], bloque['rect'])

    # Actualizar pantalla
    pygame.display.flip()
    
    # Controlar FPS
    reloj.tick(60)

# Cerrar Pygame
pygame.quit()