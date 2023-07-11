# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

weight = int(input('Input the bearing capacity of the bag in kg: '))
tings_dict = {'plate': 0.2, 'knife': 0.5, 'cup': 0.5, 'tent': 5, 'firewood': 7, 'coal': 5, 'clothes': 2, 'shoes': 1,
              'shugar': 0.2, 'water': 2, 'matches': 0.1, 'flashlight': 0.5
              }
res_list = []
tings_dict = dict(sorted(tings_dict.items(), key=lambda item: item[1]))

for item in tings_dict:
    if tings_dict[item] < weight:
        res_list.append(item)
        weight -= tings_dict[item]

print(res_list)

