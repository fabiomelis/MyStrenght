import functions
import muscles
import exercises

'''
# CALCOLO PUNTEGGIO WILKS 2020 

bw = 80

lifted_weight = 250

n_reps = 1


max = functions.compute_max(n_reps,lifted_weight)
x = functions.compute_wilks_2020(bw,max)

print(x)
'''

bw = 67
fabio = exercises.Persona(bw, "Maschio", 25)

print("Dopo la creazione di Persona:")
print(f"Muscoli coinvolti in fabio: {[str(muscolo) for muscolo in fabio.muscoli_coinvolti.muscoli]}")

exercises.squat(bw, 6, 130, fabio)
print("\nDopo la funzione squat:")
print(f"Muscoli coinvolti in fabio: {[str(muscolo) for muscolo in fabio.muscoli_coinvolti.muscoli]}\n")

fabio.print_rating()

exercises.deadlift(bw, 1, 165, fabio)
print("\nDopo la funzione deadlift:")
print(f"Muscoli coinvolti in fabio: {[str(muscolo) for muscolo in fabio.muscoli_coinvolti.muscoli]}\n")

fabio.print_rating()

exercises.bench_press(bw, 6, 72.5, fabio)
print("\nDopo la funzione bench_press:")
print(f"Muscoli coinvolti in fabio: {[str(muscolo) for muscolo in fabio.muscoli_coinvolti.muscoli]}\n")

fabio.print_rating()

exercises.military_press(bw, 12, 38, fabio)
print("\nDopo la funzione military_press:")
print(f"Muscoli coinvolti in fabio: {[str(muscolo) for muscolo in fabio.muscoli_coinvolti.muscoli]}\n")


exercises.barbell_shrug(bw,12,80,fabio)

exercises.cable_bicep(bw,11,45,fabio)

exercises.dips(bw,22,bw,fabio)

exercises.dumbbell_lateral_raise(bw,12,12,fabio)

exercises.dumbell_curl(bw,12,12,fabio)

exercises.lat_pulldown(bw,11,60,fabio)

exercises.tricep_cable_pushdown(bw,10,50,fabio)

exercises.pull_ups(bw,20,bw,fabio)

exercises.decline_sit_ups(bw,50,bw,fabio)

exercises.machine_back_extension(bw,10,77.5,fabio)

fabio.print_rating()
