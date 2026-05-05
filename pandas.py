'1. Installing and Importing Pandas
pip install pandas
import pandas as pd

----------------------------------------------------------

'2. Creating DataFrames
import pandas as pd
data = {
    'Name': ["Player_A", "Player_B", "Player_C"],
    'Age': [25, 30, 35]}
    
df = pd.DataFrame(data)

print(df)
Output:

out1
DataFrame

---------------------------------------------------

'3. Creating Series
import pandas as pd
age_series = pd.Series([25, 30, 35], index=["Player_A", "Player_B", "Player_C"])
print(age_series)
Output:

out-2
Series

----------------------------------------------------------

'4.Reading CSV and JSON Files
import pandas as pd 
df = pd.read_csv("people.csv")
print(df)
Output:


import pandas as pd
df = pd.read_json('data.json')
print(df)

---------------------------------------------------------

'5. Understanding and Analyzing the Data Frame
head(): View the first n rows of the DataFrame (default is 5 rows).
tail(): View the last n rows of the DataFrame (default is 5 rows).
info(): This method provides a concise summary of the DataFrame, including the number of non null entries, column names and data types.
describe(): Generates summary statistics like count, mean and standard deviation for numerical columns. Use .describe(include='all') to include non numeric columns as well.
Let's see an example demonstrating the use of .head(), .tail(), .info() and .describe() methods:

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [24, 27, 22, 32, 29],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
df = pd.DataFrame(data)

print("First 3 rows using head():")
print(df.head(3))

print("\nLast 2 rows using tail():")
print(df.tail(2))

print("\nDataFrame summary using info():")
df.info()
Output:


Understanding Data in Pandas
Pandas offers versatile tools for viewing and inspecting data, enabling to quickly summarize or dive deeper into specific data attributes. To explore more advanced functionalities in Pandas, you can follow the links below:

View basic statistical details
Get information about the DataFrame (data types, non-null counts, etc.)
Check for missing data
Inspect the DataFrame shape (rows and columns)
Checking rows with minimum and maximum values
6. Indexing in Pandas
Indexing in Pandas refers to process of accessing and selecting data from a Pandas DataFrame or Series. There are multiple ways to do this. We will cover how to basic indexing, select specific columns , apply slicing and use Boolean indexing to filter data efficiently.

Example : Basic Indexing( Selecting a single column ) with use of [ ] operator:




import pandas as pd
​
data = {'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35]}
df = pd.DataFrame(data)
​
age_column = df['Age']
print(age_column)
Output:

out5
Indexing
You can select multiple columns in a DataFrame by passing a list of column names. For example, using ['Name', 'Age'] will return both columns together as a new DataFrame .When selecting rows, Pandas provides two main methods:

.loc[] : Used for label based indexing. You select rows using their index labels (the actual row names or index values).
.iloc[] : Used for position based indexing. You select rows using their integer positions (like 0 for first row, 1 for second row).

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

row_by_label = df.loc[1]  
row_by_position = df.iloc[1]  

print("Row by label:\n", row_by_label)
print("\nRow by position:\n", row_by_position)
Output:

out4
Indexing
For more examples where we have covered selecting single and multiple columns and row based selection, Indexing and Selecting Data with Pandas. Explore the following resources for advanced indexing techniques:

Using loc[] and iloc[] for Advanced Row and Column Selection
Boolean Indexing in Pandas
Slicing dataFrames and series
7. Selecting and Filtering Data Based on Conditions
Selecting and filtering data after indexing means narrowing down the dataset by applying conditions to choose only the rows or columns that meet specific criteria. Instead of using the entire dataset, we apply logical conditions to extract only the relevant data needed for analysis.
In this example, we filter the rows where the Age column is greater than 30. This condition narrows the dataset to only those rows that satisfy the requirement.
For additional methods, you can refer to the page Selecting Rows from a DataFrame Based on Column Values.

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35]}
df = pd.DataFrame(data)
filtered_df = df[df['Age'] > 28]

print(filtered_df)
You can also refer to following resources for advanced techniques and more conditions in filtering and selection:

Select Rows With Multiple Filters in Pandas
Filtering by Column Value
Filter rows based on a list of values
Filter Pandas Dataframe with multiple conditions
8. Dealing with Rows and Columns in Pandas DataFrame
It involves various data manipulation techniques in Pandas, such as adding and deleting columns, truncating data, iterating over DataFrames and sorting data. For more detailed explanations of each concept and step, you can refer to Dealing with Rows and Columns in Pandas DataFrame.

1. Adding a New Column to DataFrame: There are several methods available, each suitable for specific use cases. We can easily add new columns by assigning values to them by direct assignment.


import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})

df['Salary'] = [50000, 60000, 70000]
print(df)
Output:

