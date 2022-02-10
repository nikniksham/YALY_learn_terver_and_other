from copy import copy
from data import some_data


def recr_print(data, add_nesting=0, lines_nesting=[], recr=0, last=False):  # Если бы мы знали, что это такое, но мы не знаем, что это такое
    first = recr == 0
    if type(data) is dict:
        keys = data.keys()
        for ind, key in enumerate(keys, start=1):
            last_dict_elem = (ind == len(keys))
            print(end=(("─" if len(keys) == 1 else ("┌" if ind == 1 else ("├" if not last_dict_elem else '└'))) if first else ("│" if not last else " ")))
            print(f"{''.join(lines_nesting[:-1]) + ' ' * add_nesting}{('├' if not last_dict_elem else '└') if recr > 0 else ''}<{key}>┐")
            if last_dict_elem and len(lines_nesting):
                lines_nesting[-1] = lines_nesting[-1].replace("│", " ")
            new_lines_nesting = copy(lines_nesting)
            new_lines_nesting.append((len(key) + 2) * ' ' + '│')
            recr_print(data[key], len(key) + 2, new_lines_nesting, recr + 1, last_dict_elem and recr == 0 or last)
    else:
        print(f"{'│' if not last else ' '}{''.join(lines_nesting[:-1]) + ' ' * add_nesting}└{data}")


# Набор данных для анализа
dataset_for_analysis = {}

# СНабор данных с группами
dataset = {}
for name, data in some_data:
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
dataset_for_analysis["median"] = {"score": total / count_pupils, "average_dispersion": total_var / count_pupils}
dataset_for_analysis["median"]["general_dispersion"] = total_square / count_pupils - dataset_for_analysis["median"]["score"]**2

# Нахожу финальную дисперсию
znach, count_pupils = 0, 0
for key in dataset.keys():
    count_pupils += dataset[key]["count"]
    znach += (dataset_for_analysis["median"]["score"] - dataset[key]["average"])**2 * dataset[key]["count"]
dataset_for_analysis["median"]["final_dispersion"] = znach / count_pupils
dataset_for_analysis["letter_etta"] = (dataset_for_analysis["median"]["final_dispersion"] / dataset_for_analysis["median"]["general_dispersion"])**0.5

# recr_print(dataset)
recr_print(dataset_for_analysis)
