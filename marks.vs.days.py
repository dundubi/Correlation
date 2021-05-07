import csv
import numpy as np
import plotly.express as px
import pandas as pd

marks = []
days = []

with open("data1.csv") as file :

    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        marks.append(float(row["Marks In Percentage"]))
        days.append(float(row["Days Present"]))

    correlation = np.corrcoef(marks,days)
    print(correlation[0,1])

read = pd.read_csv("data1.csv")
plt = px.scatter(read, x = "Marks In Percentage", y = "Days Present")
plt.show()