import csv
import os
import random

path = os.getcwd()
MAX = 500
select_action = []  # Liste des actions selectionnées
achat_action = 0  # Total des actions achetées
benefice = 0  # Total des bénéfices
nbr_temp = []  #
csv_path = os.path.join(path, "Actions.csv")
with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    list_actions = list(reader)


def calculate_percentage(get_i):
    get_i = int(get_i)
    get_action = list_actions[get_i]
    get_cost_action = int(get_action["CoutParAction"])  # Récupération du cout de l'action
    get_pourcentage = float(get_action["PourcentageBenefice"])  # Récupération du pourcentage
    get_profit_result = get_cost_action * get_pourcentage
    return get_action, get_profit_result


while True:
    i = random.randint(0, 19)
    if nbr_temp:
        if i not in nbr_temp:
            j = list_actions[i]
            nbr_temp.append(i)
            select_action.append(j)
    if not nbr_temp:
        action, profit_result = calculate_percentage(i)
        benefice = profit_result
        nbr_temp.append(i)
        select_action.append(action)


# k = achat_action * pourcentage
# benefice = "{0:.2f}".format(k) # Permet d'afficher les 2 chiffres après la virgule
