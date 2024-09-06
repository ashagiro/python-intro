# List Comprehention
# new_list = [new_item for item in list]
# can work with List, tuple, string, range

numbers = [1, 2, 3, 4, 5]
new_numbers = [n+1 for n in numbers]
new_range = [n*2 for n in range(1, 5)]
# new_range = [2, 4, 6, 8]

# Conditional list comprehention
# new_list = [new_item for item in list if test]

names = ["Alex", "Caroline", "Dave", "Beckham", "Marie", "Susie", "Beth"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num%2 == 0]
# print(result)

with open("file1.txt") as data_1:
    list_1 = data_1.readlines()
with open("file2.txt") as data_2:
    list_2 = data_2.readlines()
result_1 = [int(item.strip("\n")) for item in list_1]
result_2 = [int(item.strip("\n")) for item in list_2]
result = [item for item in result_1 if (item in result_2)]
# print(result)

# Dictionary comprehention
# new_dict = {new_key:new_value for item in list}
# OR
# new_dict = {new_key:new_value for (key, value) in dict.items()}

import random
student_scores = {student:random.randint(1, 100) for student in names}
# print(student_scores)
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {item:len(item) for item in sentence.split()}
# print(result)
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {key: ((value * 9/5) + 32) for (key, value) in weather_c.items()}
# print(weather_f)

# Pandas looping
import pandas

student_dict = {
    "student": ["Alex", "Caroline", "Dave", "Beckham", "Marie", "Susie", "Beth"],
    "score": [45, 67, 34, 65, 97, 70, 57]
}
# Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

student_dict_frame = pandas.DataFrame(student_dict)
print(student_dict_frame)
# loop through rows of dataframe:
for (index, row) in student_dict_frame.iterrows():
    print(row.score)

# Note:
# If unnamed dict (without student and score in student_dict) is converted to data frame then error occurs. 
# Can use "pandas.DataFrame(student_dict, index=[0])" or convert to list "pd.DataFrame({'A': [a], 'B': [b]}) or pd.DataFrame([{'A': a, 'B': b}])"
