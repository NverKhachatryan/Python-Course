def add_lists(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] + list2[i])
    return list3

def minus_lists(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] - list2[i])
    return list3

def multiply_lists(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] * list2[i])
    return list3

def divide_lists(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] / list2[i])
    return list3

