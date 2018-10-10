import pygame

class Pozadina:
    """Klasa koje sluzi za pozadinu na ekranu"""
    def __init__(self,ekran,lokacija_slike):
        self.ekran=ekran
        self.lokacija_slike=lokacija_slike

        self.slika=pygame.image.load(self.lokacija_slike)

    def postavi(self):
        self.ekran.blit(self.slika,(0,0))