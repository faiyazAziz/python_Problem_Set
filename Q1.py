def ordreList(my_list,order):
    if (order=="asc"):
        my_list.sort()

    elif(order=="desc"):
        my_list.sort(reverse=True)

    elif(order=="none"):
        my_list=my_list

    else:
        print("\nchoose order as 'asc';'desc';'none' only")
    print(my_list)


n=int(input("enter no. of elements in list"))
list1=[]
for i in range(n):
    print("enter the number at position",i)
    x=float(input())
    list1.append(x)
order=input("enetr the order ")
ordreList(list1,order)
