d2 = {"Sandy":"Veg", "Rugita":"Fish", "Eshwari":{"B":"maggi", "L":"Pizza", "D":"cake"}}

d3 = d2
print(d2.copy())

del d3["Sandy"]
print(d2)

print("\n")
d1 = {"Sandy":"Veg", "Rugita":"Fish", "Eshwari":{"B":"maggi", "L":"Pizza", "D":"cake"}}
d4 = d1.copy()                      # complete copy using dot
del d4["Sandy"]
print(d1)

d1.update({"Leena":"Water"})
print(d1)
print(d1.keys())
print(d1.items())