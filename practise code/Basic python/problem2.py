lst=[]
num=int(input("enter the numbers"))
for i in range(0,num+1):
    ele=int(input("enter the elements of the list"))
    lst.append(ele)
if len(lst)>2:
    max_num= max(lst)
    min_num= min(lst)
    if max_num==min_num:
        print("Error")
    else:
        sort_list = sorted(lst)
        print("sorted list: {}".format(sort_list))
        uniq_ele=set(sort_list)
        print("uniq_ele: {}".format(uniq_ele))
        new_sorted_list= list(uniq_ele)
        print(" second min: {}".format(new_sorted_list[-2]))
else:
    print("error")
