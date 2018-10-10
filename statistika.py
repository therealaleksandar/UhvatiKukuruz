from funkcije_igre import dobij_najbolji_rezultat

class Stats:
    """Klasa koja predstavlja statistiku igre"""
    def __init__(self,podesavanja):
        self.podesavanja=podesavanja
        self.resetuj_stats()

    def resetuj_stats(self):
        self.uhvaceni=0
        self.lista_uhvacenih=[0]
        self.propali=self.podesavanja.kukuruz_broj_propalih
        self.kukuruz_pada=False
        self.nivo=len(self.lista_uhvacenih)
        self.igra_aktivna=False
        self.najbolji_rezultat=dobij_najbolji_rezultat()
        self.pauza=False
