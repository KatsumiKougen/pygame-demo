import pygame
from pygame.locals import *

pygame.init() 
pygame.mixer.init()
poi = pygame.mixer.Sound("botan_poi.ogg")

clock = pygame.time.Clock()
clock.tick(60)

win = pygame.display.set_mode([640, 400])

class playerSprite(pygame.sprite.Sprite):

    def __init__(self):
        super(playerSprite, self).__init__()
        self.sprite = pygame.image.load("shime20.png").convert()
        self.sprite.set_colorkey((0xff, 0xff, 0xff), RLEACCEL)
        self.rect = self.sprite.get_rect()

    def move(self, key):
        if key[K_UP]:
            self.rect.move_ip(0, -1)
        elif key[K_DOWN]:
            self.rect.move_ip(0, 1)
        elif key[K_LEFT]:
            self.rect.move_ip(-1, 0)
        elif key[K_RIGHT]:
            self.rect.move_ip(1, 0)
        elif key[K_SPACE]:
            poi.play()

player = playerSprite()

running = True

while running: 

    win.fill([0x22, 0x22, 0x22])

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    keypress = pygame.key.get_pressed()
    player.move(keypress)

    win.blit(player.sprite, player.rect)
    pygame.display.flip()

pygame.quit()
