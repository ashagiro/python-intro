
# with open("./weather_data.csv") as file:
#    all_data = file.readlines()
# data = all_data.split("\n")
# print(data)

# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             continue
#         temperatures.append(int(row[1]))
# print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data["temp"].mean())
# print(data["temp"].max())

# #Get data in columns
# print(data["day"])
# print(data.condition)

# #Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# # create dataframe from a scratch
# data_dict = {
#     "students": ["Angela", "Aidana", "Nursultan"],
#     "scores": [34, 76, 96]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# make a table with a fur color and amount of squirrels
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

dict = {
    "color": ["grey", "black", "cinnamon"],
    "number": [grey_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}

df = pandas.DataFrame(dict)
df.to_csv("squirrel_count.csv")

