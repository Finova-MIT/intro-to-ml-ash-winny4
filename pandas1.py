import pandas as pd 
import numpy as np 
df = pd.read_csv(r"C:\Users\ashwi\OneDrive\Desktop\FINOVA-INTRO-TO-ML\intro-to-ml-ash-winny4\hotel.txt",delimiter='\t')
print(df)
print(df.describe())  #describes data, count, mean and all (for numeric columns)
print(df['Company'].value_counts()) #shows the companies and how many rooms they booked 
df2 = df.dropna()  #drop null vals and creates another df
#filling na vals 
print(df['Room number'].fillna(method='bfill'))


 



