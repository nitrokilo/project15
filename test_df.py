## Verified Functions


# Split df into credit and debit df
# credit_df = df.loc[df['Transaction Type'] == 'Credit', :]
# debit_df = df.loc[df['Transaction Type'] == 'Debit', :]

# print only a certain number of results
# df.head(n) ; n is number of results you want.

# Example Sort statement
# df.sort_values(by=['Purchase Amount'], ascending=False)
# print(df.to_string())

# Example custom filter function

# def basic_filter_amount(dataframe, operation, amount):
#     if operation == 'L':
#         new_df = dataframe.loc[df['Purchase Amount'] <= amount, :]
#         return new_df
#
#     if operation == 'G':
#         new_df = dataframe.loc[df['Purchase Amount'] >= amount, :]
#         return new_df
#
#     if operation == 'E':
#         new_df = dataframe.loc[df['Purchase Amount'] == amount, :]
#         return new_df

# date filter function; taking start and end date parameters. Returns new df as result. date format: 'yr-mnt-day'
# def date_filter(s_date, e_date):
#     filtered_df = df.loc[(df['Transaction Date'] >= s_date) & (df['Transaction Date'] < e_date)]
#     return filtered_df

# Example finding sum of column of df
# debit_sum = debit_df['Purchase Amount'].sum()

# Example finding min max values of column
# print(debit_df['Purchase Amount'].min())
# print(credit_df['Purchase Amount'].max())


# Example viewing datatypes of df columns
# print(df.dtypes)

# Get len of df
# print(len(df))
###############################################################################################################

# Playground
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:admin@192.168.0.50:3306/default")

df = pd.read_sql_table('Transaction_2022', engine)
# print(df.to_string())


# Split df into credit and debit df
credit_df = df.loc[df['Transaction Type'] == 'Credit', :]
debit_df = df.loc[df['Transaction Type'] == 'Debit', :]

# print(debit_df.sum())

# print(debit_df.dtypes)

# debit_sum = debit_df['Purchase Amount'].sum()
# print('Debit sum', debit_sum)
#
# credit_sum = credit_df['Purchase Amount'].sum()
# print('Credit Sum', credit_sum)
#
# total_sum = debit_sum + credit_sum
# print('Total Sum', total_sum)

# print(df.dtypes)
# date filter function; taking start and end date parameters. Returns new df as result. date format: 'yr-mnt-day'


#
# def date_filter(s_date, e_date):
#     filtered_df = df.loc[(df['Transaction Date'] >= s_date) & (df['Transaction Date'] < e_date)]
#     return filtered_df


# filtered_df = df.loc[(df['Transaction Date'] > '2022-1-01') & (df['Transaction Date'] < '2022-01-31')]
# print(filtered_df.to_string())


# print(credit_df.to_string())
# debit_df.sort_values(by=['Purchase Amount'], ascending=True, inplace=True)
# print(debit_df.to_string())

# def basic_filter_amount(dataframe, operation, amount):
#     if operation == 'L':
#         new_df = dataframe.loc[df['Purchase Amount'] <= amount, :]
#         return new_df
#
#     if operation == 'G':
#         new_df = dataframe.loc[df['Purchase Amount'] >= amount, :]
#         return new_df
#
#     if operation == 'E':
#         new_df = dataframe.loc[df['Purchase Amount'] == amount, :]
#         return new_df

# new_df = df.loc[df['Purchase Amount'] >= 1000, :]
# print(new_df.to_string())

# filtered_df = df.loc[(df['Transaction Date'] > '2022-1-01') & (df['Transaction Date'] < '2022-01-31')]
# filtered_df.sort_values(by=['Purchase Amount'], ascending=True)
# print(filtered_df.head(7).to_string())

# print(df.to_string())

words = ['Debit Card Purchase - ', 'Digital Card Purchase - ']


# Function to take transaction description and convert to only two word identifier to aid in transaction. Some transaction have similiar first 2 words which lead to hard identification so problem phrase is removed to
# get accurate description. Parameter is transaction name
def short(y):
    # Loop over problem phrases
    for i in words:
        # Search for problem phrase in string, if found index is -1, triggering if conditional.
        a = y.find(i)
        if a != -1:
            # split both problem phrase and transaction description into words
            res = y.split()
            res1 = i.split()
            # Create new list to represented new string with problem phrase
            list_difference = []
            # Use loop to populate new list with no problem phrase
            for element in res:
                if element not in res1:
                    list_difference.append(element)
            # Creation of new word
            final = list_difference[0] + ' ' + list_difference[1]
            # reassign new word for the remaining of function
            y = final

    # Split word into parts
    res = y.split()
    # If category is only one word, return
    if len(res) == 1:
        return y
    # Take first two words and return
    else:
        final = res[0] + ' ' + res[1]
        return final


name = []

# for z in range(len(df)):
#     name.append(short(df.iloc[z, 1]))
#
# df['test'] = name
#
# df['test'] = df['Transaction Name'].apply(short)
#
# short('AMZN Mktp US*8E0D 01/01 PURCHASE Amzn.com/bill WA')
# print(df.to_string())
from cat_algo import home

for x in df['Transaction Name']:
    home(x)


# print(len('PP*APPLE.COM/BIL'))
