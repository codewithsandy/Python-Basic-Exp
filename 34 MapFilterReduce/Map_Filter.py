list1 = [2, 5, 8, 9, 4, 7]
def is_greater_5(num):
    return num>5
gr_than_5 = list(filter(is_greater_5, list1))
print(gr_than_5)
