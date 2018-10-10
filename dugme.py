import pygame.font

class Dugme:

    def __init__(self,ekran,poruka):
        self.ekran=ekran
        self.ekran_rect=self.ekran.get_rect()

        #Postavi dimenzije i funkcije dugmeta
        self.sirina,self.visina=150,40
        self.boja_dugmeta=(0,0,0)
        self.boja_teksta=(255,255,255)
        self.font=pygame.font.SysFont(None,42)

        #Napravi dugme rect i centriraj ga
        self.rect=pygame.Rect(0,0,self.sirina,self.visina)
        self.rect.center=self.ekran_rect.center

        self.poruka=poruka

        self.nacrtaj_dugme()

    def nacrtaj_dugme(self):
        """Crta dugme sa tekstom na ekranu"""
        self.poruka_slika=self.font.render(self.poruka,True,self.boja_teksta,self.boja_dugmeta)
        self.poruka_slika_rect=self.poruka_slika.get_rect()
        self.poruka_slika_rect.center=self.rect.center

        #Nacrtaj prazno dugme i dodaj poruku
        self.ekran.fill(self.boja_dugmeta,self.rect)
        self.ekran.blit(self.poruka_slika,self.poruka_slika_rect)
