import pandas as pd

df = pd.read_csv(f"/home/markus/Temperature_Log_AIM384_2023-03-12T153147.txt", header = 2)
print(df)

df.plot()