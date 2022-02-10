from copy import copy


def beautiful_print(data, add_nesting=0, lines_nesting=[], recr=0, last=False):  # Если бы мы знали, что это такое, но мы не знаем, что это такое
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
            beautiful_print(data[key], len(key) + 2, new_lines_nesting, recr + 1, last_dict_elem and recr == 0 or last)
    else:
        print(f"{'│' if not last else ' '}{''.join(lines_nesting[:-1]) + ' ' * add_nesting}└{data}")