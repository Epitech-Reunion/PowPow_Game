import pygame
from pygame.event import get
from pygame.locals import *
from pygame.time import *
import random

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 800))
clock = Clock()
w = screen.get_width()
h = screen.get_height()

exclam = pygame.image.load("assets/exclam.png").convert()
background = pygame.image.load("assets/background.png").convert()
p1_stand = pygame.image.load("assets/p1_stand.png").convert()
p2_stand = pygame.image.load("assets/p2_stand.png").convert()
p1_atk = pygame.image.load("assets/p1_atk.png").convert()
p2_atk = pygame.image.load("assets/p2_atk.png").convert()
p1_loose = pygame.image.load("assets/p1_loose.png").convert()
p2_loose = pygame.image.load("assets/p2_loose.png").convert()

p1 = pygame.Rect(30, h / 2 , 30, 30)
p2 = pygame.Rect(w - 60, h / 2, 30, 30)
exclam = pygame.Rect(w / 2, h / 2, 60, 60)

win = None
p1_state = -1
p2_state = -1
p1_key = pygame.K_m
p2_key = pygame.K_s

running = True
screen.fill((0, 0, 0))
_delay = random.randrange(3000, 10000)
__delay = 5000
atk = False

while running:
    for e in  pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == p1_key:
                if atk:
                    p1_state = pygame.time.get_ticks() - _delay
                else:
                    win = "p2"
            if e.key == p2_key:
                if atk:
                    p2_state = pygame.time.get_ticks() - _delay
                else:
                    win = "p1"
    if (pygame.time.get_ticks() >= _delay) and not atk:
        atk = True
    if atk and pygame.time.get_ticks() - _delay >= __delay:
        atk = False
    screen.fill((0, 0, 0))
    if atk:
        pygame.draw.rect(screen, (0, 255, 0), exclam)
    if p1_state == -1 and p2_state != -1:
        win = "p2"
    if p1_state != -1 and p2_state == -1:
        win = "p1"
    if p1_state != -1 and p2_state != -1:
        win = "p1" if p1_state < p2_state else "p2"
    if win != None:
        print(win)
        running = False
    pygame.draw.rect(screen, (255, 0, 0), p1)
    pygame.draw.rect(screen, (0, 0, 255), p2)
    pygame.display.update()