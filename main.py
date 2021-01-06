# # with open("weather_data.csv") as weather_data_file:
# #     weather_data = weather_data_file.readlines()
# #     print(weather_data)

# # import csv

# # with open("weather_data.csv") as weather_data_file:
# #     weather_data = csv.reader(weather_data_file)
# #     temperature = []
# #     for row in weather_data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))

# #     print(temperature)
# # import matplotlib.pyplot as plt
# import pandas
# data = pandas.read_csv("weather_data.csv")
# #!gettng data in column
# # print(data.condition)

# # # print(data["temp"])

# # data_dict = data.to_html()
# # print(data_dict)


# # temp_list = data["temp"].to_list()
# # print(temp_list)

# # max_temp = data["temp"].max()
# # print(max_temp)

# #! getting data in row 

# # print(data[data.day=="Monday"])

# # print(data[data.temp==data.temp.max()])

# # monday = data[data.day=="Monday"]

# # print(monday.condition)

# # print(int((monday.temp*9/5)+32))
# #! create dataframe from scratch
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "scores" : [89,34,45]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("./data.csv")
# print(data)


import pandas
data = pandas.read_csv("squirrel_data.csv")
gray_squirrel =  len(data[data["Primary Fur Color"]=="Gray"])
red_squirrel =  len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel =  len(data[data["Primary Fur Color"]=="Black"])
print(gray_squirrel)
print(red_squirrel)
print(black_squirrel)

data_dict = {
    "Fur color": ["Gray","Cinnamon","Black"],
    "Count": [gray_squirrel,red_squirrel,black_squirrel]

}

count_data = pandas.DataFrame(data_dict)
count_data.to_csv("./count_data_squirrel.csv")