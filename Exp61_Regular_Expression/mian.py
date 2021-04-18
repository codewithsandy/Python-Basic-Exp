import re
str = '''Tech Limited
Mr. sandesh pol, programmer
9854, Akluj place
California, United State
phone: +1 25111996
fax: +1 20 12122255
Emain: sandy@tech.com
website: www.Infotech.com

Tech Bits, North America
Canada, United State
phone: +1 86511996
fax: +1 20 86542255
Emain: techbits@tech.com
website: www.techbits.com'''

patt = re.compile(r'tech')

matches = patt.finditer(str)
for match in matches:
    print(match)

"""Simple searching using for lopp"""