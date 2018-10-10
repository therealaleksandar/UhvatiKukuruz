import pygame
import sys
import funkcije_igre as fi

from podesavanja import Podesavanje
from korpa import Korpa
from kukuruz import Kukuruz
from pygame.sprite import Group
from statistika import Stats
from rezultat import Rezultat
from poruke import Poruke
from dugme import Dugme
from pozadina import Pozadina

pygame.init()

#pravljenje objekta podesavanja
podesavanja=Podesavanje()

#pravljenje ekrana (umetanje rezolucije i stavljanje naslova)
ekran=pygame.display.set_mode((podesavanja.ekran_sirina,podesavanja.ekran_visina))
pygame.display.set_caption("Uhvati Kukuruz")

#pravlejnje objekta korpa
korpa=Korpa(ekran,podesavanja)

#pravljenje grupe kukuruza
kukuruzi=Group()

#pravljenje objekta stats
stats=Stats(podesavanja)

#pravljenje objekta rezultat
rez=Rezultat(ekran,stats,podesavanja)

#pravljenje objekta por
por=Poruke(ekran,stats,podesavanja)

#pravljenje dugmeta igraj
dugme_igraj=Dugme(ekran,'Nova igra')

#pravlejnje dugmeta izlaz
dugme_izlaz=Dugme(ekran,'Izlaz')

#pravlejnje dugmeta izlaz
dugme_nastavi=Dugme(ekran,'Nastavi')

#pravljenje pozadine
pozadina=Pozadina(ekran,podesavanja.lokacija_slike)

#zvukovi
uhvacen_zvuk=pygame.mixer.Sound('zvukovi/uhvacen.wav')
propao_zvuk=pygame.mixer.Sound('zvukovi/propao.wav')
novi_nivo=pygame.mixer.Sound('zvukovi/novi_nivo.wav')
najbolji_rez=pygame.mixer.Sound('zvukovi/najbolji_rez.wav')

while True:

    fi.prati_desavanja(korpa,stats,dugme_igraj,dugme_izlaz,podesavanja,rez,kukuruzi)

    #ekran.fill(podesavanja.ekran_boja_pozadine)

    #postavljanje pozadine na ekranu
    pozadina.postavi()

    if stats.igra_aktivna:

        fi.proveri_nivo(stats,podesavanja,rez,novi_nivo)

        fi.napravi_kukuruz(kukuruzi,ekran,podesavanja,stats)
        
        fi.proveri_kukuruz_ekran(kukuruzi,stats,rez,propao_zvuk)

        fi.proveri_kontakt_korpe_kukuruza(korpa,kukuruzi,stats,rez,uhvacen_zvuk)
    
    else:
        fi.nacrtaj_dugmad(dugme_igraj,dugme_izlaz,dugme_nastavi,stats)
           
    fi.azuriraj_ekran(korpa,ekran,podesavanja,kukuruzi,rez,por,stats,najbolji_rez)
