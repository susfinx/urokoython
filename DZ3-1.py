same_list = [1, 1, 2, 15, 3, 1, 38, 3, 5, 5, 4, 1, 3, 9, 4]
tu_list=[]
for i in same_list:
    if same_list.count(i) > 1:
        tu_list.append(i)

print(list(set(tu_list)))
