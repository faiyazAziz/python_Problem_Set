num1=int(input("enter the first numner of range"))
num2=int(input("enter the second number of range"))

for i in range(num1,num2):
    if (i==2 or i==3):
        print(i)
    for j in range(2,int(i**(1/2)+1)):
        if i%j==0:
            break
        if (j==int(i**(1/2))):
            print(i)