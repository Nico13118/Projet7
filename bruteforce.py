import csv
import os
import random

path = os.getcwd()
MAX = 500
random_search = True
info_max = True
select_action = []  # Liste des actions selectionnées
achat_action = 0  # Total des actions achetées
benefice = 0  # Total des bénéfices
benefice_max = 0
nbr_temp = []  # Liste temporaire des index

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
    return get_action, get_profit_result, get_cost_action


def show_result():
    print("Liste des actions selectionnées: ")
    for select_action1 in select_action:
        print(select_action1["NomAction"],
              "Coût par action :", select_action1["CoutParAction"],
              "Bénéfice :", select_action1["PourcentageBenefice"])
    print("Total des actions: ", achat_action)
    print("Total des bénéfices : ", benefice)
    return False


def profit_control(benefice_max1):
    benefice_max1 = float(benefice_max1)
    if benefice_max1:
        if benefice == benefice_max1:
            show_result()
            info_max1 = False
            random_search1 = False
            return benefice, info_max1, random_search1
        if benefice > benefice_max1:
            info_max1 = False
            return benefice, info_max1, random_search
        if benefice < benefice_max1:
            info_max1 = False
            return benefice, info_max1, random_search
    else:
        info_max1 = False
        return benefice, info_max1, random_search


while random_search:
    i = random.randint(0, 19)
    if nbr_temp:
        if i not in nbr_temp:
            action, profit_result, cost_action = calculate_percentage(i)
            achat_action += cost_action
            if achat_action > MAX:
                achat_action -= cost_action
                info_benefice, info_max, random_search = profit_control(benefice_max)
                if benefice > benefice_max:
                    benefice_max = info_benefice
            if achat_action <= MAX:
                if info_max:
                    benefice += profit_result
                    nbr_temp.append(i)
                    select_action.append(action)

    if not nbr_temp:
        info_max = True
        action, profit_result, cost_action = calculate_percentage(i)
        benefice = profit_result
        nbr_temp.append(i)
        select_action.append(action)
        achat_action += cost_action
    if not random_search:
        random_search = False
    if not info_max:
        select_action.clear()
        nbr_temp.clear()
        achat_action = 0
        benefice = 0


# k = achat_action * pourcentage
# benefice = "{0:.2f}".format(k) # Permet d'afficher les 2 chiffres après la virgule
