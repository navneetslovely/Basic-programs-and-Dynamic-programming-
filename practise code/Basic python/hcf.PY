first_num= int(input("enter your first number"))
second_num= int(input('enter your second number'))

def calculateHCF(first_num, second_num):


    smaller_num= second_num if first_num>second_num else first_num
    HCF=1
    for i in range (1, smaller_num+1):
        if (first_num % i ==0) and (second_num % i ==0):
            HCF=i
    return HCF

print("HCF of {} and {} is {}".format(first_num,second_num, calculateHCF(first_num,second_num)))
