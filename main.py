#Projet Pizza
"""on crée une liste de pizza contenant un tuple pour les ingredients 
ce programme affiche a l'utilisateur le menu des pizza et pernet a l'utilisateur de créer 
sa pizza personnalisée. On utilisera la POO(Programmation Orientée Objet) de python
"""

class Pizza:
    
    def __init__(self,nom :str ,prix : str,ingredients, vegetarien : bool = False) -> None:
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarien = vegetarien

    def afficher(self) :
        vegetarien_str = "" 
        if self.vegetarien:
            vegetarien_str = " - VEGETARIENNE "
        print(f"PIZZA {self.nom} : {self.prix}$" + vegetarien_str )
        print((",").join(self.ingredients))
        print("")



class PizzaPersonnalisee(Pizza):
    PRIX_DE_BASE=7
    PRIX_PAR_INGREDIENT=1.5
    dernier_numero=0
    def __init__(self) -> None:
        PizzaPersonnalisee.dernier_numero+=1
        self.numero=PizzaPersonnalisee.dernier_numero
        super().__init__("Personnalisée "+ str(self.numero), 0, [])
      
        self.ajouter_ingredient()
        self.calculer_le_prix()


    def ajouter_ingredient(self):
        print()
        print(f"Ingredients pour la pizza personnalisée {self.numero}")
        self.ingredients=[]
        while True:
            ingr_entrer=input("Ajouter chaque ingredients / appuyer sur ENTR pour terminer :")
            print(f'vous avez ajouter {len(self.ingredients)+1} ingrédients')
            self.ingredients.append(ingr_entrer)
            if ingr_entrer =='':
                break
    def calculer_le_prix(self):
        self.prix=PizzaPersonnalisee.PRIX_DE_BASE
        for i in self.ingredients:
            self.prix += 1.5
        
pizzas = [
    Pizza("4 fromages" ,8.5 ,("brie","emmental","compté","parmesan"),True),
    Pizza("Hawai" ,9.5 ,("tomate","ananas","oignoms","parmesan")),
    Pizza("4 saisons" ,11 ,("oeuf","emmental","tomate","jambon")),
    Pizza("végétarienne" ,7.8 ,("champignon","tomate","oignon","poivron"),True),
]       


while True: 
    print("--------MENU---------")
    print("Que voulez vous faire?")
    print("""
1-Afficher le menu des pizzas disponibles 
2-Créer une pizza personalisée
"""
)
    reponse=input("Votre choix:")
    try:
        reponse_int = int(reponse)
    except:
        print("ERREUR veuillez saisir un nombre ")
        
    else:
            
        if 1 > reponse_int or reponse_int == "":
            print("ERREUR veuillez saisir un nombre entre 1 et 2")
        elif reponse_int == 1:
            for i in pizzas:
                i.afficher()
            
        elif reponse_int == 2:
            pizza=PizzaPersonnalisee()
            pizzas.append(pizza)
        else:
            print("ERREUR veuillez saisir un nombre entre 1 et 2")





