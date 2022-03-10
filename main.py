def mixing(arr1: list, arr2: list) -> list:
    """Generate array with PIN's, mixing between two array"""
    if len(arr1) == 0:
        return arr2
    arr_2d = [[i + j for i in arr1] for j in arr2]
    return [arr_2d[k][m] for k in range(len(arr_2d)) for m in range(len(arr_2d[k]))]


def get_pins(observed: str) -> [str]:
    """Generate array with all PIN's"""
    arr_str: list = list(observed)
    arr_all: list = []

    for i in arr_str:
        if i == '0':
            arr_all.append([i, '8'])
        elif i == '1':
            arr_all.append([i, '2', '4'])
        elif i == '2':
            arr_all.append(['1', i, '3', '5'])
        elif i == '3':
            arr_all.append(['2', i, '6'])
        elif i == '4':
            arr_all.append(['1', i, '5', '7'])
        elif i == '5':
            arr_all.append(['2', '4', i, '6', '8'])
        elif i == '6':
            arr_all.append(['3', '5', i, '9'])
        elif i == '7':
            arr_all.append(['4', i, '8'])
        elif i == '8':
            arr_all.append(['5', '7', i, '9', '0'])
        elif i == '9':
            arr_all.append(['6', '8', i])

    new_arr: list = []
    if len(arr_all) < 1:
        pass
    elif len(arr_all) == 1:
        new_arr = arr_all[0]
    else:
        for i in range(len(arr_all)):
            new_arr = mixing(new_arr, arr_all[i])

    return sorted(list(set(new_arr)))
