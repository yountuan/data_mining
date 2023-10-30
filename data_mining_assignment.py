# 1. Write a program to create a list of names; then define a function to display all the elements in the received list. Call the function to execute its statements and display all names in the list.

# 2. Write a program to compare tuples of integers and tuples of strings.

# 3. Write a program to create a series to maintain three students’ names and GPA values.

# 4. Write a program to create a data frame to maintain three students’ names associated with their grades in three courses and then add a new column named Mean to maintain the calculated mean mark per course. Display the final data frame.


#1
# names = ["Mekia", "Amina", "Aida", "Gulnur", "Aliya"]

# def display_names(name_list):
#     for name in name_list:
#         print(name)

# display_names(names)

#2
# int_tuple1 = (1, 2, 3)
# int_tuple2 = (4, 2, 6)
# str_tuple1 = ("hello", "1", "world")
# str_tuple2 = ("hello", "apple", "world")

# if int_tuple1 == int_tuple2:
#     print("Integer tuples are equal")
# else:
#     print("Integer tuples are not equal")

# if str_tuple1 == str_tuple2:
#     print("String tuples are equal")
# else:
#     print("String tuples are not equal")

#3
import pandas as pd

# data = {'Student Name': ['Aida', 'Amina', 'Gulnur'], 'GPA': [4, 3.8, 3.7]}

# student_series = pd.Series(data)
# print(student_series)

#4
# data = {
#     'Student': ['Aida', 'Amina', 'Gulnur'],
#     'AI': [85, 95, 78],
#     'Data Mining': [92, 86, 65],
#     'Information Security': [82, 84, 91]
# }

# student_df = pd.DataFrame(data)
# student_df['Mean'] = student_df[['AI', 'Data Mining', 'Information Security']].mean(axis=1)
# print(student_df)


#5
# data1 = pd.read_csv("export_data1.csv")
# data2 = pd.read_csv("export_data2.csv")

# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)

# concat= pd.concat([df1, df2], axis=0)
# merged= df1.merge(df2, on='Country Name')

# print(concat)
# print(merged)

#6
# data = pd.read_csv("timesData.csv", nrows=50, usecols=["world_rank", "university_name", "country"])
# data = pd.DataFrame(data=data)
# print(data)

#7
import json
import pandas as pd
way = "dev-v1.1.json"
# with open('datapackage.json') as json_data:
#     JSONdta = json.load(json_data)
# print(JSONdta)

data = pd.read_json(way)
print(data.head())
columns = ["title", "paragraphs"]
selected_data = data[columns]

print(selected_data)