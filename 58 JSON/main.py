import json
data = '{"var1":"sandy", "var2":"1996"}'
parsed = json.loads(data)
print(parsed)
print(type(parsed))

print(parsed['var1'])



data2 = {"name":"Peter", "lname":"Parkar", "Job":["Spiderman", "Goodboy"], "cars":["Audi", "Ferrari", "BMW"]}

jscomp = json.dumps(data2)
print(jscomp)