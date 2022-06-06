str1=input("enter the number")
sum=0
for i in range(len(str1)):
     if str1[i].isdigit():
         x=int(str1[i])
         sum=sum+x
print(sum)
