import functions
from statistics import mean

# male only for now

#def squat (bw, lifted_weight, n_reps):

#    elite_threshold_male = 232
#    rating = functions.compute_data(bw, lifted_weight, n_reps, elite_threshold_male)

elite_threshold = {
    'squat': 232,
    'deadlift': 265,
    'bench_press':177.6,
    'military_press':115.4,
    'pull_ups':191,
    'dumbbell_curl':59.5,
    'push_ups': 360,
    'sled_leg_press': 452,
    'dumbbell_shoulder_press':66,
    'bent_over_row':159,
    'incline_bench_press':157,
    'dumbbell_incline_bench_press':74,
    'dips':223,
    'lat_pulldown':158,
    'dumbbell_lateral_raise':41,
    'leg_extension':210.5,
    'romanian_deadlift':228,
    'dumbbell_row':91,
    'tricep_cable_pushdown':108.5,
    'seated_cable_row':160,
    'EZ_bar_curl':90.5,
    'seated_leg_curl':168,
    'barbell_shrug':271,
    'cable_bicep':130
    }


class Muscolo:
    def __init__(self, nome, categoria, rating, percentuale_coinvolgimento):
        self.nome = nome
        self.categoria = categoria
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
            (25, 'E+'), (20, 'E'), (15, 'E-'),
            (0, 'NULL')
        ]

        # Trova la lettera corrispondente al rating
        for limite, lettera in intervalli:
            if rating >= limite:
                return lettera

    '''
    # OLD CODE
    
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
    '''

    def print_rating(self):
        categorie_muscoli = set(muscolo.categoria for muscolo in self.muscoli_coinvolti.muscoli)

        media_tot = []

        for categoria in categorie_muscoli:
            muscoli_categoria = [muscolo for muscolo in self.muscoli_coinvolti.muscoli if
                                 muscolo.categoria == categoria]

            # Stampa la categoria
            print(f"\nCategoria: {categoria}")

            muscoli_per_nome = {}

            # Raggruppa gli oggetti Muscolo per nome nella categoria attuale
            for muscolo in muscoli_categoria:
                if muscolo.nome not in muscoli_per_nome:
                    muscoli_per_nome[muscolo.nome] = []
                muscoli_per_nome[muscolo.nome].append(muscolo)

            # Calcola e stampa la media ponderata per ogni nome di muscolo

            media_categoria = []


            for nome_muscolo, muscoli in muscoli_per_nome.items():
                media_ponderata = self.muscoli_coinvolti.calcola_media_ponderata(nome_muscolo)
                media_categoria.append(media_ponderata)
                lettera = self.converti_a_lettera(media_ponderata)
                print(f"  Rating per '{nome_muscolo}': {media_ponderata:.1f} ({lettera})")

            lettera_media = self.converti_a_lettera(mean(media_categoria))
            print(f"Media categoria: {mean(media_categoria):.1f} ({lettera_media})")
            media_tot.append(mean(media_categoria))

        lettera_tot = self.converti_a_lettera(mean(media_tot))
        print(f"\nOverall: {mean(media_tot):.1f} ({lettera_tot})")


