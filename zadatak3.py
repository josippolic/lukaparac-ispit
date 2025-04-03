import sqlite3

def kreiraj_bazu():
    conn = sqlite3.connect("vozni_park.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vozila (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proizvodac TEXT NOT NULL,
            godina_proizvodnje INTEGER NOT NULL,
            prijedeni_km INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def dodaj_podatke():
    conn = sqlite3.connect("vozni_park.db")
    cursor = conn.cursor()
    vozila = [
        ("Ford", 2005, 250000),
        ("Mercedes", 2010, 180000),
        ("Toyota", 2000, 300000),
        ("BMW", 2015, 120000)
    ]
    cursor.executemany("INSERT INTO vozila (proizvodac, godina_proizvodnje, prijedeni_km) VALUES (?, ?, ?)", vozila)
    conn.commit()
    conn.close()

def zadatak3():
    conn = sqlite3.connect("vozni_park.db")
    cursor = conn.cursor()
    cursor.execute("SELECT proizvodac, godina_proizvodnje, prijedeni_km FROM vozila ORDER BY godina_proizvodnje ASC LIMIT 1")
    najstarije = cursor.fetchone()
    if najstarije:
        proizvodac, godina, kilometri = najstarije
        prosjecna_god_km = kilometri / (2025 - godina)
        print(f"Najstarije vozilo: {proizvodac}, Godina: {godina}, Prosječna godišnja kilometraža: {prosjecna_god_km:.2f} km")
    else:
        print("Nema podataka u bazi.")
    conn.close()

# Kreiranje baze i dodavanje podataka
kreiraj_bazu()
dodaj_podatke()

# Pokretanje programa
zadatak3()
