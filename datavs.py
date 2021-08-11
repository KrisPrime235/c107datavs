import pandas as pd
import plotly.express as pe

data = pd.read_csv("datavs.csv")
lvlmean = data.groupby("level")["attempt"].mean()
fig = pe.scatter(lvlmean, x = lvlmean, y = ["Level 1", "Level 2", "Level 3", "Level 4"], orientation = 'h', size = "attempt", size_max = 10, color = "attempt")
fig.show()
print(lvlmean)