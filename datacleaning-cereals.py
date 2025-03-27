#cereals csv from DAV LAB LMS
import pandas as pd
df = pd.read_csv(r"C:\Users\ashwi\OneDrive\Desktop\FINOVA-INTRO-TO-ML\intro-to-ml-ash-winny4\Cereals.xls",delimiter='\t')
summary_1 = df.describe().loc[['min', '25%', '50%', '75%','max']]
print("5 Number Summary Before Treating Missing Values:")
print(summary_1)
numeric_columns = df.select_dtypes(include=['float64','int64']).columns
for column in numeric_columns:
    mean_value = df[column].replace('?', pd.NA).mean()
    df[column] = df[column].replace('?', mean_value)
summary_after_missing = df.describe().loc[['min', '25%','50%', '75%', 'max']]
print("5 Number Summary After Treating Missing Values:")
print(summary_after_missing)
for column in numeric_columns:
    median_value = df[column].median()
    df[column] = df[column].apply(lambda x: median_value if x< 0 else x)
summary_after_noisy = df.describe().loc[['min', '25%', '50%','75%', 'max']]
print("5 Number Summary After Treating Noisy Values:")
print(summary_after_noisy)