import csv
import plotly.express as px
import pandas as pd
import numpy as np

coffee = []
sleep = []

with open("coffee.vs.sleep.csv") as file:
    readFile = csv.DictReader(file)
    
    for row in readFile :
        coffee.append(float(row["Coffee in ml"]))
        sleep.append(float(row["sleep in hours"]))
    
    correlation = np.corrcoef(coffee,sleep)
    print(correlation[0,1])

plotRead = pd.read_csv("coffee.vs.sleep.py")
plotGraph = px.scatter(plotRead, x = "Coffee in ml", y = "sleep in hours")
plotGraph.show()