"""Normal List uses Squqre Bracket"""
set2 = [myset1 for myset1 in ["set01", "set02", "set01", "set03", "set01"]]
print(set2)
print(type(set2))


"""Set Comprehensions use Curle Bracket"""
set1 = {myset for myset in {"set01", "set02", "set01", "set03", "set01"}}
print(set1)
print(type(set1))