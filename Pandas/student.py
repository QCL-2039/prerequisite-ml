import pandas as pd
import numpy as np
import random

print("Version of your Numpy:", np.__version__)
print("Version of your pandas:", pd.__version__)

rand = np.random.default_rng()

names = [f"Student_ID{i}" for i in range(1, 11)]
print(names)

marks = rand.integers(low=40, high=100, size=10)
print(marks)
print(type(marks))

gender = random.choices(["Male", "Female"], k=10)
print(gender)
print(type(gender))

data = pd.DataFrame({
    "Names": names,
    "Marks": marks
})

# Additional random columns
attendance = rand.integers(low=0, high=10, size=10)
physics = rand.integers(low=1, high=10, size=10)
chemistry = rand.integers(low=1, high=10, size=10)
biology = rand.integers(low=1, high=10, size=10)

data["Attendance"] = attendance
data["Physics"] = physics
data["Chemistry"] = chemistry
data["Biology"] = biology
data["Total"] = data[["Physics", "Chemistry", "Biology"]].sum(axis=1)
data["Average"] = (data["Total"] / 3).round(2)
data.to_csv("student.csv",index=False)
print(data)
