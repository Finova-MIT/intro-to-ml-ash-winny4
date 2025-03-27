import pandas as pd
data = {
 'Roll Number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
 'Name': ['Ashwin', 'Rahul', 'Grace', 'Priya', 'Evan', 'Rohit', 'Om', 'Naina', 'Riya', 'Ayushi'],
 'Gender': ['M', 'M', 'F', 'F', 'M', 'M', 'M', 'F', 'F', 'F'],
 'Marks1': [85, 78, 92, 88, 76, 95, 89, 77, 84, 91],
 'Marks2': [80, 85, 78, 90, 82, 88, 79, 84, 86, 87],
 'Marks3': [90, 88, 85, 92, 87, 91, 86, 89, 84, 90]
}
df = pd.DataFrame(data) #convert data dictionary into dataframe
df['Total Marks'] = df['Marks1'] + df['Marks2'] + df['Marks3']
lowest_marks1 = df['Marks1'].min()
print(f"Lowest marks in Marks1: {lowest_marks1}")
highest_marks2 = df['Marks2'].max()
print(f"Highest marks in Marks2: {highest_marks2}")
average_marks3 = df['Marks3'].mean()
print(f"Average marks in Marks3: {average_marks3:.2f}")
df['Average Marks'] = df['Total Marks'] / 3
highest_avg_student = df.loc[df['Average Marks'].idxmax(), 'Name']
print(f"Student with highest average marks: {highest_avg_student}")
failed_students_marks2 = df[df['Marks2'] < 40].shape[0]
print(f"Number of students who failed in Marks2: {failed_students_marks2}")
