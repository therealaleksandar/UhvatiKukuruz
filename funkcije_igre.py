import pygame
import sys
import json

from kukuruz import Kukuruz
from rezultat import Rezultat
from time import sleep

def prati_desavanja(korpa,stats,dugme_igraj,dugme_izlaz,podesavanja,rez,kukuruzi):
    """Funkcija koja prati pritiskanje tastature"""
    for dogadjaj in pygame.event.get():
        if dogadjaj.type==pygame.QUIT:
            sys.exit(0)
        elif dogadjaj.type==pygame.KEYDOWN:
            key_down(dogadjaj,korpa,stats,podesavanja,rez,kukuruzi)
        elif dogadjaj.type==pygame.KEYUP:
            key_up(dogadjaj,korpa)
        elif dogadjaj.type==pygame.MOUSEBUTTONDOWN:
            mis_x,mis_y=pygame.mouse.get_pos()
            proveri_dugme_igraj(dugme_igraj,stats,mis_x,mis_y,podesavanja,rez,kukuruzi,korpa)
            proveri_dugme_izlaz(stats,dugme_izlaz,dugme_igraj,mis_x,mis_y)
            proveri_dugme_nastavi(stats,dugme_izlaz,dugme_igraj,mis_x,mis_y)

def key_down(dogadjaj,korpa,stats,podesavanja,rez,kukuruzi):
    if dogadjaj.key==pygame.K_q:
        sys.exit(0)
    elif dogadjaj.key==pygame.K_LEFT:
        if not stats.pauza:
            korpa.pomeranje_ulevo=True
    elif dogadjaj.key==pygame.K_RIGHT:
        if not stats.pauza:
            korpa.pomeranje_udesno=True
    elif dogadjaj.key==pygame.K_n:
        if not stats.igra_aktivna:
            pocni_igru(stats,podesavanja,rez,kukuruzi,korpa)
    elif dogadjaj.key==pygame.K_SPACE:
        if stats.igra_aktivna:
            pauza(stats)
        elif stats.pauza:
            nastavi_igru(stats)

def key_up(dogadjaj,korpa):
    if dogadjaj.key==pygame.K_LEFT:
        korpa.pomeranje_ulevo=False
    elif dogadjaj.key==pygame.K_RIGHT:
        korpa.pomeranje_udesno=False

def proveri_dugme_igraj(dugme_igraj,stats,mis_x,mis_y,podesavanja,rez,kukuruzi,korpa):
    """Proverava da li je dugme pritisnuto i aktivira igru ako jeste"""
    dugme_igraj_pritisnuto=dugme_igraj.rect.collidepoint(mis_x,mis_y)
    if dugme_igraj_pritisnuto and not stats.igra_aktivna:
        pocni_igru(stats,podesavanja,rez,kukuruzi,korpa)

def pocni_igru(stats,podesavanja,rez,kukuruzi,korpa):
    resetovanje(stats,podesavanja,rez)
    stats.igra_aktivna=True
    kukuruzi.empty()
    pygame.mouse.set_visible(False)
    korpa.centriraj()

def podesi_poziciju_dugme_izlaz(dugme_igraj,dugme_izlaz):
    dugme_izlaz.rect.top=dugme_igraj.rect.bottom+10

def proveri_dugme_izlaz(stats,dugme_izlaz,dugme_igraj,mis_x,mis_y):
    podesi_poziciju_dugme_izlaz(dugme_igraj,dugme_izlaz)
    """Proverava da li je dugme pritisnuto i izlazi iz igre ako jeste"""
    dugme_izlaz_pritisnuto=dugme_izlaz.rect.collidepoint(mis_x,mis_y)
    if dugme_izlaz_pritisnuto and not stats.igra_aktivna:
        sys.exit(0)

def podesi_poziciju_dugme_nastavi(dugme_igraj,dugme_nastavi):
    dugme_nastavi.rect.bottom=dugme_igraj.rect.top-10

def proveri_dugme_nastavi(stats,dugme_nastavi,dugme_igraj,mis_x,mis_y):
    podesi_poziciju_dugme_nastavi(dugme_igraj,dugme_nastavi)
    """Proverava da li je dugme pritisnuto i nastavlja sa igrom ako jeste"""
    dugme_nastavi_pritisnuto=dugme_nastavi.rect.collidepoint(mis_x,mis_y)
    if dugme_nastavi_pritisnuto and not stats.igra_aktivna:
        nastavi_igru(stats)

def nastavi_igru(stats):
    stats.igra_aktivna=True
    pygame.mouse.set_visible(False)
    stats.kukuruz_pada=True
    stats.pauza=False

def pauza(stats):
    stats.igra_aktivna=False
    pygame.mouse.set_visible(True)
    stats.kukuruz_pada=False
    stats.pauza=True

