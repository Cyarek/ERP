import sys
sys.path
sys.path.append(r'C:\secure-erp-python-Cyarek')


""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

def list_transactions():
    table = data_manager.read_table_from_file(DATAFILE, ';')
    # print(table)
    return table


def add_transaction(customer_data):
    addd = []
    addd = data_manager.read_table_from_file(DATAFILE, separator=';')
    addd.append(customer_data)
    data_manager.write_table_to_file(DATAFILE, addd, separator=';')
    return addd

def update_transaction(local_list_of_transactions):
    bbb = []
    bbb = local_list_of_transactions
    data_manager.write_table_to_file(DATAFILE, bbb, separator=';')
    return bbb

def delete_transaction(local_list_of_transactions_delete):
    ccc = []
    ccc = local_list_of_transactions_delete
    data_manager.write_table_to_file(DATAFILE, ccc, separator=';')
    return ccc

def get_biggest_revenue_transaction():
    pass

# `list_transactions()`