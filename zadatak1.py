import random

# Zadatak 1
# Program bira slučajni broj u intervalu [1, 50] i korisnik ima 10 pokušaja da ga pogodi.

def zadatak1():
    broj = random.randint(1, 50)  # Generiranje slučajnog broja
    pokusaji = 10  # Maksimalan broj pokušaja
    
    for i in range(1, pokusaji + 1):
        try:
            unos = int(input(f"Pokušaj {i}/{pokusaji} - Unesite broj: "))
        except ValueError:
            print("Molimo unesite ispravan cijeli broj!")
            continue
        
        if unos > broj:
            print("Upisani broj je veći od traženog.")
        elif unos < broj:
            print("Upisani broj je manji od traženog.")
        else:
            print(f"Pogodak! Broj pokušaja: {i}")
            return
    
    print("Žao mi je, više sreće drugi put!")

# Pokretanje programa
zadatak1()
