from modules.models import Ouvriere, Soldat, Reine, Fourmi

class Simulation:
    """Contrôleur de la simulation de la colonie de fourmis."""

    def __init__(self, nb_ouvrieres, nb_soldats, nb_reines):
        self.colonie = []  # Liste pour stocker les fourmis
        self.nourriture_totale = 0
        self.nouvelles_fourmis_totales = 0

        # Initialisation de la colonie avec des ouvrières, soldats et reines
        for i in range(nb_ouvrieres):
            self.colonie.append(Ouvriere(f"Ouvrière_{i+1}", energie=10, force=2, vitesse=5))

        for i in range(nb_soldats):
            self.colonie.append(Soldat(f"Soldat_{i+1}", energie=12, force=5, vitesse=3))

        for i in range(nb_reines):
            self.colonie.append(Reine(f"Reine_{i+1}", energie=20, force=10, vitesse=1))

    def demarrer_simulation(self):
        """Lancer la simulation : toutes les fourmis effectuent leur action."""
        for fourmi in self.colonie:
            Fourmi.se_deplacer()  # Chaque fourmi se déplace (méthode de classe)

            if isinstance(fourmi, Ouvriere):
                self.nourriture_totale += fourmi.collecter_nourriture()  # Méthode d'instance
            elif isinstance(fourmi, Soldat):
                fourmi.defendre_colonie()  # Méthode d'instance
            elif isinstance(fourmi, Reine):
                self.nouvelles_fourmis_totales += fourmi.produire_fourmis()  # Méthode d'instance

    def afficher_resultats(self):
        """Affiche les résultats de la simulation."""
        print("-" * 10)
        print(f"Nourriture totale collectée : {self.nourriture_totale}")
        print("-" * 10)
        print(f"Nouvelles fourmis produites : {self.nouvelles_fourmis_totales}")
        print("-" * 10)
        print(f"Énergie restante de la colonie : {Fourmi.get_energie_colonie()}")
        print("-" * 10)
