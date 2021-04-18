dict1 = {i:f"item {i}" for  i in range(100, 200) if i%20==0}
print(dict1)

"""List Comprehensions"""
dict2 = {i:f"item {i}" for  i in range(10)}
dict2 = {value:key for key, value in dict2.items()}
print(dict2)


