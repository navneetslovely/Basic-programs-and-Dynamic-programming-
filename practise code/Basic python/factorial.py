# logic 1::program for fictorial of N

num=int(input("enter the number:  "))
# b=1
a=1
for i in range(1, num+1):
    a= i*a
print(a)



# logic2 :::

def recc(num):
    if num<0:
        return "error"
    if num==0 or num==1:
        return 1
    return num* recc(num-1)