from functions_for_dict import beautiful_print, make_new_dict, generate_new_dict
# import matplotlib.pyplot as plt

dict_for_analysis = make_new_dict("titanic.csv")
statistics = generate_new_dict([["class", "First", "Second", "Third"], ["sex", "male", "female"], {"fares": [], "count": 0}], {})
# statistics = generate_new_dict([["embarked", "Southampton", "Cherbourg", "Queenstown", "unknown"], ["class", "First", "Second", "Third"], ["deck", "A", "B", "C", "D", "E", "F", "G"], {"fares": [], "count": 0}], {})
normal_cost = {"First": [30, 20000], "Second": [10, 40], "Third": [0, 20]}

# beautiful_print(statistics)
for people in dict_for_analysis.keys():

    class_key = dict_for_analysis[people]["class"]
    sex_key = dict_for_analysis[people]["sex"]
    embarked_key = dict_for_analysis[people]["embark_town"] if dict_for_analysis[people]["embark_town"] != "" else "unknown"
    deck_key = dict_for_analysis[people]["deck"] if dict_for_analysis[people]["deck"] != "" else "unknown"
    fare = float(dict_for_analysis[people]["fare"])

    if deck_key != "unknown":
        if fare and normal_cost[class_key][0] <= fare <= normal_cost[class_key][1]:
            statistics["class"][class_key]["sex"][sex_key]["fares"].append(fare)
            # statistics["embarked"][embarked_key]["class"][class_key]["deck"][deck_key]["fares"].append(fare)
        statistics["class"][class_key]["sex"][sex_key]["count"] += 1
        # statistics["embarked"][embarked_key]["class"][class_key]["deck"][deck_key]["count"] += 1

# for embarked_key in ["Southampton", "Cherbourg", "Queenstown", "unknown"]:
#     for class_key in ["First", "Second", "Third"]:
#         for deck_key in ["A", "B", "C", "D", "E", "F", "G"]:
#             fares = statistics["embarked"][embarked_key]["class"][class_key]["deck"][deck_key]["fares"]
#             if len(fares) > 0:
#                 statistics["embarked"][embarked_key]["class"][class_key]["deck"][deck_key]["average_fare"] = sum(fares) / len(fares)
#                 statistics["embarked"][embarked_key]["class"][class_key]["deck"][deck_key]["minimal_fare"] = min(fares)
#                 statistics["embarked"][embarked_key]["class"][class_key]["deck"][deck_key]["maximal_fare"] = max(fares)

for class_key in ["First", "Second", "Third"]:
    for sex_key in ["male", "female"]:
        fares = statistics["class"][class_key]["sex"][sex_key]["fares"]
        statistics["class"][class_key]["sex"][sex_key]["average_fare"] = sum(fares) / len(fares)
        statistics["class"][class_key]["sex"][sex_key]["minimal_fare"] = min(fares)
        statistics["class"][class_key]["sex"][sex_key]["maximal_fare"] = max(fares)

beautiful_print(statistics)

# from pylab import *

# classes, sex = {"First": "первый", "Second": "второй", "Third": "третий"}, {"male": "мужчинами", "female": "женщинами"}
# for class_key in ["First", "Second", "Third"]:
#     # for sex_key in ["male", "female"]:
#     x, y = [], []
#     # fares = statistics["class"][class_key]["sex"][sex_key]["fares"]
#     fares = statistics["class"][class_key]["fares"]
#     for cost in range(int(min(fares)), int(max(fares)) + 1):
#         x.append(cost)
#         y.append(len(list(filter(lambda f: f >= cost, fares))))
#     figure()
#     plot(x, y)
#     xlabel("Стоимость билетов")
#     ylabel("Количество желающих купить")
#     title(f"Спрос на билеты в {classes[class_key]} класс")
#     show()
#     # print(x, "\n", y)
#     input("Показать следующий график?")

# for class_key in ["First", "Second", "Third"]:
#     # for sex_key in ["male", "female"]:
#     x, y = [], []
#     # fares = statistics["class"][class_key]["sex"][sex_key]["fares"]
#     fares = statistics["class"][class_key]["fares"]
#     for cost in range(int(min(fares)), int(max(fares)) + 1):
#         x.append(cost)
#         y.append(len(list(filter(lambda f: cost + 1 >= f >= cost, fares))))
#     figure()
#     plot(x, y)
#     xlabel("Стоимость билета")
#     ylabel("Количество купленных билетов")
#     title(f"Покупка билетов в {classes[class_key]} класс")
#     show()
#     # print(x, "\n", y)
#     input("Показать следующий график?")

# beautiful_print(statistics)