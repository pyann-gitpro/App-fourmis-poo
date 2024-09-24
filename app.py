# App.py

from modules.controller import Simulation

if __name__ == "__main__":
    print("Début de la simulation de colonie de fourmis.")

    # Initialiser et démarrer la simulation
    simulation = Simulation(nb_ouvrieres=3, nb_soldats=2, nb_reines=1)
    simulation.demarrer_simulation()

    # Afficher les résultats
    simulation.afficher_resultats()
