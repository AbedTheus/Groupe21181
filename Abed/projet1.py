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