"""
Simulazione di produzione di componenti elettronici
(schede madri, batterie e schermi)
--------------------------------------------------
Questo programma in Python genera una simulazione
realistica della capacità produttiva di un’azienda
specializzata in elettronica, stimando quantità da
produrre, tempi e giorni necessari.
I risultati vengono stampati a schermo e salvati
in formato CSV per ulteriori analisi.
"""

import random
import csv

# Lista dei prodotti oggetto della simulazione
prodotti = ["Scheda Madre", "Batteria", "Schermo"]

# ==============================
# Funzione di utilità per formattare i tempi
# ==============================
def formatta_ore_minuti(ore_decimali):
    ore = int(ore_decimali)                # parte intera delle ore
    minuti = int((ore_decimali - ore) * 60)  # parte frazionaria convertita in minuti
    if ore == 0 and minuti == 0:
        return "meno di 1 minuto"
    elif ore == 0:
        return f"{minuti} min"
    elif minuti == 0:
        return f"{ore} h"
    else:
        return f"{ore} h {minuti} min"

# ==============================
# Funzione 1: Genera quantità da produrre per ogni prodotto
# ==============================
def genera_quantita_prodotti():
    quantita = {}
    for prodotto in prodotti:
        q = random.randint(50000, 100000)   # quantità simulata (es. ordine cliente)
        if q <= 0:
            q = 50000
        quantita[prodotto] = q
    return quantita

# ==============================
# Funzione 2: Genera parametri di produzione (tempi medi e capacità giornaliera)
# ==============================
def genera_parametri_produzione():
    # Tempo medio per produrre una singola unità (in ore decimali)
    tempo_produzione = {
        "Scheda Madre": random.uniform(1.0, 2.0),
        "Batteria": random.uniform(0.3, 0.6),
        "Schermo": random.uniform(0.8, 1.2)
    }

    # Capacità produttiva giornaliera stimata (unità/giorno)
    capacita_giornaliera = {
        "Scheda Madre": random.randint(10000, 20000),
        "Batteria": random.randint(200000, 500000),
        "Schermo": random.randint(150000, 300000)
    }

    return tempo_produzione, capacita_giornaliera

# ==============================
# Funzione 3: Calcola tempi complessivi di produzione
# ==============================
def calcola_tempo_produzione(quantita, tempo_produzione, capacita_giornaliera):
    tempo_totale = 0
    dettagli = {}

    for prodotto in prodotti:
        quantita_da_produrre = quantita[prodotto]
        tempo_per_unita = tempo_produzione[prodotto]
        capacita_max = capacita_giornaliera[prodotto]

        # Stima di giorni e ore necessarie
        giorni_necessari = quantita_da_produrre / capacita_max
        ore_necessarie = quantita_da_produrre * tempo_per_unita

        tempo_totale += ore_necessarie

        dettagli[prodotto] = {
            "quantita": quantita_da_produrre,
            "tempo_unitario": tempo_per_unita,
            "capacita_giornaliera": capacita_max,
            "giorni": round(giorni_necessari, 2),
            "ore": ore_necessarie
        }

    return tempo_totale, dettagli

# ==============================
# Funzione 4: Simulazione completa della produzione
# ==============================
def simula_produzione():
    # Generazione dati di simulazione
    quantita = genera_quantita_prodotti()
    tempo_produzione, capacita_giornaliera = genera_parametri_produzione()
    tempo_totale, dettagli = calcola_tempo_produzione(
        quantita, tempo_produzione, capacita_giornaliera
    )

    capacita_totale = sum(capacita_giornaliera.values())

    # Stampa dei risultati a schermo
    print("\n=== RISULTATI DELLA SIMULAZIONE ===\n")
    for prodotto, info in dettagli.items():
        print(f"- {prodotto.upper()}:")
        print(f"  Quantità da produrre: {info['quantita']} unità")
        print(f"  Tempo unitario medio: {formatta_ore_minuti(info['tempo_unitario'])}")
        print(f"  Capacità giornaliera: {info['capacita_giornaliera']} unità/giorno")
        print(f"  Giorni stimati: {info['giorni']}")
        print(f"  Tempo totale stimato: {formatta_ore_minuti(info['ore'])}\n")

    print(f"Capacità produttiva complessiva: {capacita_totale} unità/giorno")
    print(f"Tempo complessivo stimato: {formatta_ore_minuti(tempo_totale)}")

    # Salvataggio dei risultati in un file CSV
    with open("risultati_simulazione.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Prodotto", "Quantità", "Tempo unitario", "Capacità giornaliera",
            "Giorni stimati", "Tempo totale stimato"
        ])
        for prodotto, info in dettagli.items():
            writer.writerow([
                prodotto, info['quantita'],
                formatta_ore_minuti(info['tempo_unitario']),
                info['capacita_giornaliera'], info['giorni'],
                formatta_ore_minuti(info['ore'])
            ])

        # Riga riepilogativa finale
        writer.writerow([])
        writer.writerow(["Capacità produttiva complessiva", capacita_totale])
        writer.writerow(["Tempo complessivo stimato", formatta_ore_minuti(tempo_totale)])

    print("\nI risultati sono stati salvati in 'risultati_simulazione.csv'")

# ==============================
# Esecuzione del programma
# ==============================
if __name__ == "__main__":
    simula_produzione()
