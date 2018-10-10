import pygame

class Korpa:
    """Klasa koja predstavlja korpu kojom se hvata"""
    def __init__(self,ekran,podesavanja):
        self.ekran=ekran
        self.ekran_rect=self.ekran.get_rect()
        self.podesavanja=podesavanja

        #dodaj sliku i napravi rect
        self.slika=pygame.image.load('slike/korpa.png')
        self.rect=self.slika.get_rect()

        #podesi poziciju korpe na sredini i dnu ekrana
        self.rect.centerx=self.ekran_rect.centerx
        self.rect.bottom=self.ekran_rect.bottom

        #podesi pomeranje levo, desno na False
        self.pomeranje_ulevo=False
        self.pomeranje_udesno=False

        self.center=float(self.rect.centerx)

    def nacrtaj_korpu(self):
        """Funkcija koja crta korpu na ekranu"""
        self.ekran.blit(self.slika,self.rect)

    def azuriraj_kretanje(self):
        """Funkcija koja azurira kretanje korpe po ekranu"""
        if self.pomeranje_ulevo and self.rect.left>=self.ekran_rect.left:
            self.center-=self.podesavanja.korpa_brzina_kretanja
        if self.pomeranje_udesno and self.rect.right<=self.ekran_rect.right:
            self.center+=self.podesavanja.korpa_brzina_kretanja

        self.rect.centerx=self.center

    def centriraj(self):
        self.center=float(self.ekran_rect.centerx)
        self.rect.centerx=self.center