def insertion_sort(arr):
    for i in range (1,len(arr)):
        key= arr[i]
        n= i-1
        while n>=0 and arr[n]>key:
            arr[n+1]= arr[n]
            n=n-1
            
        arr[n+1]= key
arr=[56,40,57,23,88,9,24,89,34,54,11,4]
insertion_sort(arr)
print("the sort array")
# for i in range(0,len(arr)):
#     print(arr[i])
for i in arr:
    print(i)