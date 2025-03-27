import numpy as np 
a = [3,4,5,6,89,65,43]
arr = np.array(a)
floatarr = arr.astype(np.float64)#converting the type of data 
print(floatarr)
#assuming a is quantity of products and b is name of product
b = ["Shoes","Chocolate","Tshirts","Hats","Pens","Pencils","Erasers"]
barr = np.array(b)
#boolean inexing 
condition = arr > 10
morequantity = barr[condition]
print(morequantity) #prints items with quantity more than 10
