import re
str1 = '''Tech Limited
Mr. sandesh pol, programmer
9854, Akluj place
California, United State
phone: +1 25111996
fax: +1 20 12122255
Emain: sandy@tech.com
website: www.Infotech.com

ieee
Tech Bits, North America
Canada, United State
phone: +1 86511996
fax: +1 20 86542255
Emain: techbits@tech.com
website: www.techbits.com'''

"""Regular Expression"""
# patt = re.compile(r'.aliforni')
# matches = patt.finditer(str)
# for match in matches:
#     print(match)

# patt1 = re.compile(r'^Cali')
# matches1 = patt1.finditer(str)
# for match in matches1:
#     print(match)

# patt2 = re.compile(r'$Cali')
# matches2 = patt2.finditer(str)
# for match in matches2:
#     print(match)

patt2 = re.compile(r'its.com$')
matches2 = patt2.finditer(str1)
for match in matches2:
    print(match)

patt2 = re.compile(r'tec+')
matches2 = patt2.finditer(str1)
for match in matches2:
    print(match)

print("\n")
patt2 = re.compile(r'ie{3}')
matches2 = patt2.finditer(str1)
for match in matches2:
    print(match)