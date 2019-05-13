import re

#No 4
f = open('key.htm', 'r', encoding='latin1')
teks = f.read()
f.close()
i = r'\s<td>[\d\.\w\/]+</td>'
p = r'(\w+)</a></td>' + i + i + i + r'\s<td>([\d\.\w\/]+)</td>'
string = re.findall(p, teks)
string1 = [(i[0], float(i[1])) for i in string]
print(string1)
