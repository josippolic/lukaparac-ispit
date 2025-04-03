class Vozilo:
    def __init__(self, proizvodac, masa, udaljenost):
        self.proizvodac = proizvodac
        self.masa = masa
        self.udaljenost = udaljenost
    
    def trosak_prijevoza(self):
        return 0.05 * self.masa * self.udaljenost * 0.3

class Dostava(Vozilo):
    def trosak_osiguranja(self):
        return 225 + 0.02 * self.masa

def ispis_troskova(dostave):
    print("| Proizvođač | Masa  | Udaljenost | Trošak prijevoza | Premija | Ukupni trošak |")
    print("-" * 80)
    for d in dostave:
        trosak = d.trosak_prijevoza()
        premija = d.trosak_osiguranja()
        ukupno = trosak + premija
        print(f"| {d.proizvodac:10} | {d.masa:4}kg | {d.udaljenost:10}km | {trosak:15.1f} | {premija:7.1f} | {ukupno:13.1f} |")

def zadatak2():
    kombi1 = Dostava("Ford", 700, 300)
    kombi2 = Dostava("Mercedes", 800, 400)
    kombi3 = Dostava("Iveco", 750, 350)
    ispis_troskova([kombi1, kombi2, kombi3])

# Pokretanje programa
zadatak2()
