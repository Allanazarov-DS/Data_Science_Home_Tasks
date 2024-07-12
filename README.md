# My Python Tasks with Pandas, Seaborn, Matplotlib.pyplot, and NumPy

This repository contains Python scripts and notebooks where I have completed various tasks using Pandas, Seaborn, Matplotlib.pyplot, and NumPy.

## Tasks Completed:
- Analyzed a dataset using Pandas to extract meaningful insights.
- Created visualizations using Seaborn and Matplotlib.pyplot to explore data trends.
- Implemented numerical computations and data manipulation tasks using NumPy arrays.

## Sample Code:
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Example Pandas usage
data = pd.read_csv('data.csv')
print(data.head())

# Example Seaborn and Matplotlib.pyplot usage
sns.pairplot(data)
plt.show()

# Example NumPy usage
arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))    