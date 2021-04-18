items_list = [int, float, "Rose", 5, 6, 9, 5, 89, 33, 54, 8]

for item in items_list:
    if str(item).isnumeric() and item>=9:
        print(item)

