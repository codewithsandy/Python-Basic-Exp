# Dot Format
me = "Sandy"
a1 = 12
a = "I am a {} {}"
b = a.format(me, a1)
print(b)
print("\n")
a = "I am a {1} {0}"    # start from 0
b = a.format(me, a1)
print(b)