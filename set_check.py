"""set_check
Given two sorted lists, create functions that would perform a set union and set intersections on the lists
"""


def set_union(list1, list2):
    return list(set(list1 + list2))


def set_intersection(list1, list2):
    return list(set(list1) - set(list2))


# implement manually
def set_union_manual(list1, list2):
    # if len(list1) > len(list2):
    list_dict = {x: x for x in list1}
    new_list = list1
    for ele in list2:
        if ele in list_dict:
            continue
        new_list.append(ele)
    return new_list

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    b = [6, 7, 8, 9, 0]
    print(set_union(a, b))
    # print(set_intersection(a, b))
    print(set_union_manual(a, b))

