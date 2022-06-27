import pandas as pd
import sqlalchemy
import flask
from flask import jsonify, request
from flask_cors import CORS

engine = sqlalchemy.create_engine("mysql+pymysql://root:admin@192.168.0.50:3306/default")

df = pd.read_sql_table('Transaction_2022', engine)
credit_df = df.loc[df['Transaction Type'] == 'Credit', :]
debit_df = df.loc[df['Transaction Type'] == 'Debit', :]



def get_df():
    # Format: DF name : DB name
    df.rename(columns={
        # 'Transaction Description': 'Transaction Name',
        # 'Date': 'Transaction Date',
        # 'Transaction Amount': 'Purchase Amount',
        # 'Card No.': 'Account number',
        # 'Description': 'Transaction Name',
        # 'Category': 'Transaction Category'
        "Account number": "acc_num",
        "Balance": "balance",
        "Bank name": "bank_name",
        "Comments": "comments",
        "Purchase Amount": "purchase_amt",
        "Transaction Category": "trans_cat",
        "Transaction Date": "trans_date",
        "Transaction Name": "trans_name",
        "Transaction Type": "trans_type"

    }, inplace=True)
    new = df.to_dict('records')  # can also use split, index, tight , records
    return new


# print(get_df())

#
# setting up flask application
app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

# Endpoint to get db.
@app.route('/api/test', methods=['GET'])
def all_trans():
    # calls get_all() and returns content after parsing as json
    return jsonify(get_df()) , {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/header', methods=['GET'])
def get_header():
    # get header values
    debit_sum = round(debit_df['Purchase Amount'].sum())
    credit_sum = round(credit_df['Purchase Amount'].sum())
    net_spending = round(debit_sum + credit_sum)
    transaction_count = len(df)
    dict = {
        'd_sum':debit_sum,
        'c_sum':credit_sum,
        'n_spending':net_spending,
        'trans':transaction_count
    }
    return jsonify(dict)
# Run Statement
app.run()
