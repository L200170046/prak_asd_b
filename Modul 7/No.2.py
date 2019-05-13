import re

#No 2
f = open('indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
p = r'\s(di\w+)'
string = re.findall(p, teks)
print(string)
