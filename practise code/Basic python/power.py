
num1=int(input("enter the base"))
num2=int(input("enter the power"))

#logic 1
def power(num1,num2):
    if num1==0 or num2 ==0:
        return 0
    if num2==1:
        return num1
    else:
        num=num1**num2
        return num
print("result using simple logic: {}".format(power(num1,num2)))



# logic 2
import math
def power_rec(num1,num2):
    if num1==0 or num2==0:
        return 0
    if num2==1:
        print("thidd id  rnningn2")
        return num1
    elif num2%2==0:
        print("this now running")
        temp=power_rec(num1,num2/2)
        print("temp1== ",temp)
        print(temp*temp)
        return temp*temp
    else:
        temp=power_rec(num1,math.floor(num2/2))
        print("temp2== ",temp)
        print(temp*temp)
        return temp*temp*num1
print("reuslt using rec: {}".format(power_rec(num1,num2)))