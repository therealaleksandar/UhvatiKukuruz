import pygame

from pygame.sprite import Sprite
from random import randint

class Kukuruz(Sprite):
    """Klasa kukuruza koji se prikuplja"""
    def __init__(self,ekran,podesavanja,stats):
        super().__init__()
        self.ekran=ekran
        self.ekran_rect=self.ekran.get_rect()
        self.podesavanja=podesavanja
        self.stats=stats

        #dodavanje slike i pravljenje rect-a
        self.image=pygame.image.load('slike/kukuruz.png')
        self.rect=self.image.get_rect()

        #postavljanje kukuruza iznad ekrana
        self.rect.bottom=self.ekran_rect.top
        self.rect.x=randint(0,self.ekran_rect.width-self.rect.width)

        self.y=float(self.rect.y)

    def update(self):
        if self.stats.kukuruz_pada:
            self.y+=self.podesavanja.kukuruz_brzina_spustanja
            self.rect.y=self.y

class KukuruzMali(Sprite):
    """Klasa kukuruza koji se prikuplja"""
    def __init__(self,ekran,podesavanja):
        super().__init__()
        self.ekran=ekran
        self.ekran_rect=self.ekran.get_rect()
        self.podesavanja=podesavanja

        #dodavanje slike i pravljenje rect-a
        self.image=pygame.image.load('slike/kukuruz_mali.png')
        self.rect=self.image.get_rect()
