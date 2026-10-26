import pygame

pygame.init()

ANCHO = 800
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi primera ventana")

AZUL = (50, 120, 220)
pantalla.fill(AZUL)

pygame.display.flip()

ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

pygame.quit()
