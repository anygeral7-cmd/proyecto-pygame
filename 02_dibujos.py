import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ejemplo 2 - Figuras geometricas")

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 200, 0)
AZUL = (0, 100, 255)
NEGRO = (0, 0, 0)

pantalla.fill(BLANCO)

# Dibujar un rectangulo
pygame.draw.rect(pantalla, ROJO, (50, 50, 200, 100))

# Dibujar un circulo
pygame.draw.circle(pantalla, VERDE, (400, 150), 60)

# Dibujar una linea
pygame.draw.line(pantalla, AZUL, (50, 300), (700, 300), 5)

# Dibujar una elipse
pygame.draw.ellipse(pantalla, NEGRO, (300, 380, 180, 100))

pygame.display.flip()

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

pygame.quit()
