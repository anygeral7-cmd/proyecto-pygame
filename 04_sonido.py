import pygame
import math
import array

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=1)

ANCHO, ALTO = 600, 300
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejemplo 4 - Sonido")

# Crear un tono de audio sin archivos externos
frecuencia = 440
duracion = 1
muestras = 44100
volumen = 10000

audio = array.array("h")

for i in range(muestras * duracion):
    valor = int(
        volumen * math.sin(2 * math.pi * frecuencia * i / 44100)
    )
    audio.append(valor)

sonido = pygame.mixer.Sound(buffer=audio.tobytes())
sonido.set_volume(0.5)

BLANCO = (255, 255, 255)
AZUL = (30, 100, 220)
NEGRO = (0, 0, 0)

fuente = pygame.font.Font(None, 36)
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                sonido.play()

    pantalla.fill(BLANCO)
    texto = fuente.render("Pulsa ESPACIO para escuchar", True, AZUL)
    pantalla.blit(texto, (90, 100))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
