#list operations  
list=[] 
n = int(input("Enter number of elements in list:")) 
for i in range(0,n): 
    x = int(input("Enter element:")) 
    list.append(x) 
large = list[0] 
small = list[0] 
for i in list: 
    if i>large: 
        large = i 
for i in list: 
    if i<small: 
        small = i 
count=numsum=avg=0 
for i in list: 
    numsum = numsum + i 
avg = numsum/n 
cnum=int(input("Enter number to count:")) 
for i in list: 
    if i==cnum: 
        count+=1 
print("Largest element is %d"%(large)) 
print("Smallest element is %d"%(small))