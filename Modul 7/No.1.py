import re


#No 1

f = open('indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
p = r'\s([Mm]e\w+)'
string = re.findall(p, teks)
print(string)
