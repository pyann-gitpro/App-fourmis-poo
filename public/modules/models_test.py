# modules/models.py
import random

class Fourmi:
    energie_class = 20  # Énergie partagée de la colonie

    def __init__(self, nom: str, energie: int, force: int, vitesse: int, password: str) -> None:
        self.nom = nom
        self.energie = energie
        self.force = force
        self.vitesse = vitesse
        self.__password = password

    @classmethod
    def se_deplacer(cls):
        if cls.energie_class > 0:
            cls.energie_class -= 1
            print(f"Une fourmi se déplace. Énergie de la colonie restante : {cls.energie_class}.")
        else:
            print("La colonie n'a plus d'énergie pour se déplacer.")

my_ant = Fourmi("Antman", 10, 10, 10, "2024@++")

# my_ant.__password
print("-" * 10)
print(my_ant.nom)
print("-" * 10)
print(my_ant.vitesse)
print("-" * 10)








# class Ouvriere(Fourmi):
#     def collecter_nourriture(self):
#         nourriture = random.randint(1, 5)
#         print(f"{self.nom} a collecté {nourriture} unités de nourriture et la ramène à la colonie.")
#         return nourriture


# class Soldat(Fourmi):
#     def defendre_colonie(self):
#         print(f"{self.nom} se bat pour défendre la colonie avec une force de {self.force}.")


# class Reine(Fourmi):
#     def produire_fourmis(self):
#         nouvelles_fourmis = random.randint(1, 3)
#         print(f"La reine {self.nom} produit {nouvelles_fourmis} nouvelles fourmis pour agrandir la colonie.")
#         return nouvelles_fourmis
