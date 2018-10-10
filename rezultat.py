import pygame

from pygame.sprite import Group
from kukuruz import KukuruzMali

class Rezultat:
    """Klasa za prikaz rezultata"""
    def __init__(self,ekran,stats,podesavanja):
        self.ekran=ekran
        self.ekran_rect=self.ekran.get_rect()
        self.stats=stats
        self.podesavanja=podesavanja

        self.veliki_font=pygame.font.SysFont(None,60)
        self.mali_font=pygame.font.SysFont(None,25)

        self.pripremi_rezultat()
        self.pripremi_propale_kukuruze()
        self.pripremi_nivo()
        self.pripremi_najbolji_rez()

    def pripremi_rezultat(self):
        """Funkcija koja priprema vrednost trenutnog rezultata"""
        self.slika=self.veliki_font.render(str(self.stats.uhvaceni),True,
            self.podesavanja.rezultat_boja_fonta)
        self.rect=self.slika.get_rect()
        self.rect.centerx=self.ekran_rect.centerx
        self.rect.top=10

    def pripremi_propale_kukuruze(self):
        """Funkcija koja priprema vrednost propalih kukuruza"""
        self.kukuruzi_propali=Group()
        for broj_kukuruza in range(self.stats.propali):
            kukuruz_mali=KukuruzMali(self.ekran,self.podesavanja)
            kukuruz_mali.rect.right=self.ekran_rect.width-10-kukuruz_mali.rect.width*broj_kukuruza
            kukuruz_mali.rect.top=self.ekran_rect.top+10
            self.kukuruzi_propali.add(kukuruz_mali)

    def pripremi_nivo(self):
        """Funkcija koja priprema nivo igre"""
        self.nivo=self.mali_font.render('Nivo: '+str(self.stats.nivo),True,self.podesavanja.rezultat_boja_fonta)
        self.nivo_rect=self.nivo.get_rect()
        self.nivo_rect.right=self.ekran_rect.width-10
        self.nivo_rect.top=self.ekran_rect.top+50

    def pripremi_najbolji_rez(self):
        """Funkcija koja priprema najbolji rezultat"""
        self.najbolji_rez=self.veliki_font.render(str(self.stats.najbolji_rezultat),True,
            self.podesavanja.rezultat_boja_fonta)
        self.najbolji_rez_rect=self.najbolji_rez.get_rect()
        self.najbolji_rez_rect.left=10
        self.najbolji_rez_rect.top=10


    def prikazi_rezultat(self):
        """Funkcija koja crta rezultat i preostale kukuruze"""
        self.ekran.blit(self.slika,self.rect)
        self.kukuruzi_propali.draw(self.ekran)
        self.ekran.blit(self.nivo,self.nivo_rect)   
        self.ekran.blit(self.najbolji_rez,self.najbolji_rez_rect)
