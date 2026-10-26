import pygame
import random

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapa la estrella")

BLANCO = (255, 255, 255)
AZUL = (30, 100, 230)
AMARILLO = (255, 210, 0)
NEGRO = (30, 30, 30)

reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 36)

jugador = pygame.Rect(100, 100, 40, 40)
estrella = pygame.Rect(
    random.randint(0, ANCHO - 25),
    random.randint(50, ALTO - 25),
    25, 25
)

velocidad = 5
puntos = 0
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        jugador.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador.x += velocidad
    if teclas[pygame.K_UP]:
        jugador.y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador.y += velocidad

    jugador.clamp_ip(pantalla.get_rect())

    if jugador.colliderect(estrella):
        puntos += 1
        estrella.x = random.randint(0, ANCHO - estrella.width)
        estrella.y = random.randint(50, ALTO - estrella.height)

    pantalla.fill(BLANCO)

    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.ellipse(pantalla, AMARILLO, estrella)

    texto = fuente.render(f"Puntos: {puntos}", True, NEGRO)
    pantalla.blit(texto, (20, 15))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
