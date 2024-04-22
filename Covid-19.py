import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("worldometer_data.csv")
print(df)

x=df['TotalCases']
y=df['Population']
plt.plot(x,y)
plt.title("covid-19 case study")
plt.xlabel("No. of total cases")
plt.ylabel("Total Population")
plt.show()