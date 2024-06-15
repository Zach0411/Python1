import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x = np.random.randint(1,7,100)
plt.hist(x)
plt.title('sample histogram')
plt.xlabel('Numbers')
plt.ylabel('Count')
plt.show()