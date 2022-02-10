from data import some_data_for_dispersion_2, some_data_for_dispersion
from functions_for_dict import beautiful_print

# Набор данных для анализа
dataset_for_analysis = {}

# СНабор данных с группами
dataset = {}
for name, data in some_data_for_dispersion:
    dataset[name] = {"data": data}
    # dataset = {"group_1": {"data": group_1}, "group_2": {"data": group_2}, "group_3": {"data": group_3}}

# Нахожу кол-во учеников в группе и среднее арифметическое их результатов
for key in dataset.keys():
    key_data = dataset[key]["data"]
    dataset[key]["count"] = len(key_data)
    dataset[key]["average"] = sum(key_data) / len(key_data)

# Считаю дисперсионные значения для каждой группы
for key in dataset.keys():
    sq_med = sum([el**2 for el in dataset[key]["data"]]) / len(dataset[key]["data"])
    variance = sq_med - dataset[key]["average"]**2
    dataset[key]["square"] = sq_med
    dataset[key]["variance"] = variance
    dataset[key]['sigma'] = variance**0.5

# Нахожу среднее значение и среднюю дисперсию
total, count_pupils, total_var, total_square = 0, 0, 0, 0
for key in dataset.keys():
    count_pupils += dataset[key]["count"]
    total += dataset[key]["count"] * dataset[key]["average"]
    total_var += dataset[key]["variance"] * dataset[key]["count"]
    total_square += dataset[key]["square"] * dataset[key]["count"]
dataset_for_analysis["median"] = {"middle_score": total / count_pupils, "average_dispersion": total_var / count_pupils}
dataset_for_analysis["median"]["general_dispersion"] = total_square / count_pupils - dataset_for_analysis["median"]["middle_score"]**2

# Нахожу финальную дисперсию
znach, count_pupils = 0, 0
for key in dataset.keys():
    count_pupils += dataset[key]["count"]
    znach += (dataset_for_analysis["median"]["middle_score"] - dataset[key]["average"])**2 * dataset[key]["count"]
dataset_for_analysis["median"]["final_dispersion"] = znach / count_pupils
dataset_for_analysis["letter_etta"] = (dataset_for_analysis["median"]["final_dispersion"] / dataset_for_analysis["median"]["general_dispersion"])**0.5

beautiful_print(dataset)
beautiful_print(dataset_for_analysis)
