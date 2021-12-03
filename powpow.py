from typing import final
from numpy import csingle
import pygame
from pygame.event import get
from pygame.locals import *
from pygame.mixer import pause
from pygame.time import *
import random
import time

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 800))
clock = Clock()
w = screen.get_width()
h = screen.get_height()
font = pygame.font.SysFont(None, 24)


yoo_sound = pygame.mixer.Sound('assets/sound/yoo.wav')
#exclam = pygame.image.load("assets/sprites/exclam.png").convert()
#background = pygame.image.load("assets/sprites/background.png").convert()
p1_stand = pygame.image.load("assets/sprites/p1_stand.png").convert()
p2_stand = pygame.image.load("assets/sprites/p2_stand.png").convert()
p1_atk = pygame.image.load("assets/sprites/p1_atk.png").convert()
p2_atk = pygame.image.load("assets/sprites/p2_atk.png").convert()
p1_loose = pygame.image.load("assets/sprites/p1_loose.png").convert()
p2_loose = pygame.image.load("assets/sprites/p2_loose.png").convert()

p1_stand = pygame.transform.scale(p1_stand, (100, 100))
p2_stand = pygame.transform.scale(p2_stand, (100, 100))

p2_stand = pygame.transform.flip(p2_stand, True, False)

font = pygame.font.SysFont(None, 24)


exclam = pygame.Rect(w / 2, h / 2, 60, 60)



p1_key = pygame.K_m
p2_key = pygame.K_s

screen.fill((0, 0, 0))
_delay = random.randrange(3000, 10000)
__delay = 5000

def pause_loop():
    pause = True
    while pause:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pause = False
            if e.type == pygame.KEYDOWN:
                pause = False

def match_loop():
    atk = False
    running = True
    p1_state = -1
    p2_state = -1
    yoo_sound.play()
    #yoo_sound.stop()
    while running:
        for e in  pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                if e.key == p1_key:
                    if atk:
                        p1_state = pygame.time.get_ticks() - _delay
                    else:
                        return "p2"
                if e.key == p2_key:
                    if atk:
                        p2_state = pygame.time.get_ticks() - _delay
                    else:
                        return "p1"
        if (pygame.time.get_ticks() >= _delay) and not atk:
            atk = True
        if atk and pygame.time.get_ticks() - _delay >= __delay:
            atk = False
        
        screen.fill((0, 0, 0))
        if atk:
            pygame.draw.rect(screen, (0, 255, 0), exclam)
        if p1_state == -1 and p2_state != -1:
            return "p2"
        elif p1_state != -1 and p2_state == -1:
            return "p1"
        elif p1_state != -1 and p2_state != -1:
            return "p1" if p1_state < p2_state else "p2"
        screen.blit(p1_stand, (0, h / 2))
        screen.blit(p2_stand, (w - 100, h / 2))
        pygame.display.update()
        clock.tick(60)

def game_loop():
    winner = match_loop()
    yoo_sound.stop()
    txt = font.render(f"{winner} WINS THIS MATCH", True, (255, 0, 0) if winner == "p1" else (0, 0, 255))
    screen.blit(txt, (20, 20))
    pygame.display.update()
    pause_loop()
    return winner

final_score = [game_loop(), game_loop(), game_loop()]
game_winner = "p1" if final_score.count("p1") > final_score.count("p2") else "p2"
txt = font.render(f"{game_winner} WINS THE GAME", True, (255, 0, 0) if game_winner == "p1" else (0, 0, 255))
screen.blit(txt, (w / 2, 20))
pygame.display.update()
pause_loop()
