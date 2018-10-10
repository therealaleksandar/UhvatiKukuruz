class Podesavanje:
    """Klasa gde se nalaze sva podesavanja za igru"""
    def __init__(self):

        #ekran podesavanja
        self.ekran_boja_pozadine=255,255,255
        self.ekran_visina=800
        self.ekran_sirina=800

        #kukuruz
        self.kukuruz_broj_propalih=3

        #rezultat
        self.rezultat_boja_fonta=(255,255,255)

        #ubrzanje
        self.ubrzanje_stepen=1.5

        #nivo stepen prebacivanja
        self.nivo_stepen=30

        #lokacija pozadine
        self.lokacija_slike='slike/pozadina.png'

        self.pocetne_vrednosti()

    def pocetne_vrednosti(self):
        """Postavlja pocetne vrednosti za parametre ispod"""
        #kukuruz
        self.kukuruz_brzina_spustanja=2.5
        #korpa
        self.korpa_brzina_kretanja=2.5

    def ubrzaj(self):
        self.kukuruz_brzina_spustanja*=self.ubrzanje_stepen
        self.korpa_brzina_kretanja*=self.ubrzanje_stepen
