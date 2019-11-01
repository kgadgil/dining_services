import wikipedia
import re

samsung = wikipedia.page("Samsung Galaxy Tab series")
#samsung.title
#samsung.categories
#samsung.sections
#samsung.content
#samsung.sections
#samsung.content
s = samsung.content
#print(s)
a = re.split("%s+",s)
#print(a)
for i in a:
    print(i)
splt = s.split("\n\n")
#print (splt[2])
#print(splt[3])
print(len(splt))
#for i in range(4,7):
#    print(splt[i])
#r = splt.split("===")
#print(r)
