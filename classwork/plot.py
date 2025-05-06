# import matplotlib.pyplot as plt 
# x = [1,2,3,4,5]
# y1 = [5,15,25,35,45]
# y2 = [10,30,20,40,50]
# plt.plot (x, y1, marker = 'o', linestyle = '--', color = 'b', label = "line1")
# plt.plot (x, y2, marker = '*', linestyle = '-', color = 'r', label = "line2")
# plt.xlabel ("X-axis")
# plt.ylabel ("Y-axis")
# plt.title("Two line plot")
# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt
# study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# exam_scores = [50, 55, 60, 65, 70, 75, 80, 85, 90, 100]
# plt.scatter(study_hours, exam_scores, color = 'g', marker = 'o', label = "student")
# plt.xlabel ("Study hours")
# plt.ylabel ("exam scores")
# plt.title ("hours vs scores")
# plt.legend ()
# plt.grid (True)
# plt.show ()

# import matplotlib.pyplot as plt
# import numpy as np
# height = np.random.randint (140, 191, 100)
# plt.hist (height, bins = 10, color = 'b', edgecolor = 'k')
# plt.xlabel("height (cm)")
# plt.ylabel("frequency")
# plt.title("Student height Distribution")
# plt.show()

# import matplotlib.pyplot as plt

# name = ['Apple', 'Samsung', 'Redmi', 'Oneplus']
# market_share = [30, 35, 20, 15]
# col = ['y', 'b', 'g', 'r']

# plt.pie(market_share, 
#         labels=name, 
#         colors=col, 
#         autopct='%1.1f%%',  # Fixed typo: autopet → autopct
#         startangle=140)

# plt.title("Smartphone Market Share")
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# # Define number of students
# student = 10  # You can change this number

# # Generate random scores (50-100) for each subject
# maths_score = np.random.randint(50, 101, student)
# sci_score = np.random.randint(50, 101, student)
# eng_score = np.random.randint(50, 101, student)

# # Create DataFrame
# df = pd.DataFrame({
#     "Student ID": range(1, student + 1),
#     "Math": maths_score,
#     "Science": sci_score,
#     "English": eng_score
# })

# # Calculate average marks
# df["Average Marks"] = df[["Math", "Science", "English"]].mean(axis=1)

# # Display DataFrame
# print(df)
# plt.bar(df["Student ID"], df["Average Marks"], color ='b', label = "Students")
# plt.xlabel ("Student ID")
# plt.ylabel("Avg Marks")
# plt.title("Student performance")
# plt.legend()
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd. DataFrame({
#     'Month' : ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
#     'Sales' : [1200, 1500, 1800, 2100, 1900, 2300]
# })
# print("Sales Data")
# print(df)
# print("\n")

# total_sales = df['Sales'].sum()
# avg_sales = df['Sales'].mean()
# print(f"Total Sales: {total_sales:,.2f}\n")
# print(f"Average Sales: {avg_sales:.2f}\n")

# plt.plot(df['Month'], df['Sales'], marker='o', color='b', linestyle='-')
# plt.title('Monthly Sales Performance')
# plt.xlabel('Month')
# plt.ylabel('Sales')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("myfile.xlsx")

# 2. Clean data (no missing values here, just showing the step)
df = df.dropna()  # This would remove any empty rows if they existed

# 3. Basic plots
# Sales line plot
df.plot(x='Month', y='Sales', kind='line', marker='o', 
        title='Monthly Sales', color='blue')
plt.ylabel('Amount ($)')
plt.show()

# Expenses bar chart
df.plot(x='Month', y='Expenses', kind='bar', 
        title='Monthly Expenses', color='orange')
plt.ylabel('Amount ($)')
plt.show()

# 4. Show the data
print("\nSales Data:")
print(df)