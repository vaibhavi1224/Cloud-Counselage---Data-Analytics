# -*- coding: utf-8 -*-
"""Data analytics data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bkAN5StXUMCvDu45kpxuaS67g-hJvnsl
"""

import pandas as pd

# Load the Excel file
data = pd.read_excel('Data analyst Data.xlsx')

# Display the first few rows of the dataset to understand its structure
data.head()

"""**Question 1: How many unique students are included in the dataset?**"""

# Count the number of unique students based on 'Email ID'
unique_students = data['Email ID'].nunique()
unique_students

"""**Question 2: What is the average GPA of the students?**"""

# Calculate the average GPA (CGPA) of the students
average_gpa = data['CGPA'].mean()
average_gpa

"""**Question 3: What is the distribution of students across different graduation years?**"""

# Get the distribution of students across different graduation years
grad_year_distribution = data['Year of Graduation'].value_counts()
grad_year_distribution

"""**Question 4: What is the distribution of students' experience with Python programming?**"""

# Get the distribution of students' experience with Python programming (in months)
python_exp_distribution = data['Experience with python (Months)'].value_counts()
python_exp_distribution

"""**Question 5: What is the average family income of the student?**"""

# The 'Family Income' column is categorical, so we can summarize it by counting occurrences
family_income_distribution = data['Family Income'].value_counts()
family_income_distribution

"""**How does the GPA vary among different colleges? (Show top 5 results only)**"""

# Calculate the average GPA for each college and display the top 5
gpa_by_college = data.groupby('College Name')['CGPA'].mean().sort_values(ascending=False).head(5)
gpa_by_college

"""**Question 7: Are there any outliers in the quantity (number of courses completed) attribute?**"""

# Identify outliers using the IQR method for the 'Quantity' column
Q1 = data['Quantity'].quantile(0.25)
Q3 = data['Quantity'].quantile(0.75)
IQR = Q3 - Q1
outliers = data[(data['Quantity'] < (Q1 - 1.5 * IQR)) | (data['Quantity'] > (Q3 + 1.5 * IQR))]
if outliers.empty:
    print("No outliers found.")
else:
    print("Outliers:")
    print(outliers)

"""**Question 8: What is the average GPA for students from each city?**"""

# Calculate the average GPA for each city
gpa_by_city = data.groupby('City')['CGPA'].mean()
gpa_by_city

"""**Question 9: Can we identify any relationship between family income and GPA?**"""

# First, we need to convert the 'Family Income' categorical data to numerical form for correlation analysis
income_map = {'0-2 Lakh': 1, '2-5 Lakh': 2, '5-7 Lakh': 3, '7 Lakh+': 4}
data['Family Income Numeric'] = data['Family Income'].map(income_map)

# Calculate the correlation between family income and GPA
correlation_income_gpa = data[['Family Income Numeric', 'CGPA']].corr().iloc[0, 1]
if correlation_income_gpa > 0:
    print("There is a positive correlation between family income and GPA, correlation between income and gpa is",correlation_income_gpa)
elif correlation_income_gpa < 0:
    print("There is a negative correlation between family income and GPA.")

"""**Question 10: How many students from various cities? (Solve using data visualization tool).**"""

import matplotlib.pyplot as plt
import seaborn as sns

# Count the number of students from various cities
students_by_city = data['City'].value_counts()

# Plotting the data
plt.figure(figsize=(12, 6))
sns.barplot(x=students_by_city.index, y=students_by_city.values, palette='viridis')
plt.title('Number of Students from Various Cities')
plt.xlabel('City')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.show()

"""**Question 11: How does the expected salary vary based on factors like 'GPA', 'Family income', 'Experience with python (Months)'?**"""

import seaborn as sns
import matplotlib.pyplot as plt

# Convert 'Expected salary (Lac)' to numeric
data['Expected salary (Lac)'] = pd.to_numeric(data['Expected salary (Lac)'])

# Plotting the relationships
plt.figure(figsize=(14, 8))

plt.subplot(3, 1, 1)
sns.scatterplot(data=data, x='CGPA', y='Expected salary (Lac)')
plt.title('Expected Salary vs GPA')

plt.subplot(3, 1, 2)
sns.boxplot(data=data, x='Family Income', y='Expected salary (Lac)')
plt.title('Expected Salary vs Family Income')

plt.subplot(3, 1, 3)
sns.scatterplot(data=data, x='Experience with python (Months)', y='Expected salary (Lac)')
plt.title('Expected Salary vs Experience with Python (Months)')

plt.tight_layout()
plt.show()

"""**Question 12: Which event tends to attract more students from specific fields of study?**"""

# Count the number of students for each event
students_by_event = data['Events'].value_counts()
students_by_event

"""**Question 14: How many students are graduating by the end of 2024?**"""

# Count the number of students graduating by 2024
students_grad_2024 = data[data['Year of Graduation'] <= 2024].shape[0]
students_grad_2024

"""**Question 15: Which promotion channel brings in more student participations for the event?**"""

# Count the promotion channels
promotion_channel = data['How did you come to know about this event?'].value_counts()
promotion_channel

"""**Question 16: Find the total number of students who attended the events related to Data Science? (From all Data Science related courses.)**"""

# Assuming 'Data Science related courses' are identified in the 'Events' column
data_science_events = data[data['Events'].str.contains('Data Science', case=False, na=False)]
total_data_science_students = data_science_events['Email ID'].nunique()
total_data_science_students

"""**Question 17: Those who have high CGPA & more experience in language, do they have high expectations for salary? (Avg)**"""

# Defining 'high' CGPA and 'more' experience
high_cgpa_threshold = data['CGPA'].mean()
more_experience_threshold = data['Experience with python (Months)'].mean()

# Filtering students with high CGPA and more experience
high_cgpa_more_exp = data[(data['CGPA'] > high_cgpa_threshold) &
                          (data['Experience with python (Months)'] > more_experience_threshold)]

# Average expected salary for these students
avg_expected_salary_high_cgpa_exp = high_cgpa_more_exp['Expected salary (Lac)'].mean()
if avg_expected_salary_high_cgpa_exp is not None:
    avg_expected_salary_high_cgpa_exp = round(avg_expected_salary_high_cgpa_exp, 2)
print("yes they do have higher expectation in salary and the avg is:",avg_expected_salary_high_cgpa_exp)

"""**Question 18: How many students know about the event from their colleges? Which are these Top 5 colleges?**"""

# Count students who came to know about the event from their colleges
college_promotion_students = data[data['How did you come to know about this event?'] == 'College']
total_college_promotion_students = college_promotion_students.shape[0]

# Top 5 colleges by number of students knowing about the event
top_5_colleges = college_promotion_students['College Name'].value_counts().head(5)
total_college_promotion_students, top_5_colleges