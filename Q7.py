import  numpy as np

# finding element having maximum frequency

arr=np.array([1,1,1,2,3,4,5,6,78,95,12,45,45,45,45])
arr.sort()
n=arr.size
i=0
max_frequency=0
while (i<n):
    x=np.where(arr==arr[i])
    n1=len(x[0])
    # print(n1)
    if max_frequency<n1:
        max_frequency=n1
        max_frequency_element=i
    i=i+n1

print("the number having maximum frequency :", arr[max_frequency_element])
