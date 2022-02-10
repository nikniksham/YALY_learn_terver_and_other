from copy import copy


def beautiful_print(data, add_nesting=0, lines_nesting=[], recr=0, last=False):  # Делает красивый вывод словарика, очень красивый вывод
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
            new_lines_nesting.append((len(str(key)) + 2) * ' ' + '│')
            beautiful_print(data[key], len(str(key)) + 2, new_lines_nesting, recr + 1, last_dict_elem and recr == 0 or last)
    else:
        print(f"{'│' if not last else ' '}{''.join(lines_nesting[:-1]) + ' ' * add_nesting}└({data})")


def make_new_dict(filename):  # Делает словарь из файла csv
    new_dict = {}
    with open(filename, "r") as file:
        args = []
        for arg in file.readline().strip().split(","):
            args.append(arg)
        for i, elem in enumerate(file.readlines()):
            new_name = f"people_{i + 1}"
            new_dict[new_name] = {}
            for ind, arg in enumerate(elem.strip().split(",")):
                new_dict[new_name][args[ind]] = arg
    return new_dict


def generate_new_dict(args, new_dict):  # Даже не спрашивайте как, работает и работает
    arg = args[0]
    if type(arg) is dict:
        return dict(arg)
    else:
        new_dict[arg[0]] = {}
        for elem in arg[1:]:
            new_dict[arg[0]][elem] = generate_new_dict((args[1:] if 1 < len(args) else [{}]), {})
    return dict(new_dict)


# beautiful_print(new_generate_new_dict([["a", "b", "c"], ["d", "e", "f"], {1: 0, 2: 0}], {}))

# beautiful_print(generate_new_dict([["people", "adult", "children"], ["sex", "male", "female"], ["class", "First", "Second", "Third"], {"average_fare": 0, "count_known_fares": 0, "alone": 0, "with_pair": 0, "survived": 0, "died": 0, "average_age": 0, "count_known_ages": 0, "survival_rate": 0}], {}))
# statistics = generate_new_dict([["people", "adult", "children"], ["sex", "male", "female"], ["class", "First", "Second", "Third"], ["company", "alone", "with_pair"], {"average_fare": 0, "count_known_fares": 0, "survived": 0, "died": 0, "average_age": 0, "count_known_ages": 0, "survival_rate": 0}], {})
# beautiful_print(statistics)