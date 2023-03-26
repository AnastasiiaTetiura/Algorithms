
def even_numbers_first(arr):
    even_num = 0
    odd_num = len(arr) - 1

    while even_num < odd_num:
        if arr[even_num] % 2 == 0:
            even_num += 1
        else:
            arr[even_num] = arr[odd_num]
            arr[odd_num] = arr[even_num]
            odd_num -= 1
    return arr


test_list = [7, 3, 5, 6, 4, 10, 3, 2]
res = even_numbers_first(test_list)
print(res)


def increment_num(arr):
    index = len(arr) - 1
    while index >= 0 and arr[index] == 9:
        arr[index] = 0
        index -= 1

        if index < 0:
            arr.insert(0, 1)
        else:
            arr[index] += 1
    return arr


test_list = [1, 2, 9]
result = increment_num(test_list)
print(result)







