import datetime
import sys
sys.path
sys.path.append(r'C:\secure-erp-python-Cyarek')

from model.sales import sales
from model import util as model
from view import terminal as view

CURRENT_DATE = datetime.datetime.now()
CURRENT_DATE = CURRENT_DATE.strftime('%Y-%m-%d')
print(CURRENT_DATE)



def ask_for_details():
    customer_data = []
    customer_data.append(model.generate_id())
    customer_data.append('sztywne id')
    customer_data.append(view.get_input("Please provide product of the new transaction:"))
    customer_data.append(view.get_input("Please provide price of the new transaction:"))
    ask_for_date = view.get_input("Do you want to insert date manually?(yes/no)").lower()
    if ask_for_date == 'yes':
        customer_data.append(view.get_input("Please type in format:yyyy-mm-dd"))#POPRAWIĆ
    elif ask_for_date == 'no':
        customer_data.append(CURRENT_DATE)
    for i in customer_data:
        if i == '':
            customer_data.remove(i)
    if len(customer_data) == 5:
        sales.add_transaction(customer_data)
    else:
        view.clear_console()
        view.print_error_message("All gaps must be filled!")
        run_operation(2)
    
def list_transactions():
    list_of_transactions = sales.list_transactions()
    view.print_table(sales.HEADERS, list_of_transactions)
    return list_of_transactions

def add_transaction():
    list_transactions()
    ask_for_details()
    view.clear_console()
    view.print_message("Transaction has been added!")
    list_transactions()

    
def update_transaction():
    local_list_of_transactions = []
    local_list_of_transactions = list_transactions()
    update_transaction = view.get_input("Please choose your transaction to change by typing id: ")
    zmienna = []
    index_of_transaction = - 1
    condition = 0
    for transaction in local_list_of_transactions:
        index_of_transaction += 1
        if update_transaction == transaction[0]:
            zmienna.append(transaction)
            view.clear_console()
            view.print_table(sales.HEADERS, zmienna)
            condition = 1
            break
        if condition == 0 and index_of_transaction == len(local_list_of_transactions) - 1:
            view.clear_console()
            view.print_error_message("Wrong Id")
            run_operation(3)
    if condition == 1:   
        details_of_update = view.get_input("Choose data to update(product, price, data):").lower() # poprawić! ("All gaps must be filled")
        if (details_of_update == 'product') or (details_of_update == 'price') or (details_of_update == 'data'):
            if details_of_update == 'product':
                local_list_of_transactions[index_of_transaction][2] = view.get_input("Insert new name:")
            if details_of_update == 'price':
                local_list_of_transactions[index_of_transaction][3] = view.get_input("Insert new price:")
            if details_of_update == 'data':  
                local_list_of_transactions[index_of_transaction][4] = view.get_input("Please type in format:yyyy-mm-dd")
            elif (details_of_update != 'product') and (details_of_update != 'price') and (details_of_update != 'data'):
                view.print_error_message("Try one more time")
                run_operation(3)
        elif details_of_update == False:
            view.clear_console()
            view.print_error_message("All gaps must be filled")
            run_operation(3)
        
    sales.update_transaction(local_list_of_transactions)
    view.print_table(sales.HEADERS, local_list_of_transactions)


def delete_transaction():
    local_list_of_transactions_delete = []
    local_list_of_transactions_delete = list_transactions()
    list_of_ids = []
    for lines in local_list_of_transactions_delete:
        list_of_ids.append(lines[0])
    transaction_id = view.get_input("Please select a transaction to delete(ID): ")
    if transaction_id not in list_of_ids:
        view.clear_console()
        view.print_error_message("Wrong ID!")
        run_operation(4)
    for transaction in local_list_of_transactions_delete:
        if transaction_id == transaction[0]:
            local_list_of_transactions_delete.remove(transaction)
    sales.delete_transaction(local_list_of_transactions_delete)
    view.print_message("Selected transaction has been removed")
    view.print_table(sales.HEADERS, local_list_of_transactions_delete)
    # continuing = view.get_input("If you want to delete another transaction, type 'y'")



def get_biggest_revenue_transaction():
    biggest_transactions = list_transactions()
    higher = []
    for elements in biggest_transactions:
        higher.append(elements[3])
    higher = [float(i) for i in higher]
    higher.sort()
    higher_value = higher[-1]
    higher_value_int = int(higher_value)
    higher_value_str = str(higher_value_int)
    for elements in biggest_transactions:
        if higher_value_str == elements[3]:
            view.print_message(f"The biggest revenue has following transaction:\n{elements}")

