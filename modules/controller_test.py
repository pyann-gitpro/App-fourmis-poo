# modules/controller.py
from modules.models_test import Ouvriere, Soldat, Reine, Fourmi

class Simulation:
    def __init__(self):
        self.colonie = []
        self.nourriture_totale = 0
        self.nouvelles_fourmis_totales = 0

    def initialiser_colonie(self):
        # Ajout des ouvrières
        for i in range(5):
            self.colonie.append(Ouvriere(f"Ouvrière_{i+1}", energie=10, force=2, vitesse=5))

        # Ajout des soldats
        for i in range(3):
            self.colonie.append(Soldat(f"Soldat_{i+1}", energie=12, force=5, vitesse=3))

        # Ajout de la reine
        self.colonie.append(Reine(f"Kimera", energie=20, force=10, vitesse=1))

    def simuler(self):
        # Simulation des actions de la colonie
        for fourmi in self.colonie:
            Fourmi.se_deplacer()

            if isinstance(fourmi, Ouvriere):
                self.nourriture_totale += fourmi.collecter_nourriture()
            elif isinstance(fourmi, Soldat):
                fourmi.defendre_colonie()
            elif isinstance(fourmi, Reine):
                self.nouvelles_fourmis_totales += fourmi.produire_fourmis()

    def afficher_resultats(self):
        print(f"Nourriture totale collectée : {self.nourriture_totale}")
        print(f"Nouvelles fourmis produites : {self.nouvelles_fourmis_totales}")
