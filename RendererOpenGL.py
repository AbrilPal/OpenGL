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
# HOMBRE 
# r.camPosition.z = 200
# r.camPosition.y = 100
# r.pointLight.y = 100
# r.pointLight.z = 50

# HAMSTER
# r.camPosition.z = 1
# r.camPosition.y = 0
# r.pointLight.y = 50
# r.pointLight.z = 50

# MUJER Y MUJER E HIJO  
r.camPosition.z = 50
r.camPosition.y = 150
r.pointLight.y = 0
r.pointLight.z = 300

r.setShaders(shaders.vertex_shader, shaders.fragment_shader)

r.modelList.append(Model('./models/mujer_hijo.obj', './models/mujer_hijo.bmp'))



isPlaying = True
while isPlaying:

    # Para revisar si una tecla esta presionada
    keys = pygame.key.get_pressed()

    # Move cam
    if keys[K_d]:
        r.camPosition.x += 1 * deltaTime
    if keys[K_a]:
        r.camPosition.x -= 1 * deltaTime
    if keys[K_w]:
        r.camPosition.z -= 1 * deltaTime
    if keys[K_s]:
        r.camPosition.z += 1 * deltaTime


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

    # Main Renderer Loop
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000


pygame.quit()
