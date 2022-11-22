# # Given n: the number of integers that need to be input, we need to input the integers and print the sum of these "n" integers.
# # logic =1
# list=[]
# num_count= int(input("enter the count of the element you wnat to provide in the list of number: "))

# for i in range (0, num_count):
#     num_element= int(input("enter the element in the list"))
#     list.append(num_element)
# num_element=list
# count_ele= len(num_element)
# sum=0
# if count_ele==num_count:
#     for i in num_element:
#         sum+= i
#         i+=1
#     print(sum)
# else: 
#     print(sum)
#     print("please elements of the list agian")


# logic 2 if the given input is in string form
print(50*"#")
num= int(input())
sum_l2=0

if num==0:
    print(sum_l2)
else:
    str=input()
    lst=str.split()    
    count_str=len(lst)
    if count_str==num:
        for i in lst:
            sum_l2+= int(i)
            
print(sum_l2)
