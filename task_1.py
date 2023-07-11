# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

list_1 = [3, 6, 15, 8, 8, 3, 15, 7, 2, 0]
def set_element(list_1):
    count = 0
    set_new_list = []

    for i in list_1:
        for j in list_1:
            if i == j:
                count += 1
                if j not in set_new_list and count > 1:
                    set_new_list.append(j)
        count = 0
    return set_new_list

print(f"Список дублирующихся элементов без дубликатов {set_element(list_1)}")