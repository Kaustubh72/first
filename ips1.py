import re
value = input()
#separate those non-digit characters
res = re.split ("\D+" , value)
# print the result
for elements in res :
    print (elements)
