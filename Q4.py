def doubleTheString(str):
    reqStr=""
    for i in range(len(str)):
        reqStr+=str[i]+str[i]

    print(reqStr)
str1=input()
doubleTheString(str1)
