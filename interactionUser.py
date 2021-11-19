
class User:
    
    def init():
        """Initialisation of the user"""
        print("OK")

    def chooseTrace(self):
        """Ask to the user to choose a trace"""

        print("1 : Entrepot -> 2 Rue Papin")
        print("2 : Entrepot -> 2 Rue Polytech")
        print("3 : Entrepot -> 2 Rue Apple")
        numTrace = input('Entrez le numero de la trace : ')
        return numTrace

