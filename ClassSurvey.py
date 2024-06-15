import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
#loading csv file
df = pd.read_csv(r'C:\Users\saint\OneDrive\Desktop\Surveyinfo.csv')
x = df["RAM (in GB)"]
plt.hist(x)
plt.title("Quantity of RAM")
plt.xlabel("RAM (in GB)")
plt.ylabel("Frequency")
plt.show()