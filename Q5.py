
arr=[]
for i in range(0,100):
    x=int(input())
    arr.append(x)
found=0
for i in range(100):
   for j in range(i+1,100):
       if (arr[i]==arr[j]):
           print(arr[i])
           found+=1
           break
   if found==1:
        break

