import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,screen_width,speed):
        super().__init__()
        self.image = pygame.image.load('./graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x = screen_width
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

        self.lasers = pygame.sprite.Group()

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if self.rect.right > self.max_x:
                self.rect.right = self.max_x
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            if self.rect.left < 0:
                self.rect.left = 0
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.ready = False
            self.shoot_laser()
            self.laser_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center, 8, self.rect.bottom))

    def update(self):
        self.get_input()
        self.recharge()
        self.lasers.update()