out6
Adding a new column
There are multiple methods, for that refer to: Adding new column to existing dataFrame in pandas. If you want to add columns from one dataFrame to another, refer to Adding Columns from Another DataFrame.

2. Renaming Columns in a DataFrame: There are multiple ways to rename columns depending on the requirement. We can use the rename() method for selective renaming of specific columns or directly modify the columns attribute when renaming all columns at once.


import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

df.rename(columns={'A': 'X', 'B': 'Y', 'C': 'Z'}, inplace=True)
print(df)
Output:

out7
Renamed Columns
We can also Rename column by index in Pandas

3. Reindexing Data with Pandas: Reindexing allows us to modify the row or column labels of a DataFrame or Series. This is useful for aligning data with a new set of labels, managing missing values and restructuring datasets. The reindex() method helps update row indices or column labels as needed.

Note: If the new index includes labels not present in the original DataFrame, the corresponding values will be set to NaN by default.


import pandas as pd

data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
df = pd.DataFrame(data)

new_index = [0, 1, 2, 3]
df_reindexed = df.reindex(new_index)
print("Reindexed Rows:\n", df_reindexed)
Output:

out8
Reindexed Rows
What if you want to reset the index? for that refer to: Convert Index to Column in Pandas Dataframe

9. Handling Missing Data in Pandas
Working with Missing Data in Pandas is one of the most common tasks in data manipulation. Pandas provides various functions to identify, fill and drop missing values efficiently. To explore the procedure hand to hand in detail refer to below steps:

1. Identifying Missing Data With Pandas using isnull() and notnull():

isnull(): Returns True where values are missing (NaN) and False where values are present.
notnull(): Returns True where values are present and False where they are missing.
Example:


import pandas as pd
import numpy as np
df = pd.DataFrame({'Col1': [1, 2, np.nan],'Col2': [3, np.nan, np.nan]})

print(df.isnull())
Output:

out9
Checking Missing Values
When working with real world datasets, missing values are common. Broadly, we have two main ways to deal with missing data:

Impute (Fill) the missing values
Remove (Delete) the missing values
2. Filling Missing Data: To replace missing values with a specific value, we use the fillna() method.

For example: If you want to fill all missing values with a default value like 0, you can use df.fillna(0). Also we use inplace=True to make changes in our dataset


import pandas as pd
import numpy as np

df = pd.DataFrame({'Col1': [1, 2, np.nan],'Col2': [3, np.nan, np.nan]})
df.fillna(0,inplace=True)

print(df)
Output:

out10
Filled Missing Values with 0
We can also fill missing values with below techniques:

Replacing with the mean, median, or mode of the column
forward fill - Fill missing values with the last valid observation
backward fill- Fill missing values with the next valid observation
3. Dropping Missing Data With Pandas: We can also remove rows or columns that contain missing values using .dropna().

We can remove missing data in different ways depending on the situation. Pandas provides flexible options that allow us to either remove entire columns or selectively drop rows based on specific conditions. Some common approaches include:

Removing columns that contain missing values using df.dropna(axis=1)
Dropping rows where certain columns have missing values using df.dropna(subset=['Column1', 'Column2'])
To explore more variations of dropping data, you can refer to topics like Dropping Rows from a Pandas DataFrame with Missing Values and Dropping One or Multiple Columns.

For example:


import pandas as pd

data = {'Name': ['Alice', 'Bob', None], 'Age': [25, None, 35]}
df = pd.DataFrame(data)
df_dropped = df.dropna()

print(df_dropped)
Output:

out11
Missing Data Dropped
10. Aggregation and Grouping With Pandas
Aggregation and grouping in Pandas are powerful tools for analyzing and summarizing data. Grouping allows to segment your data into categories, while aggregation performs operations (like sum, mean, or count) on these groups to derive insights. groupby() function is commonly used for grouping data, followed by aggregation methods like sum(), mean() or custom functions for statistical analysis.

Example:

groupby('Category'): Groups data by the 'Category' column.
.sum(), .mean(), and .size(): Perform aggregation on the grouped data.

import pandas as pd

