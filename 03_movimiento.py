import pygame

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejemplo 3 - Movimiento")

BLANCO = (255, 255, 255)
AZUL = (0, 100, 255)

x = 375
y = 275
velocidad = 5
reloj = pygame.time.Clock()

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Evitar que el personaje salga de la ventana
    x = max(0, min(x, ANCHO - 50))
    y = max(0, min(y, ALTO - 50))

    pantalla.fill(BLANCO)
    pygame.draw.rect(pantalla, AZUL, (x, y, 50, 50))
    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
