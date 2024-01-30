import exercises

def compute_max(n_rep, lifted_weight):
    """
    Calcola il massimale utilizzando la formula di Epley.

    :param n_rep: Numero di ripetizioni
    :param lifted_weight: Peso sollevato
    :return: Massimale stimato
    """
    # Coefficienti della formula di Epley
    a, b = 1, 0.0333

    if n_rep == 1:
        return lifted_weight
    else:
        # Calcolo del massimale
        max_estimate = lifted_weight * (1 + b * n_rep)

    return max_estimate



def compute_wilks(bw, max_estimate, is_male=True):
    """
    Calcola il punteggio Wilks.

    :param bw: Peso corporeo in kg
    :param max_estimate: Massimale stimato
    :param is_female: True se l'atleta è una donna, False altrimenti
    :return: Punteggio Wilks
    """
    # Coefficienti per uomo e donna
    if is_male:
        a, b, c, d, e, f = -216.0475144, 16.2606339, -0.002388645, -0.00113732, 7.01863e-06, -1.291e-08
    else:
        a, b, c, d, e, f = 594.31747775582, -27.23842536447, 0.82112226871, -0.00930733913, 4.731582e-05, -9.054e-08

    # Calcolo del punteggio Wilks
    wilks_score = max_estimate * 500 / (a + b * bw + c * bw**2 + d * bw**3 + e * bw**4 + f * bw**5)

    return wilks_score


def compute_wilks_2020(bw, max_estimate, is_male=True):
    """
    Calcola il punteggio Wilks utilizzando la formula aggiornata del 2020.

    :param bw: Peso corporeo in kg
    :param max_estimate: Massimale stimato
    :param is_female: True se l'atleta è una donna, False altrimenti
    :return: Punteggio Wilks
    """
    # Coefficienti per uomo e donna
    if is_male:
        a, b, c, d, e, f = -125.4255398, 13.71219419, -0.03307250631, -0.001050400051, 9.38773881462799e-6, -2.3334613884954e-8
    else:
        a, b, c, d, e, f = 47.46178854, 8.472061379, 0.07369410346, -0.001395833811, 7.07665973070743e-6, -1.20804336482315e-8

    # Calcolo del punteggio Wilks
    wilks_coefficient = 600 / (a + b * bw + c * bw**2 + d * bw**3 + e * bw**4 + f * bw**5)
    wilks_score = max_estimate * wilks_coefficient

    return wilks_score



def compare_rating(elite_threshold, wilks_score):
    """
    Calcola il rating in base al punteggio Wilks rispetto a una soglia ELITE.

    :param elite_threshold: Soglia Wilks per il rango ELITE
    :param wilks_score: Punteggio Wilks attuale
    :return: rating : Punteggio ottenuto nell'esercizio in base alla soglia ELITE
    """

    #elite_threshold sta a 100 come wilks_score sta a rating

    rating = (100 * wilks_score) / elite_threshold

    return rating


def compute_rating(bw, lifted_weight, n_reps, elite_threshold):

    #elite_threshold = exercises.elite_threshold[string]

    max = compute_max(n_reps,lifted_weight)
    wilks = compute_wilks_2020(bw, max)
    rating = compare_rating(elite_threshold, wilks)
    return rating