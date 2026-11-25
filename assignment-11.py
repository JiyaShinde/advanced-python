import pandas as pd
import numpy as np

# Generate ten random numbers
numbers = np.random.randint(1, 100, 10)

# Create a Pandas Series
series = pd.Series(numbers)

# Display the Series
print(series)
