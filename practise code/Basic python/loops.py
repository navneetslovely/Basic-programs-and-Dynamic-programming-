#prgram to display all the prime number in the range or interval

num1= int(input("enter the first number of the range:  "))
num2= int(input("enter the second number of the range: "))

print(" prime number in the range {0} and {1} are: ".format(num1, num2))

for num in range(num1,num2+1):
    if num >1:
        isDivisible= False
        for i in range (2, num):
            if num %i==0:
                isDivisible = True
        if not isDivisible:
            print(num)





