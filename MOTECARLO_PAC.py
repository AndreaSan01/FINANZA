import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import random


tickers = ["^IXIC", "^GSPC", "^DJI", "^FCHI"]
starting_date = "1900-01-01"
#ending_date = "2024-01-01"
ending_date = datetime.today()
ending_date = ending_date.date()
ending_date = ending_date.strftime("%Y-%m-%d")
data = pd.DataFrame()

for ticker in tickers:
        data[ticker] = yf.download(ticker, start=starting_date, end=ending_date)["Adj Close"]



sns.set_style("dark")  # Set a background style (optional)
# Create the plot with Seaborn functions
fig, ax = plt.subplots(figsize=(12, 6))  # Adjust figure size as needed
# Line plot with color based on column names (assuming columns are indices)
sns.lineplot(data=data)
# Customize the plot
plt.title("Historical Closing Prices")
plt.legend(title="Indices")  # Adjust legend title if needed
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
# Improve spacing and display
plt.tight_layout()
plt.show()
data = data.reset_index()


#for i in data['Date']:

    #month = i.month 
    #while(month==i.month):
    #    index_start = data.iloc[data['Date'] == i].index
     #   print(index_start) 
    