def nacrtaj_dugmad(dugme_igraj,dugme_izlaz,dugme_nastavi,stats):
    dugme_igraj.nacrtaj_dugme()
    podesi_poziciju_dugme_izlaz(dugme_igraj,dugme_izlaz)
    dugme_izlaz.nacrtaj_dugme()
    if stats.pauza:
        podesi_poziciju_dugme_nastavi(dugme_igraj,dugme_nastavi)
        dugme_nastavi.nacrtaj_dugme()

def napravi_kukuruz(kukuruzi,ekran,podesavanja,stats):
    """Funkcija koja pravi kukuruz ako ga nema"""
    if len(kukuruzi)==0:
        kukuruz=Kukuruz(ekran,podesavanja,stats)
        kukuruzi.add(kukuruz)
        stats.kukuruz_pada=True

def proveri_kukuruz_ekran(kukuruzi,stats,rez,propao_zvuk):
    """Funkcija koja proverava da li je kukuruz na ekranu i uklanja ako nije"""
    for kukuruz in kukuruzi.copy():
        if kukuruz.rect.top>=kukuruz.ekran_rect.bottom:
            pygame.mixer.Sound.play(propao_zvuk)
            kukuruzi.remove(kukuruz)
            stats.kukuruz_pada=False
            stats.propali-=1
            rez.pripremi_propale_kukuruze()

def proveri_kontakt_korpe_kukuruza(korpa,kukuruzi,stats,rez,uhvacen_zvuk):
    """Fukncija koja proverava kontakt izmedju korpe i kukuruza"""
    kontakt=pygame.sprite.spritecollide(korpa,kukuruzi,True)
    if kontakt:
        pygame.mixer.Sound.play(uhvacen_zvuk)
        stats.kukuruz_pada=False
        stats.uhvaceni+=1
        rez.pripremi_rezultat()

def proveri_nivo(stats,podesavanja,rez,novi_nivo):
    """Funkcija koja proverava da li treba da se promeni nivo, i ubrzava igru ako treba"""
    if stats.uhvaceni not in stats.lista_uhvacenih and stats.uhvaceni%podesavanja.nivo_stepen==0 and not stats.kukuruz_pada:
        pygame.mixer.Sound.play(novi_nivo)
        stats.lista_uhvacenih.append(stats.uhvaceni)
        stats.nivo=len(stats.lista_uhvacenih)
        podesavanja.ubrzaj()
        rez.pripremi_nivo()

def dobij_najbolji_rezultat():
    with open('naj_rez.json') as fajl:
        return json.load(fajl)

def sacuvaj_najbolji_rezultat(stats):
    with open('naj_rez.json',mode='w') as fajl:
        json.dump(stats.uhvaceni,fajl)

def proveri_najbolji_rez(stats,rez):
    """Funkcija koja proverava i preprema najboji rezultat"""
    if stats.uhvaceni>stats.najbolji_rezultat:
        sacuvaj_najbolji_rezultat(stats)
        rez.pripremi_najbolji_rez()
        return True

def pripremi_poruke(por,stats,rez,najbolji_rez):
    #pripremi poruku koja prikazuje koliko je uhvaceno
    por.pripremi_uhvatili_ste()

    #proveri najbolji rezultat i postavi ga ako je trenutni veci
    if proveri_najbolji_rez(stats,rez):
        #prikazi poruku novi najbolji rez
        por.blit_novi_naj()
        pygame.mixer.Sound.play(najbolji_rez)
    else:
        #prikazi poruku
        por.blit_kraj()

def resetovanje(stats,podesavanja,rez):
    #reset statistike i ubrzanja
    stats.resetuj_stats()
    podesavanja.pocetne_vrednosti()

    #reset rezultata
    rez.pripremi_nivo()
    rez.pripremi_propale_kukuruze()
    rez.pripremi_rezultat()
    rez.pripremi_najbolji_rez()

def proveri_kraj(stats,rez,por,podesavanja,najbolji_rez):
    if stats.propali<0:
        
        pripremi_poruke(por,stats,rez,najbolji_rez)

        #osvezenje ekrana i pauza od 3 sekunde
        pygame.display.flip()
        sleep(3)

        resetovanje(stats,podesavanja,rez)

        #vrati misa na ekran
        pygame.mouse.set_visible(True)

def azuriraj_ekran(korpa,ekran,podesavanja,kukuruzi,rez,por,stats,najbolji_rez):
    """Funkcija koja azurira ekran"""
    proveri_kraj(stats,rez,por,podesavanja,najbolji_rez)

    korpa.nacrtaj_korpu()

    korpa.azuriraj_kretanje()    
    
    kukuruzi.draw(ekran)

    kukuruzi.update() 

    rez.prikazi_rezultat()

    pygame.display.flip()
