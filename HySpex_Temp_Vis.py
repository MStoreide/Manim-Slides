import pandas as pd
import numpy as np

# You must be logged in to the Colorlab server to use the script!

# Add lines that loads all the temp files in the folder
# 

temps = np.loadtxt(f"/home/markus/Temperature_Log_AIM384_2023-03-12T153147.txt",
                    skiprows = (2))
HS = pd.DataFrame(temps, columns = ["Time(s)", "Sensor(K)", "Ready"])
print(HS)

# Plot them against each other
HS.plot()

# Impleent so that it prints the date of the measurement. Maybe as the DF name?