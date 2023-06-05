import os
import pandas as pd
import matplotlib.pyplot as plt

def load_txt_files(folder_path):
    dataframes = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(file_path, delimiter='\t')  # Assuming tab-separated values
            dataframes.append(df)
    return dataframes

# Specify the folder path where the .txt files are located
folder_path = '/path/to/your/folder'

# Load the .txt files as separate pandas DataFrames
loaded_dataframes = load_txt_files(folder_path)

# Access the individual DataFrames
for i, df in enumerate(loaded_dataframes):
    print(f"DataFrame {i+1}:")
    print(df.head())  # Print the first few rows of each DataFrame
    print()

    # Plot the values in the DataFrame
    plt.plot(df.index, df.values)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title(f"DataFrame {i+1} Values")
    plt.show()
