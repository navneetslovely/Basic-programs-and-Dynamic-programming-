# rod_len= int(input("Enter the lenght of the rod:  "))
price_table={}
num=int(input("enter the lenght of table"))
for i in range(num+1):
    len_pi=int(input("enter the lenght in inch:  "))
    pri_len=int(input("enter the price of the length:  "))
    price_table[len_pi]=pri_len
print(price_table)

