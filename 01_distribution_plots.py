# -*- coding: utf-8 -*-
"""01_Distribution_plots.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m48O_JykIckdkqtis9Gh_QB54Wmx1RXS

# Introduction to Seaborn
![alt text](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2018/07/seaborn.png)

Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

Important Features of Seaborn
Seaborn is built on top of Python’s core visualization library Matplotlib. It is meant to serve as a complement, and not a replacement. However, Seaborn comes with some very important features. Let us see a few of them here. The features help in −

* Built in themes for styling matplotlib graphics
* Visualizing univariate and bivariate data
* Fitting in and visualizing linear regression models
* Plotting statistical time series data
* Seaborn works well with NumPy and Pandas data structures
* It comes with built in themes for styling Matplotlib graphics

## **About iPython Notebooks**

iPython Notebooks are interactive coding environments embedded in a webpage. You will be using iPython notebooks in this class. You only need to write code between the ### START CODE HERE ### and ### END CODE HERE ### comments. After writing your code, you can run the cell by either pressing "SHIFT"+"ENTER" or by clicking on "Run Cell" (denoted by a play symbol) in the left bar of the cell.


**In this notebook you will learn -**
* Distribution plots
* Categorical plots
* Matrix plots
* Grids
* Regression plots
* Style and color

## Importing Seaborn

To import Seaborn in Colaboratory under the name **sns** type the following:
"""

import seaborn as sns

"""This dataset loads as Pandas DataFrame by default. If there is any function in the Pandas DataFrame, it works on this DataFrame.

Seaborn comes with built-in data sets.Here we will load the **tips** dataset.
"""

tips = sns.load_dataset('tips')

tips.head()

"""## distplot

The distplot shows the distribution of a univariate set of observations.
"""

sns.distplot(tips['total_bill'])
# Safe to ignore warnings

"""To remove the kde layer and just have the histogram use:"""

sns.distplot(tips['total_bill'],kde=False,bins=30)

"""## jointplot

jointplot() allows you to basically match up two distplots for bivariate data. With your choice of what **kind** parameter to compare with: 
* “scatter” 
* “reg” 
* “resid” 
* “kde” 
* “hex”
"""

sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')

sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')

sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')

"""## pairplot

pairplot will plot pairwise relationships across an entire dataframe (for the numerical columns) and supports a color hue argument (for categorical columns).
"""

sns.pairplot(tips)

sns.pairplot(tips,hue='sex',palette='coolwarm')

"""## rugplot

rugplots are actually a very simple concept, they just draw a dash mark for every point on a univariate distribution. They are the building block of a KDE plot:
"""

sns.rugplot(tips['total_bill'])

"""## kdeplot

kdeplots are [Kernel Density Estimation plots](http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth). These KDE plots replace every single observation with a Gaussian (Normal) distribution centered around that value. For example:
"""

# Don't worry about understanding this code!
# It's just for the diagram below
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Create dataset
dataset = np.random.randn(25)

# Create another rugplot
sns.rugplot(dataset);

# Set up the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# 100 equally spaced points from x_min to x_max
x_axis = np.linspace(x_min,x_max,100)

# Set up the bandwidth, for info on this:
url = 'http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth'

bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2


# Create an empty kernel list
kernel_list = []

# Plot each basis function
for data_point in dataset:
    
    # Create a kernel for each point and append to list
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    #Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color = 'grey',alpha=0.5)

plt.ylim(0,1)

# To get the kde plot we can sum these basis functions.

# Plot the sum of the basis function
sum_of_kde = np.sum(kernel_list,axis=0)

# Plot figure
fig = plt.plot(x_axis,sum_of_kde,color='indianred')

# Add the initial rugplot
sns.rugplot(dataset,c = 'indianred')

# Get rid of y-tick marks
plt.yticks([])

# Set title
plt.suptitle("Sum of the Basis Functions")

"""So with our tips dataset:"""

sns.kdeplot(tips['total_bill'])
sns.rugplot(tips['total_bill'])

sns.kdeplot(tips['tip'])
sns.rugplot(tips['tip'])

"""# Great Job!"""