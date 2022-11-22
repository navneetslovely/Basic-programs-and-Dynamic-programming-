seq1= input("enter sequence: ")
seq2= input("enter the sequence 2: ")
#seq1= seq1.split()
#seq2= seq2.split()
print(seq1)
print(seq2)

seq1=[*seq1]
seq2=[*seq2]
 
lst1=[]
lst2=[]
for i in seq1:
    for j in seq2:
        #print(i)
        if seq1[i] in seq2[j]:
            print ("True")
            i=i+1
        else:
            print ("False")
            j=j+1