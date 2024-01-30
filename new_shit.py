import functions


class Muscolo:
    def __init__(self, nome, rating, percentuale_coinvolgimento):
        self.nome = nome
        self.rating = rating
        self.percentuale_coinvolgimento = percentuale_coinvolgimento

    def __str__(self):
        return f"Muscolo: {self.nome}, Rating: {self.rating}, Percentuale: {self.percentuale_coinvolgimento}%"


class ListaMuscoli:
    def __init__(self):
        self.muscoli = []

    def aggiungi_muscolo(self, muscolo):
        self.muscoli.append(muscolo)

    def rimuovi_muscolo(self, muscolo):
        self.muscoli.remove(muscolo)

    def calcola_media_ponderata(self, nome_muscolo):
        muscoli_coinvolti = [muscolo for muscolo in self.muscoli if muscolo.nome == nome_muscolo]

        if not muscoli_coinvolti:
            print(f"Nessun muscolo con il nome '{nome_muscolo}' trovato.")
            return None

        total_percentuale = sum(muscolo.percentuale_coinvolgimento for muscolo in muscoli_coinvolti)
        total = []

        for muscolo in muscoli_coinvolti:
            perc_normalizzata = muscolo.percentuale_coinvolgimento / total_percentuale
            rating_normalizzato = muscolo.rating * perc_normalizzata
            total.append(rating_normalizzato)

        media_ponderata = sum(total)

        '''
        print(f"Muscoli coinvolti: {muscoli_coinvolti}")
        print(f"Total percentuale: {total_percentuale}")
        print(f"Total: {total}")
        print(f"Media ponderata per '{nome_muscolo}': {media_ponderata}")
        '''

        return media_ponderata


class Persona:
    def __init__(self, peso, sesso, eta):
        self.peso = peso
        self.sesso = sesso
        self.eta = eta
        self.muscoli_coinvolti = ListaMuscoli()

    def calcola_rating(self):
        # Implementazione del calcolo del rating per tutti i muscoli coinvolti
        pass

    def converti_a_lettera(self, rating):
        # Definisci i range e le relative lettere
        intervalli = [
            (100, 'ELITE'), (95, 'S'), (90, 'S-'),
            (85, 'A+'), (80, 'A'), (75, 'A-'),
            (70, 'B+'), (65, 'B'), (60, 'B-'),
            (55, 'C+'), (50, 'C'), (45, 'C-'),
            (40, 'D+'), (35, 'D'), (30, 'D-'),
            (0, 'NULL')
        ]

        # Trova la lettera corrispondente al rating
        for limite, lettera in intervalli:
            if rating >= limite:
                return lettera

    def print_rating(self):
        muscoli_per_nome = {}

        # Raggruppa gli oggetti Muscolo per nome
        for muscolo in self.muscoli_coinvolti.muscoli:
            if muscolo.nome not in muscoli_per_nome:
                muscoli_per_nome[muscolo.nome] = []
            muscoli_per_nome[muscolo.nome].append(muscolo)

        # Calcola e stampa la media ponderata per ogni nome di muscolo
        for nome_muscolo, muscoli in muscoli_per_nome.items():
            media_ponderata = self.muscoli_coinvolti.calcola_media_ponderata(nome_muscolo)
            lettera = self.converti_a_lettera(media_ponderata)
            print(f"Rating per '{nome_muscolo}': {media_ponderata} ({lettera})")

def squat(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 232
    percentuale_quad = 60
    percentuale_femorali = 15
    percentuale_glutei = 15
    percentuale_addome = 5
    percentuale_lombari = 5

    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, rating, percentuale in [("Quadricipiti", rating, percentuale_quad),
                                              ("Femorali", rating, percentuale_femorali),
                                              ("Glutei", rating, percentuale_glutei),
                                              ("Addome", rating, percentuale_addome),
                                              ("Lombari", rating, percentuale_lombari)]:
        muscolo = Muscolo(nome_muscolo, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def deadlift(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 265
    percentuale_quad = 15
    percentuale_femorali = 20
    percentuale_glutei = 25
    percentuale_addome = 5
    percentuale_lombari = 35

    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, rating, percentuale in [("Quadricipiti", rating, percentuale_quad),
                                              ("Femorali", rating, percentuale_femorali),
                                              ("Glutei", rating, percentuale_glutei),
                                              ("Addome", rating, percentuale_addome),
                                              ("Lombari", rating, percentuale_lombari)]:
        muscolo = Muscolo(nome_muscolo, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def bench_press(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 177.6
    percentuale_petto = 65
    percentuale_delt_front = 15
    percentuale_delt_centrale = 10
    percentuale_tricipiti = 10


    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, rating, percentuale in [("Petto", rating, percentuale_petto),
                                              ("Deltoide Frontale", rating, percentuale_delt_front),
                                              ("Deltoide Centrale", rating, percentuale_delt_centrale),
                                              ("Tricipiti", rating, percentuale_tricipiti)]:
        muscolo = Muscolo(nome_muscolo, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def military_press(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 115.4
    percentuale_delt_front = 60
    percentuale_delt_centrale = 20
    percentuale_tricipiti = 20


    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, rating, percentuale in [("Deltoide Frontale", rating, percentuale_delt_front),
                                              ("Deltoide Centrale", rating, percentuale_delt_centrale),
                                              ("Tricipiti", rating, percentuale_tricipiti)]:
        muscolo = Muscolo(nome_muscolo, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)



bw = 68
fabio = Persona(bw, "Maschio", 25)

print("Dopo la creazione di Persona:")
print(f"Muscoli coinvolti in fabio: {[str(muscolo) for muscolo in fabio.muscoli_coinvolti.muscoli]}")

squat(bw, 6, 130, fabio)
print("\nDopo la funzione squat:")
print(f"Muscoli coinvolti in fabio: {[str(muscolo) for muscolo in fabio.muscoli_coinvolti.muscoli]}\n")

fabio.print_rating()

deadlift(bw, 1, 160, fabio)
print("\nDopo la funzione deadlift:")
print(f"Muscoli coinvolti in fabio: {[str(muscolo) for muscolo in fabio.muscoli_coinvolti.muscoli]}\n")

fabio.print_rating()

bench_press(bw, 6, 72.5, fabio)
print("\nDopo la funzione bench_press:")
print(f"Muscoli coinvolti in fabio: {[str(muscolo) for muscolo in fabio.muscoli_coinvolti.muscoli]}\n")

fabio.print_rating()

military_press(bw, 12, 38, fabio)
print("\nDopo la funzione military_press:")
print(f"Muscoli coinvolti in fabio: {[str(muscolo) for muscolo in fabio.muscoli_coinvolti.muscoli]}\n")

fabio.print_rating()