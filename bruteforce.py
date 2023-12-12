import csv
import os
import random

path = os.getcwd()
MAX = 500
random_search = True
info_max = True
select_buy = []  # Liste des actions selectionnées
total_buy = 0  # Total des actions achetées
profit = 0  # Total des bénéfices
profit_max = 0 # Bénéfice max
nbr_temp = []  # Liste temporaire des index

"""Ouverture du fichier csv et stockage des données dans la variable list_actions """
csv_path = os.path.join(path, "Actions.csv")
with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    list_actions = list(reader)


def calculate_percentage(get_i):
    """
        Permet de selectionner une action, le coût de l'actionn, le pourcentage et calcul le bénéfice
        
        :parameter: get_id : Index de l'action
        :returns: get_actions, get_profit_result, get_cost_action
    """
    get_i = int(get_i)
    get_action = list_actions[get_i]
    get_cost_action = int(get_action["CoutParAction"])  # Récupération du cout de l'action
    get_pourcentage = float(get_action["PourcentageBenefice"])  # Récupération du pourcentage
    get_profit_result = get_cost_action * get_pourcentage
    return get_action, get_profit_result, get_cost_action


def show_result():
    """ Permet d'afficher la listes des actions selectionnées et les résultats"""
    print("Liste des actions selectionnées: ")
    for select_buy1 in select_buy:
        print(select_buy1["NomAction"],
              "Coût par action :", select_buy1["CoutParAction"],
              "Bénéfice :", select_buy1["PourcentageBenefice"])
    print("Total des actions: ", total_buy)
    print("Total des bénéfices : ", profit)


def profit_control(profit_max1):
    """
        Permet de rechercher la possibilité d'avoir un bénéfice supérieur. En cas d'égalité d'une boucle à l'autre,
        le programme appelle la fonction qui permet d'afficher le résultat trouvé. Si le bénéfice est inférieur au
        bénéfice max alors le programme recherche un bénéfice superieur.

        :param: profit_max1 : Ancien bénéfice trouvé
        :return: profit, info_max1, random_search1

     """
    profit_max1 = float(profit_max1)
    if profit_max1:
        if profit == profit_max1:
            show_result()
            info_max1 = False
            random_search1 = False
            return profit, info_max1, random_search1
        if profit > profit_max1:
            info_max1 = False
            return profit, info_max1, random_search
        if profit < profit_max1:
            info_max1 = False
            return profit, info_max1, random_search
    else:
        info_max1 = False
        return profit, info_max1, random_search


while random_search:
    """ 
        Boucle qui permet de sélectionner aléatoirement l'index de 0 à 19.
    
    Conditions :
    - Si nbr_temp est True et si l'index (i) n'est pas dans nbr_temp, on appelle la fonction calculate_percentage 
      en transmettant l'index et on récupère les données action, profit_result, cost_action.
    - Deux conditions qui vérifient si total_buy est supérieur ou inférieur à MAX. 
      
    Actions :
    - Si nbr_temp n'est pas True : On procède au calcul et on ajoute les données dans les variables.
    - Si random_search n'est pas True : Le programme met fin à la boucle.
    - Si info_max n'est pas True : On réinitialise les variables.         
    """
    i = random.randint(0, 19)
    if nbr_temp:
        if i not in nbr_temp:
            action, profit_result, cost_action = calculate_percentage(i)
            total_buy += cost_action
            if total_buy > MAX:
                total_buy -= cost_action
                info_profit, info_max, random_search = profit_control(profit_max)
                if profit > profit_max:
                    profit_max = info_profit
            if total_buy <= MAX:
                if info_max:
                    profit += profit_result
                    nbr_temp.append(i)
                    select_buy.append(action)

    if not nbr_temp:
        info_max = True
        action, profit_result, cost_action = calculate_percentage(i)
        profit = profit_result
        nbr_temp.append(i)
        select_buy.append(action)
        total_buy += cost_action
    if not random_search:
        random_search = False
    if not info_max:
        select_buy.clear()
        nbr_temp.clear()
        total_buy = 0
        profit = 0

