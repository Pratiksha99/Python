# -*- coding: utf-8 -*-
"""04_Missing_Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sgcu9B20k6zKvTQQogTNa3Z7jVMjXhzQ

# Introduction to Pandas

![alt text](http://i1.wp.com/blog.adeel.io/wp-content/uploads/2016/11/pandas1.png?zoom=1.25&fit=818%2C163)

Pandas is an open-source, BSD-licensed Python library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. You can think of pandas as an extremely powerful version of Excel, with a lot more features.

## **About iPython Notebooks**

iPython Notebooks are interactive coding environments embedded in a webpage. You will be using iPython notebooks in this class. You only need to write code between the ### START CODE HERE ### and ### END CODE HERE ### comments. After writing your code, you can run the cell by either pressing "SHIFT"+"ENTER" or by clicking on "Run Cell" (denoted by a play symbol) in the left bar of the cell.

**In this notebook you will learn -**

* Series
* DataFrames
* Missing Data
* GroupBy
* Merging, Joining and Concatenating
* Operations
* Data Input and Output

## Importing Pandas
To import Pandas simply write the following:
"""

import numpy as np
import pandas as pd

"""# Missing Data

Let's show a few convenient methods to deal with Missing Data in pandas:
"""

df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})

df

df.dropna()

df.dropna(axis=1)

df.dropna(thresh=2)

df.fillna(value='FILL VALUE')

df['A'].fillna(value=df['A'].mean())

"""# Great Job!"""