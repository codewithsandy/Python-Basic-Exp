# Dictionary is nothing but key value pairs

d1 = {}
print(type(d1))

d2 = {"Sandy":"Veg", "Rugita":"Fish", "Eshwari":{"B":"maggi", "L":"Pizza", "D":"cake"}}

print(d2)

d2[52] = "Burger"
print(d2)

del d2[52]
print(d2)

print(d2["Rugita"])
print(d2["Eshwari"])
