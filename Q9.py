str1=input()
str_ord_list=[]
for i in range(len(str1)):
    str_ord=ord(str1[i])
    str_ord_list.append(str_ord)

str_ord_list.sort()
reqStr=""
for i in range(len(str1)):
    reqStr+=chr(str_ord_list[i])
print(reqStr)