#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load data from CSV file
data=pd.read_csv("file:///C:\\Users\\Hp\\Downloads\\happyscore_income.csv",index_col="country")
print(file)


# In[32]:


# Create scatter plot
plt.scatter(data['avg_income'], data['adjusted_satisfaction'])
plt.xlabel('Average Income')
plt.ylabel('Adjusted Happiness Score')
plt.title('Happiness vs. Income')

# Show plot
plt.show()


# In[52]:


import matplotlib.pyplot as plt

# Extract data
x = data['median_income']

# Create histogram with 10 bins
plt.hist(x, bins=10)

# Add title and axis labels
plt.title('Histogram of Median Income')
plt.xlabel('Median Income')
plt.ylabel('Frequency')

# Display plot
plt.show()


# In[53]:


import matplotlib.pyplot as plt

# Extract data
x = data.groupby('region')['avg_income'].mean().sort_values(ascending=False)

# Create bar plot
plt.bar(x.index, x)

# Add title and axis labels
plt.title('Average Income by Region')
plt.xlabel('Region')
plt.ylabel('Average Income')

# Rotate x-axis labels
plt.xticks(rotation=45)

# Display plot
plt.show()

