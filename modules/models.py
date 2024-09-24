import random

class Fourmi:
    """Classe mère Fourmi avec les bases pour toutes les fourmis."""

    # Attribut de classe (partagé par toutes les fourmis)
    _energie_colonie = 20  # Attribut privé de classe

    def __init__(self, nom, energie, force, vitesse):
        self._nom = nom  # Attribut privé (encapsulé)
        self._energie = energie  # Attribut privé (encapsulé)
        self.force = force  # Attribut public
        self.vitesse = vitesse  # Attribut public

    @classmethod
    def se_deplacer(cls):
        """Méthode de classe pour réduire l'énergie globale de la colonie."""
        if cls._energie_colonie > 0:
            cls._energie_colonie -= 1
            print(f"Énergie de la colonie restante : {cls._energie_colonie}.")
        else:
            print("La colonie n'a plus d'énergie pour se déplacer.")

    @classmethod
    def get_energie_colonie(cls):
        """Méthode de classe pour accéder à l'énergie de la colonie (lecture)."""
        return cls._energie_colonie

    @classmethod
    def set_energie_colonie(cls, nouvelle_energie):
        """Méthode de classe pour modifier l'énergie de la colonie."""
        cls._energie_colonie = nouvelle_energie


class Ouvriere(Fourmi):
    """Classe Ouvrière qui hérite de Fourmi."""

    def collecter_nourriture(self):
        """Méthode d'instance spécifique à l'ouvrière."""
        nourriture = random.randint(1, 5)
        print(f"{self._nom} a collecté {nourriture} unité(s) de nourriture.")
        return nourriture


class Soldat(Fourmi):
    """Classe Soldat qui hérite de Fourmi."""

    def defendre_colonie(self):
        """Méthode d'instance spécifique au soldat."""
        print(f"{self._nom} défend la colonie avec une force de {self.force}.")


class Reine(Fourmi):
    """Classe Reine qui hérite de Fourmi."""

    def produire_fourmis(self):
        """Méthode d'instance spécifique à la reine."""
        nouvelles_fourmis = random.randint(1, 3)
        print(f"La reine {self._nom} produit {nouvelles_fourmis} nouvelle(s) fourmi(s).")
        return nouvelles_fourmis
