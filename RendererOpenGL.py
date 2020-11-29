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

def text_objects(text, font):
  textSurface = font.render(text, True, (0,0,0))
  return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac, action=None):
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  if x+w > mouse[0] > x and y+h > mouse[1] > y:
      pygame.draw.rect(screen, ac,(x,y,w,h))

      if click[0] == 1 and action != None:
        if action == 'listo':
          modelos()

  else:
      pygame.draw.rect(screen, ic,(x,y,w,h))

  smallText = pygame.font.Font("freesansbold.ttf",20)
  textSurf, textRect = text_objects(msg, smallText)
  textRect.center = ( (x+(w/2)), (y+(h/2)) )
  screen.blit(textSurf, textRect)

# PANTALLA DE INSTRUCTIVO
def intro():
    intro = True
    pygame.mixer.music.load('sonidos/espera1.mp3')
    pygame.mixer.music.play(10)
    screen = pygame.display.set_mode((1000, 600))
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()

        # TITULO
        screen.fill((176, 239, 252))
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects('Instructivo', largeText)
        TextRect.center = ((1000/2),(50))
        screen.blit(TextSurf, TextRect)

        # TECLAS
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('Q -- arriba', largeText)
        TextRect.center = ((1000/2),(100))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('W -- adelante', largeText)
        TextRect.center = ((1000/2),(120))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('E -- abajo', largeText)
        TextRect.center = ((1000/2),(140))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('R -- rotacion "y" derecha', largeText)
        TextRect.center = ((1000/2),(160))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('T -- rotacion "y" izquierda', largeText)
        TextRect.center = ((1000/2),(180))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('Y -- rotacion "x" abajo', largeText)
        TextRect.center = ((1000/2),(200))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('U -- rotacion "x" arriba', largeText)
        TextRect.center = ((1000/2),(220))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('I -- rotacion "z" izquierda', largeText)
        TextRect.center = ((1000/2),(240))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('O -- rotacion "z" derecha', largeText)
        TextRect.center = ((1000/2),(260))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('A -- izquierda', largeText)
        TextRect.center = ((1000/2),(280))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('S -- atras', largeText)
        TextRect.center = ((1000/2),(300))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('D -- derecha', largeText)
        TextRect.center = ((1000/2),(320))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('C -- modelo mujer', largeText)
        TextRect.center = ((1000/2),(340))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('V -- modelo mujer e hijo', largeText)
        TextRect.center = ((1000/2),(360))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('B -- modelo hamster', largeText)
        TextRect.center = ((1000/2),(380))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('N -- modelo hombre', largeText)
        TextRect.center = ((1000/2),(400))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('M -- instructivo', largeText)
        TextRect.center = ((1000/2),(440))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects('MOUSE -- cambio de luz', largeText)
        TextRect.center = ((1000/2),(420))
        screen.blit(TextSurf, TextRect)

        # TEXTO
        largeText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects('Perdon por el proyecto pasado, espero este si <3', largeText)
        TextRect.center = ((1000/2),(470))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects('En este si me esmere :) porque que verguenza', largeText)
        TextRect.center = ((1000/2),(490))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 17)
        TextSurf, TextRect = text_objects('A veces tarda', largeText)
        TextRect.center = ((800),(150))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 17)
        TextSurf, TextRect = text_objects('en cambiar de modelo :|', largeText)
        TextRect.center = ((800),(170))
        screen.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf', 17)
        TextSurf, TextRect = text_objects('no se desespere, gracias!', largeText)
        TextRect.center = ((800),(190))
        screen.blit(TextSurf, TextRect)

        # BOTON
        button('Listo',450,530,120,50,(227, 176, 252),(227, 176, 252),'listo')

        pygame.display.update()

def modelos():
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
    pygame.mixer.music.play(10)

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

        # REGRESAR A INSTRUCTIVO
        if keys[K_m]:
            intro()

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

intro()