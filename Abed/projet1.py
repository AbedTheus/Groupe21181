### Les fonctions a utiliser
"""1-une fonction qui va permettre de poser les questions
2-une fonction qui garde les choix précédent"""



def poser_question(question, option1, option2):
    """retourne le choix de l'utilisateur
    
    Args:
        question (str): texte qui pose la question a l'utilisateur
        option1 (str): premier choix
        option2 (str): deuxieme choix
    
    Returns:
        str: retourne le choix de l'utilisateur
    """
    
    print(question)
    print("1 -", option1)
    print("2 -", option2)
    
    choix = input("votre choix : ")
    return choix

def fonction_arbre():
    """Fonction qui contien l'arbre des decisions"""

    choix1 = poser_question(
        "Bobby un explorateur talentueux est perdu dans une foret sans son materielle pour l'aider a s'en sortir, que dois-t'il faire?",
        "avancer dans la foret  au hazard en esperant trouver quelque chose qui peut l'aider a s'en sortir",
        "rester la et reflechir"
    )

    if choix1 == "1":
        
        choix2 = poser_question(
            "bobby avance dans la foret et il entend un bruit",
            "aller dans la direction du bruit",
            


        )


    elif choix1 == "2":
