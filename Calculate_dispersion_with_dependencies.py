# Файл для подсчёта коэффициент ранговой корреляции Спирмена
from data import some_data_with_dependencies, some_data_with_dependencies_2
from functions_for_dict import beautiful_print

# Записываем специфические гастрономические предпочтения
wife, husband = {}, {}
for name, k1, k2 in some_data_with_dependencies_2:
    wife[name] = k1
    husband[name] = k2

# Ищем r
taste_sum, count = 0, 0
for key in wife.keys():
    taste_sum += (wife[key] - husband[key])**2
    count += 1
dataset_for_analysis = {"r": 1 - (6 * taste_sum) / (count * (count**2 - 1))}

# beautiful_print(wife)
# beautiful_print(husband)
beautiful_print(dataset_for_analysis)