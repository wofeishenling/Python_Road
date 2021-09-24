import re

#-> list inefficiency
re.findall()

#-> iter 
it = re.finditer(r"\d+","vhfdjla10086hfabhhli98765")
for i in it:
    print(i.group())