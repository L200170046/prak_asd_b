import re

#No 3
f = open('indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
p = r'\s[Dd]i\s[\w\.-]+'
string = re.findall(p, teks)
print(string)
