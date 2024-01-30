import functions

# functions.py
class MuscleRating:
    def __init__(self, rating, activation_percent):
        self.rating = rating
        self.activation_percent = activation_percent

class Muscle:
    def __init__(self, name):
        self.name = name
        self.ratings = []  # Lista per contenere gli oggetti MuscleRating

    def add_rating(self, rating, activation_percent):
        # Aggiunge un oggetto MuscleRating alla lista
        muscle_rating = MuscleRating(rating, activation_percent)
        self.ratings.append(muscle_rating)

    def calculate_weighted_average_rating(self):
        # Calcola la media ponderata dei ratings considerando le percentuali normalizzate
        if not self.ratings:
            return 0

        total_weighted_rating = sum(m.rating * (m.activation_percent / 100) / sum(r.activation_percent / 100 for r in self.ratings) for m in self.ratings)

        return total_weighted_rating

class Exercise:
    def __init__(self, name, elite_threshold, muscles_data):
        self.name = name
        self.elite_threshold = elite_threshold

        self.muscles = [Muscle(muscle) for muscle in muscles_data]

    def calculate_rating(self, bw, lifted_weight, n_reps):
        # Logica per calcolare il rating
        rating = functions.compute_rating(bw, lifted_weight, n_reps, self.name)

        # Applica il rating ai muscoli coinvolti
        for muscle in self.muscles:
            muscle_data = muscles_data.get(muscle.name, {})  # Dati specifici del muscolo nell'esercizio
            activation_percent = muscle_data.get('activation_percent', 100)  # Valore di default 100 se non specificato
            muscle.add_rating(rating, activation_percent)

        return rating, self.muscles

class Squat(Exercise):
    def __init__(self):
        # Specifica i dati per lo squat
        name = 'squat'
        elite_threshold = 232
        muscles_data = {'quads': 70, 'femorals': 15, 'glutes': 15}
        super().__init__(name, elite_threshold, muscles_data)

# Altre classi per gli esercizi possono essere definite in modo simile
class Deadlift(Exercise):
    def __init__(self):
        name = 'deadlift'
        elite_threshold = 265
        muscles_data = {'muscle1': 50, 'muscle2': 25, 'muscle3': 25}
        super().__init__(name, elite_threshold, muscles_data)
