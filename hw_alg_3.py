import statistics
def below_mean_elements(list):
    mean = statistics.mean(list)
    new_list = []
    for i in list:
        if i < mean:
            new_list.append(i)
    return new_list


my_list = [1, 3, 5, 6, 4, 10, 2, 3]
print(below_mean_elements(my_list))


def two_lowest_elements(list):
    list.sort()
    return list[:2]


my_list = [198, 3, 4, 9, 10, 9, 2]
print(two_lowest_elements(my_list))
