class KavniAparat:
    def __init__(self):
        self.stanje = 0  # Začetno stanje vplačil

    def vnos_denarja(self, znesek):
        if znesek in [10, 20, 50, 1, 2]:
            self.stanje += znesek / 100  # Pretvorba v evre
            print(f"stanje: {self.stanje:.2f} EUR")
        else:
            print("Neveljaven znesek, vnos ignoriran.")

    def izberi_napitek(self, izbira):
        cene_napitkov = {'E': 1.5, 'C': 2.2, 'A': 1.8}
        if izbira in cene_napitkov:
            cena_napitka = cene_napitkov[izbira]
            if self.stanje >= cena_napitka:
                self.stanje -= cena_napitka
                print("Prosim, vzemite skodelico.")
            else:
                print("Stanje je prenizko!")
            print(f"stanje: {self.stanje:.2f} EUR")
        elif izbira == 'V':
            print(f"vzemite denar: {self.stanje:.2f} EUR")
            self.stanje = 0
        else:
            print("Neveljavna izbira, vnos ignoriran.")

# Ustvarjanje instance kavnega avtomata
avtomat = KavniAparat()

# Primeri uporabe
avtomat.vnos_denarja(50)
avtomat.vnos_denarja(50)
avtomat.vnos_denarja(50)
avtomat.vnos_denarja(1)
avtomat.izberi_napitek('E')
avtomat.vnos_denarja(1)
avtomat.izberi_napitek('V')