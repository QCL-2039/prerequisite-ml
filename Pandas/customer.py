#Here i will perfomr data clearing operations

import pandas as pd 

print("Version of your Pandas:",pd.__version__)

#Task-1
data = pd.read_csv("customers-10000.csv")
# print(data.head(5))
# print(data.shape)

# Task-2
# print(data.info)
# print(data.describe)
# print(data.columns)

#Task-3
# print(data["First Name"])
# print(data[["Country","Email"]])

#task-4
japan=data[data["Country"]=="Japan"]
print(japan)

print(data["Country"]=="Japan")
# print(data["Country"]=="Bangladesh")

print(data["Email"].str.endswith(".org"))


# print("Total count:",data.count())
# print("Average:",data.min())
# print("Max",data.max())