def get_biggest_revenue_product():
    zmienna = list_transactions()
    product = []
    price = []
    for elements in zmienna:
        product.append(elements[2])
        price.append(elements[3])
    price = [float(i) for i in price]
    dict_biggest = list(zip(product, price))
    dict_bigg = {}
    for element in dict_biggest:
        if element [0] in dict_bigg:
            dict_bigg[element[0]] += element[1]
        else:
            dict_bigg[element[0]] = element[1]
    max_key = max(dict_bigg, key=dict_bigg.get)
    all_values = dict_bigg.values()
    max_value = max(all_values)
    view.print_message(f"Biggest revenue product:\n{max_key} with value {max_value}.")


def count_transactions_between():
    zmienna = list_transactions()
    list_of_date = []
    input_zmienna1 =  (view.get_input("Starting year: ")+'-'+ view.get_input("Starting month: ")+'-'+ view.get_input("Starting day: "))
    view.print_message(f"Starting date is: {input_zmienna1}")
    input_zmienna2 =  (view.get_input("Ending year: ")+'-'+ view.get_input("Ending month: ")+'-'+ view.get_input("Ending day: "))
    view.print_message(f"Starting date is: {input_zmienna2}")
    view.clear_console()
    for elements in zmienna:
        if input_zmienna2 >= elements[4] >= input_zmienna1:
            list_of_date.append(elements[4])
    view.print_table(sales.HEADERS, zmienna)
    view.print_message(f"There were {len(list_of_date)} transactions between {input_zmienna1} - {input_zmienna2}.")

def sum_transactions_between():
    
    zmienna = list_transactions()
    list_of_prices = []
    input_zmienna1 =  (view.get_input("Starting year: ")+'-'+ view.get_input("Starting month: ")+'-'+ view.get_input("Starting day: "))
    view.print_message(f"Starting date is: {input_zmienna1}")
    input_zmienna2 =  (view.get_input("Ending year: ")+'-'+ view.get_input("Ending month: ")+'-'+ view.get_input("Ending day: "))
    view.print_message(f"Starting date is: {input_zmienna2}")
    view.clear_console()
    for elements in zmienna:
        if input_zmienna2 >= elements[4] >= input_zmienna1:
            list_of_prices.append(elements[3])
    list_of_prices = [float(i) for i in list_of_prices]
    sum_transactions = sum(list_of_prices)
    view.print_table(sales.HEADERS, zmienna)
    view.print_message(f"Sum of transaction between {input_zmienna1} - {input_zmienna2} is {sum_transactions}.")



def run_operation(option):
    if option == 1:
        list_transactions()
        question = view.print_message(input("\n\nTo return to sales menu type'back'.").lower())
        # keyboard.wait("Esc")
        if question == 'back':    
            view.clear_console()
    elif option == 2:
        add_transaction()
        question = view.print_message(input("\n\nTo return to sales menu type'back'.").lower())        # keyboard.wait("Esc")
        if question == 'back':    
            view.clear_console()
    elif option == 3:
        update_transaction()
        question = view.print_message(input("\n\nTo return to sales menu type'back'.").lower())
        # keyboard.wait("Esc")
        if question == 'back':    
            view.clear_console()
    elif option == 4:
        delete_transaction()
        question = view.print_message(input("\n\nTo return to sales menu type'back'.").lower())
        # keyboard.wait("Esc")
        if question == 'back':    
            view.clear_console()
    elif option == 5:
        get_biggest_revenue_transaction()
        question = view.print_message(input("\n\nTo return to sales menu type'back'.").lower())
        # keyboard.wait("Esc")
        if question == 'back':    
            view.clear_console()
    elif option == 6:
        get_biggest_revenue_product()
        question = view.print_message(input("\n\nTo return to sales menu type'back'.").lower())
        # keyboard.wait("Esc")
        if question == 'back':    
            view.clear_console()
    elif option == 7:
        count_transactions_between()
        question = view.print_message(input("\n\nTo return to sales menu type'back'.").lower())
        # keyboard.wait("Esc")
        if question == 'back':    
            view.clear_console()
    elif option == 8:
        sum_transactions_between()
        question = view.print_message(input("\n\nTo return to sales menu type'back'.").lower())
        # keyboard.wait("Esc")
        if question == 'back':    
            view.clear_console()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        view.clear_console()
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            view.clear_console()
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)


# list_transactions()
# add_transaction()
# add_transaction()
# update_transaction()
# delete_transaction()
menu()