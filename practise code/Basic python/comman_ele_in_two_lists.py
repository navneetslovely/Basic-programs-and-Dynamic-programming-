

num_in_list1= int(input("enter the number of elements in the list 1:  "))
num_in_list2= int(input("enter the number of elements in the list 2:  "))
list1=[]
list2=[]
for i in range(num_in_list1):
    lst=int(input("enter the elements o fthe list 1:  "))
    list1.append(lst)

for i in range(num_in_list2):
    lst=int(input("enter the elements o fthe list 2:  "))
    list2.append(lst)



#basic logic with O(n*m) time complexity 
com_cont=0
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            print("common elements detected")
            print(list1[i])
            com_cont+=1
print("number of comman elements: ", com_cont)        
####### print("No common element found in list 1 and list 2")

#common elements in two lists in O(N) time and O(M) space IF n>m

lis_dic={}
for i in list2:
    lis_dic[i]= 1
print("Dict: {}".format(lis_dic))


cnt=0
for j in list1:
    if lis_dic.get(j)!= None:
        print(j)
        cnt += 1
print("Number of comman elements: ", cnt)





