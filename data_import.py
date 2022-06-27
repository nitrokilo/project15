# This file is used to import data from csv bank statements to add to database. It formats data to ensure data from csv also matches database. It does this for BOFA
# debit checking and Capital one credit and checking. They are arranged by individual functions.

# # need to add functionality to check for repeat entry before adding to database.
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:admin@192.168.0.50:3306/default")


# function to remove comma from csv entries
def rem_com(y):
    y = str(y)
    for i in y:
        if i == ",":
            y = y.replace(',', '')
            y = float(y)
            return y

    y = float(y)
    return y


# Function to classify entry as debit or credit
def conv(y):
    for i in y:
        if i == ',':
            y = y.replace(',', '')

    y = float(y)
    if y > 0:
        return 'Credit'
    elif y < 0:
        return 'Debit'
    else:
        return ''


def bofa_operations(file):
    # skip intro information of csv
    df = pd.read_csv(file, skiprows=6)
    # skip beginning balance entry
    df = df.drop([0])

    # loop and dictionary to repopulate transaction column
    t_type = []
    for z in range(len(df)):
        t_type.append(conv(df.iloc[z, 2]))

    # Apply remove comma functions to df columns remaining balance and amount.
    df['Amount'] = df['Amount'].apply(rem_com)
    df['Running Bal.'] = df['Running Bal.'].apply(rem_com)

    # Date conversion to match sql standard
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

    # Set default data for columns
    df['Transaction Type'] = t_type
    df['Account number'] = 6314
    df['Bank name'] = 'BOFA'
    df['Transaction Category'] = ' '
    df['Comments'] = ' '

    # Rename columns to match Database
    # Format: DF name : DB name
    df.rename(columns={
        'Description': 'Transaction Name',
        'Date': 'Transaction Date',
        'Amount': 'Purchase Amount',
        'Running Bal.': 'Balance',

    }, inplace=True)

    # Print out df, showing all columns
    print(df.to_string())

    # Push data into db
    df.to_sql(name='Transaction_2022', con=engine, index=False, if_exists='replace')


def capital_one_checking(file):
    # open csv
    df = pd.read_csv(file)

    # Apply remove comma functions to df columns remaining balance and amount.
    df['Transaction Amount'] = df['Transaction Amount'].apply(rem_com)
    df['Balance'] = df['Balance'].apply(rem_com)

    # Date conversion to match sql standard
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], infer_datetime_format=True)

    # Set default data for columns
    df['Bank name'] = 'Capital One; Checking'
    df['Comments'] = ' '

    # Rename columns to match Database
    # Format: DF name : DB name
    df.rename(columns={
        'Transaction Description': 'Transaction Name',
        'Date': 'Transaction Date',
        'Transaction Amount': 'Purchase Amount',
        'Running Bal.': 'Balance'

    }, inplace=True)

    # Print out df, showing all columns
    print(df.to_string())

    # Push data into db
    df.to_sql(name='Transaction_2022', con=engine, index=False, if_exists='append')


def capital_one_credit(file):
    # open csv
    df = pd.read_csv(file)

    # function to remove comma from csv entries
    def rem_com(y):
        y = str(y)
        for i in y:
            if i == ",":
                y = y.replace(',', '')
                y = float(y)
                return y

        y = float(y)
        return y

    # Apply remove comma functions to df columns remaining balance and amount.
    # df['Transaction Amount'] = df['Transaction Amount'].apply(rem_com)
    # df['Balance'] = df['Balance'].apply(rem_com)

    # Pull data from credit and debit columns create list for transaction type and amount
    t_type = []
    t_amount = []
    for z in range(len(df)):
        # multiply both x and y to invert for credit; We want purchases to show as negative transactions, normally they show as positive transactions
        x = df.iloc[z, 5] * -1
        y = df.iloc[z, 6] * -1
        if pd.isna(x):
            t_type.append('Credit')
            t_amount.append(y)
            # print('credit', y)

        if pd.isna(y):
            t_type.append('Debit')
            t_amount.append(x)
            # print('debit', x)

    # Date conversion to match sql standard
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], infer_datetime_format=True)

    # Set default data for columns
    df['Bank name'] = 'Capital One; Credit'
    df['Comments'] = ' '
    df['Transaction Amount'] = t_amount
    df['Transaction Type'] = t_type
    df['Balance'] = 0

    # Rename columns to match Database
    # Format: DF name : DB name
    df.rename(columns={
        'Transaction Description': 'Transaction Name',
        'Date': 'Transaction Date',
        'Transaction Amount': 'Purchase Amount',
        'Card No.': 'Account number',
        'Description': 'Transaction Name',
        'Category': 'Transaction Category'

    }, inplace=True)

    # Remove Posted date, Debit and Credit columns
    df.drop(df.columns[[1, 5, 6]], axis=1, inplace=True)

    # Print out df, showing all columns
    print(df.to_string())

    # Push data into db
    df.to_sql(name='Transaction_2022', con=engine, index=False, if_exists='append')


bofa_operations('stmt.csv')
capital_one_credit('credit.csv')

capital_one_checking('checking.csv')
