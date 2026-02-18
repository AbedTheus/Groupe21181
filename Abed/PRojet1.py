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
            "aller dans le sens opposé du bruit"
        )

        if choix2 == "1":

            choix3 = poser_question(
                "Bobby se dirige sur la pointe des pieds tel un ninja vers le bruit et il remarque une vielle cabanne au milieu de la foret",
                "il va vers la cabanne malgré les bruit effrayant",
                "plus il s'approche de la cabanne plus il a peur du bruit et finis par s'enfuire"
            )

            if choix3 == "1":

                choix4 = poser_question(
                    "Bobby entre dans la cabanne et le bruit effrayant est un bucheron couvert de sang qui decoupe une viande rouge",
                    "",
                    ""


                )
            
            elif choix3 == "2":


        elif choix2 == "2":



    elif choix1 == "2":