data = {'Category': ['A', 'B', 'A', 'B'], 'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data)

grouped_sum = df.groupby('Category').sum()
print("Sum:\n", grouped_sum)

grouped_mean = df.groupby('Category')['Value'].mean()
print("\nMean:\n", grouped_mean)

grouped_agg = df.groupby('Category').agg(['sum', 'mean'])
print("\nAggregated:\n", grouped_agg)
Output:

out12
Grouping in Pandas
For more detailed information and practical examples, refer Grouping and Aggregating with Pandas 
For more advanced operations, you can use .agg() to apply custom aggregation functions.
Grouping Rows in pandas
11. Merging and Concatenating Data in Pandas
This section covers techniques for combining multiple DataFrames or Series into a single DataFrame. These operations are essential for integrating datasets and can be performed in several ways:

1. Merging DataFrames: Combines data based on common column or index using functions like merge or join. There are mainly 4 types of joins:

Inner Join: Keeps rows that match in both DataFrames.
Left Join: Keeps all rows from the left DataFrame and match data from the right.
Right Join and Outer Join: Keep similar but differ in data retention rules.
Example:


import pandas as pd

data1 = {
    'Name': ['Alice', 'Charlie', 'Edward', 'Grace'],
    'Years_Experience': [2, 3, 4, 6]
}
df1 = pd.DataFrame(data1)

data2 = {
    'Name': ['Alice', 'Charlie', 'Frank', 'Grace'],
    'Role': ['Manager', 'Analyst', 'Developer', 'HR']
}
df3 = pd.DataFrame(data2)

df_merged_inner = pd.merge(df1, df3, on='Name', how='inner')

df_merged_outer = pd.merge(df1, df3, on='Name', how='outer')

print("\nInner Merge (Intersection of Names):\n", df_merged_inner)
print("\nOuter Merge (Union of Names):\n", df_merged_outer)
Output:

out13
Merging in Pandas
2. Concatenating Data: Refers to stacking DataFrames either vertically (adding rows) or horizontally (adding columns). This can be achieved using the pd.concat() function. Let's create two dataFrames and concatenate it with the original one:

Example:

By default, pd.concat() concatenates along rows (axis=0), which means the new DataFrame is stacked vertically below the original one.
ignore_index=True ensures that the index is reset, creating a continuous new index instead of keeping the original indices from both DataFrames.

import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Charlie', 'Edward', 'Grace'],
    'Years_Experience': [2, 3, 4, 6],
    'Role': ['Manager', 'Analyst', 'Developer', 'HR']
})


new_df = pd.DataFrame({
    'Name': ['John', 'Lily'],
    'Years_Experience': [5, 3],
    'Role': ['Designer', 'Developer']
})


concatenated_df = pd.concat([df, new_df], ignore_index=True)

print("Concatenated DataFrame:\n")
print(concatenated_df)
Output:

out14
Concatenated Dataframe
Learn Concatenate Two or More Pandas DataFrames with all operations and multiple examples. For more, Go Through below articles:
Concatenate values in different columns to one column
Merge two dataFrames on certain columns
Merge multiple CSV Files into single dataframe
12. Reshaping Data in Pandas
Reshaping data involves changing the structure of rows and columns to better organize or analyze data. Common operations include:

1. Pivot Tables in Pandas: Reshape data based on column values. The .pivot_table() method is particularly powerful for creating aggregated views of data.


import pandas as pd

data = {'Date': ['2024-10-01', '2024-10-01', '2024-10-02', '2024-10-02'],'Category': ['A', 'B', 'A', 'B'],'Values': [10, 20, 15, 25]}
df = pd.DataFrame(data)

pivot_table = df.pivot_table(values='Values', index='Date', columns='Category', aggfunc='sum')
print(pivot_table)
Output:

out15
Pivoting in Pandas
2. Melting : Multiple columns are combined into a single key value pair.

When you melt data:

The column names become the keys.
The values in the columns become the values.
Note: To melt data, you must specify columns that act as "identifiers" (id_vars) and others that need to be melted (value_vars).


import pandas as pd

data = {
    'Date': ['2024-10-01', '2024-10-01', '2024-10-02', '2024-10-02'],
    'Category_A': [10, None, 15, None],
    'Category_B': [None, 20, None, 25]
}

df = pd.DataFrame(data)

melt_df = df.melt(id_vars='Date', 
                  var_name='Category', 
                  value_name='Value')

print(melt_df)
Output:

out16
Melting in Pandas
3. Stacking and Unstacking With Pandas: Reshape the data by changing its rows and columns, particularly when working with MultiIndex DataFrames. These techniques help pivot the layout of your data.

Stacking: Moves the data from columns to rows (making the DataFrame taller).
Unstacking: Moves the data from rows to columns (making the DataFrame wider). Let’s take a simple DataFrame with multiple levels of columns.
Example:

When columns are stacked into rows using stack(), the DataFrame structure changes. The data now has a MultiIndex in the rows:

First level Product (e.g., Product_A, Product_B)
Second level Category (e.g., Sales, Expenses)
The quarter values (Q1, Q2) remain as columns, while the higherlevel column labels move into the row index.

import pandas as pd
data = {
    ('Sales', 'Q1'): [100, 150],
    ('Sales', 'Q2'): [200, 250],
    ('Expenses', 'Q1'): [50, 70],
    ('Expenses', 'Q2'): [80, 90]
}

index = ['Product_A', 'Product_B']
df = pd.DataFrame(data, index=index)
print(df)

stacked_df = df.stack() 
print(stacked_df)

unstacked_df = stacked_df.unstack() 
print(unstacked_df)
