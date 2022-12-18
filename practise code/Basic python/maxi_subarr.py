

##############################################################################
n=int(input("enter the size of arr"))
lst=[]
for i in range(n):
    ele=int(input("enter element"))
    lst.append(ele)
print(lst)


############################################################################
n=input("enter the elemests of with spcae")
lst=[]
tp_lst=n.split(" ")
for i in range(len(tp_lst)):
    ele=int(tp_lst[i])
    lst.append(ele)
print(type(lst))
print(lst)


############################################################################
n=input("enter the elemests of with comma separated values")
lst=[]
tp_lst=n.split(",")
for i in range(len(tp_lst)):
    ele=int(tp_lst[i])
    lst.append(ele)
print(type(lst))
print(lst)


def find_max_cross(lst):
    sum=0
    lft_sum=float('-inf')
    for i in range(len(lst)/2):
        sum= sum+lst[i]
        if sum>lft_sum:
            lft_sum=sum