def squat(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 232
    percentuale_quad = 60
    percentuale_femorali = 15
    percentuale_glutei = 15
    percentuale_addome = 5
    percentuale_lombari = 5

    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, categoria, rating, percentuale in [("Quadricipiti", "Gambe", rating, percentuale_quad),
                                              ("Femorali", "Gambe", rating, percentuale_femorali),
                                              ("Glutei", "Gambe", rating, percentuale_glutei),
                                              ("Addome", "Petto e Addome", rating, percentuale_addome),
                                              ("Lombari", "Schiena", rating, percentuale_lombari)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def deadlift(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 265
    percentuale_quad = 15
    percentuale_femorali = 20
    percentuale_glutei = 25
    percentuale_addome = 5
    percentuale_lombari = 35

    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, categoria, rating, percentuale in [("Quadricipiti", "Gambe", rating, percentuale_quad),
                                              ("Femorali", "Gambe", rating, percentuale_femorali),
                                              ("Glutei", "Gambe", rating, percentuale_glutei),
                                              ("Addome", "Petto e Addome", rating, percentuale_addome),
                                              ("Lombari", "Schiena",  rating, percentuale_lombari)]:
        muscolo = Muscolo(nome_muscolo,  categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def bench_press(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 177.6
    percentuale_petto = 65
    percentuale_delt_front = 15
    percentuale_delt_centrale = 10
    percentuale_tricipiti = 10


    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, categoria, rating, percentuale in [("Petto", "Petto e Addome", rating, percentuale_petto),
                                              ("Deltoide Frontale", "Spalle", rating, percentuale_delt_front),
                                              ("Deltoide Centrale", "Spalle", rating, percentuale_delt_centrale),
                                              ("Tricipiti", "Braccia", rating, percentuale_tricipiti)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def military_press(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 115.4
    percentuale_delt_front = 60
    percentuale_delt_centrale = 20
    percentuale_tricipiti = 20


    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, categoria, rating, percentuale in [("Deltoide Frontale", "Spalle", rating, percentuale_delt_front),
                                              ("Deltoide Centrale", "Spalle", rating, percentuale_delt_centrale),
                                              ("Tricipiti","Braccia", rating, percentuale_tricipiti)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def pull_ups(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 191
    percentuale_dorsali = 60
    percentuale_trapezio = 20
    percentuale_bicipiti = 15
    percentuale_romboidi= 5


    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, categoria, rating, percentuale in [("Dorsali", "Schiena", rating, percentuale_dorsali),
                                              ("Trapezio",  "Schiena",rating, percentuale_trapezio),
                                              ("Bicipiti", "Braccia", rating, percentuale_bicipiti),
                                              ("Romboidi", "Schiena", rating, percentuale_romboidi)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def dumbell_curl(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 59.5
    percentuale_bicipiti = 100

    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, categoria, rating, percentuale in [("Bicipiti","Braccia", rating, percentuale_bicipiti)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def push_ups(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 360
    percentuale_petto = 60
    percentuale_delt_front = 25
    percentuale_tricipiti = 15

    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, categoria, rating, percentuale in [("Deltoide Frontale", "Spalle", rating, percentuale_delt_front),
                                              ("Petto", "Petto e Addome", rating, percentuale_petto),
                                              ("Tricipiti","Braccia", rating, percentuale_tricipiti)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def dips(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 223
    percentuale_petto = 35
    percentuale_tricipiti = 65


    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, categoria, rating, percentuale in [("Petto","Petto e Addome", rating, percentuale_petto),
                                              ("Tricipiti","Braccia", rating, percentuale_tricipiti)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def lat_pulldown(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 158
    percentuale_dorsali = 60
    percentuale_trapezio = 15
    percentuale_bicipiti = 20
    percentuale_romboidi = 5


    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, categoria, rating, percentuale in [("Dorsali", "Schiena", rating, percentuale_dorsali),
                                              ("Trapezio", "Schiena", rating, percentuale_trapezio),
                                              ("Bicipiti", "Braccia",rating, percentuale_bicipiti),
                                              ("Romboidi", "Schiena", rating, percentuale_romboidi)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def dumbbell_lateral_raise(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 41
    percentuale_delt_front = 5
    percentuale_delt_centrale = 90
    percentuale_delt_posteriori = 5

    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, categoria, rating, percentuale in [("Deltoide Frontale", "Spalle", rating, percentuale_delt_front),
                                              ("Deltoide Centrale", "Spalle", rating, percentuale_delt_centrale),
                                              ("Deltoide Posteriore", "Spalle", rating, percentuale_delt_posteriori)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def tricep_cable_pushdown(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 108.5
    percentuale_tricipiti = 100


    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, categoria, rating, percentuale in [("Tricipiti","Braccia", rating, percentuale_tricipiti)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)

def cable_bicep(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 130
    percentuale_bicipiti = 100

    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo, categoria, rating, percentuale in [("Bicipiti","Braccia", rating, percentuale_bicipiti)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)

def barbell_shrug(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 271
    percentuale_delt_centrali = 10
    percentuale_trapezio = 80
    percentuale_romboidi= 10

    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo,  categoria,rating, percentuale in [("Trapezio", "Schiena", rating, percentuale_trapezio),
                                              ("Deltoide Centrale", "Spalle", rating, percentuale_delt_centrali),
                                              ("Romboidi", "Schiena", rating, percentuale_romboidi)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def decline_sit_ups(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 395
    percentuale_addome = 100

    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo,  categoria,rating, percentuale in [("Addome", "Petto e Addome", rating, percentuale_addome)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)


def machine_back_extension(peso, num_ripetizioni, peso_sollevato, persona):
    elite_threshold = 240
    percentuale_lombari = 85
    percentuale_glutei = 7.5
    percentuale_femorali = 7.5

    rating = functions.compute_rating(peso, peso_sollevato, num_ripetizioni, elite_threshold)

    for nome_muscolo,  categoria,rating, percentuale in [("Lombari", "Schiena", rating, percentuale_lombari),
                                                         ("Glutei", "Gambe", rating, percentuale_glutei),
                                                         ("Femorali", "Gambe", rating, percentuale_femorali)]:
        muscolo = Muscolo(nome_muscolo, categoria, rating, percentuale)
        persona.muscoli_coinvolti.aggiungi_muscolo(muscolo)






