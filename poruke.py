import pygame

class Poruke:
    """Klasa koja sluzi za ispis poruka po ekranu"""
    def __init__(self,ekran,stats,podesavanja):
        self.stats=stats
        self.podesavanja=podesavanja
        self.ekran=ekran
        self.ekran_rect=self.ekran.get_rect()

        self.font=pygame.font.SysFont(None,50)

        self.ispisi_kraj()
        self.novi_naj_rezultat()
        self.pripremi_uhvatili_ste()
    
    def ispisi_kraj(self):
        #ispisuje kraj i broj uhvacenih kukuruza
        self.kraj=self.font.render("KRAJ.",True,self.podesavanja.rezultat_boja_fonta)
        self.kraj_rect=self.kraj.get_rect()
        self.kraj_rect.center=self.ekran_rect.center

    def novi_naj_rezultat(self):
        #ispisuje novi najbolji rezultat
        self.novi_naj=self.font.render("NOVI NAJBOLJI REZULTAT!",True,
            self.podesavanja.rezultat_boja_fonta)
        self.novi_naj_rect=self.novi_naj.get_rect()
        self.novi_naj_rect.center=self.ekran_rect.center

    def pripremi_uhvatili_ste(self):
        #ispisi uhvatili ste
        self.uhvaceno=self.font.render("Broj sakupljenih kukuruza: "+str(self.stats.uhvaceni),True,
            self.podesavanja.rezultat_boja_fonta)
        self.uhvaceno_rect=self.uhvaceno.get_rect()
        self.uhvaceno_rect.centerx=self.ekran_rect.centerx
        self.uhvaceno_rect.top=self.novi_naj_rect.bottom+20

    def blit_kraj(self):
        self.ekran.blit(self.kraj,self.kraj_rect)
        self.ekran.blit(self.uhvaceno,self.uhvaceno_rect)
    
    def blit_novi_naj(self):
        self.ekran.blit(self.novi_naj,self.novi_naj_rect)
        self.ekran.blit(self.uhvaceno,self.uhvaceno_rect)
