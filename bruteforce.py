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
profit_max = 0
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
    for select_buy1 in select_buy:
        print(select_buy1["NomAction"],
              "Coût par action :", select_buy1["CoutParAction"],
              "Bénéfice :", select_buy1["PourcentageBenefice"])
    print("Total des actions: ", total_buy)
    print("Total des bénéfices : ", profit)


def profit_control(profit_max1):
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

