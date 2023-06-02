import pandas as pd
import numpy as np

temps = np.loadtxt(f"/home/markus/Temperature_Log_AIM384_2023-03-12T153147.txt",
                    skiprows = (2))

HS = pd.DataFrame(temps, columns = ["Time(s)", "Sensor(K)", "Ready"])
print(HS)
HS.plot()