# Andrea Abril Palencia Gutierrez, 18198
# Proyecto No.4 --- Graficas por computadora, seccion 20
# 25/11/2020 - 28/11/2020

import pygame
from pygame.locals import *

from gl import Renderer, Model
import shaders

deltaTime = 0.0

# Inicializacion de pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

# Inicializacion de nuestro Renderer en OpenGL
r = Renderer(screen)

# HAMSTER
r.camPosition.z = 1
r.camPosition.y = 0
r.pointLight.y = 50
r.pointLight.z = 50

r.setShaders(shaders.vertex_shader, shaders.fragment_shader)

m = Model('./models/Hamster.obj', './models/Hamster.bmp')

pygame.mixer.music.load('sonidos/caricatura.mp3')
pygame.mixer.music.play(0)

r.modelList.append(m)

isPlaying = True
while isPlaying:

    # Para revisar si una tecla esta presionada
    keys = pygame.key.get_pressed()

    # Movimientos de camara
    if keys[K_d]:
        r.camPosition.x += 1 * deltaTime
    if keys[K_a]:
        r.camPosition.x -= 1 * deltaTime
    if keys[K_w]:
        r.camPosition.z -= 1 * deltaTime
    if keys[K_s]:
        r.camPosition.z += 1 * deltaTime
    if keys[K_e]:
        r.camPosition.y -= 1 * deltaTime
    if keys[K_q]:
        r.camPosition.y += 1 * deltaTime
    if keys[K_r]:
        m.rotation.y += 3 * deltaTime
    if keys[K_t]:
        m.rotation.y -= 3 * deltaTime
    if keys[K_y]:
        m.rotation.x += 3 * deltaTime
    if keys[K_u]:
        m.rotation.x -= 3 * deltaTime
    if keys[K_i]:
        m.rotation.z += 3 * deltaTime
    if keys[K_o]:
        m.rotation.z -= 3 * deltaTime

    # cambiar de modelos
    if keys[K_c]:
        # MUJER 
        r.modelList.clear()
        r.camPosition.z = 50
        r.camPosition.y = 150
        r.pointLight.y = 0
        r.pointLight.z = 300
        m = Model('./models/mujer.obj', './models/mujer.bmp')
        r.modelList.append(m)
    if keys[K_v]:
        r.modelList.clear()
        # MUJER E HIJO
        r.camPosition.z = 50
        r.camPosition.y = 150
        r.pointLight.y = 0
        r.pointLight.z = 300
        m = Model('./models/mujer_hijo.obj', './models/mujer_hijo.bmp')
        r.modelList.append(m)
    if keys[K_b]:
        r.modelList.clear()
        # HAMSTER
        r.camPosition.z = 1
        r.camPosition.y = 0
        r.pointLight.y = 50
        r.pointLight.z = 50
        m = Model('./models/Hamster.obj', './models/Hamster.bmp')
        r.modelList.append(m)
    if keys[K_n]:
        r.modelList.clear()
        # HOMBRE
        r.camPosition.z = 50
        r.camPosition.y = 170
        r.camPosition.x = 5
        r.pointLight.y = 0
        r.pointLight.z = 300
        m = Model('./models/hombre.obj', './models/hombre.bmp')
        r.modelList.append(m)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            # para revisar en el momento que se presiona una tecla
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode()
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            r.pointLight.x = -r.pointLight.x - 100
            r.pointLight.y = -r.pointLight.y - 100

    # Main Renderer Loop
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000


pygame.quit()
