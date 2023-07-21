import random

MAX_BAG = 10
bag_list = []
bag_dict = {
    'Myaso': 3,
    'hleb': 1,
    'tushenka': 0.5,
    'spalnik': 3,
    'palatka': 5,
    'makarony': 3
}
total_weight = 0

items = list(bag_dict.keys())

while total_weight < MAX_BAG:
    chosen_item = random.sample(items, 1)[0]
    item_weight = bag_dict[chosen_item]

    if total_weight + item_weight <= MAX_BAG:
        total_weight += item_weight
        bag_list.append(chosen_item)

print(bag_list)
