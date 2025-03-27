import pandas as pd                 #mtcars from DAV LAB LMS
import numpy as np 
import matplotlib.pyplot as plt 
df = pd.read_csv(r"C:\Users\ashwi\OneDrive\Desktop\FINOVA-INTRO-TO-ML\intro-to-ml-ash-winny4\mtcars.csv",delimiter='\t')

print(df.columns)
print(df.head())
df.columns = df.columns.str.strip()
mpg = df['mpg'] #mpg column from df 
mpg.plot() #line plot
plt.figure()
plt.show()
