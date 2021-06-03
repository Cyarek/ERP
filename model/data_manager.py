# Do not modify this file!


def read_table_from_file(file_name, separator=';'):
    """Read CSV file into a data table.

    Args:
        file_name: The name of the CSV data file.
        separator: The CSV separator character

    Returns:
        The data parsed into a list of lists.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [element.replace("\n", "").split(separator) for element in lines]
    except IOError:
        return []


def write_table_to_file(file_name, table, separator=';'):from os import system, name

TABLE_WIDTH = 152
CELL_WIDTH = 30

def clear_console():
    """Clears console."""
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """

    # clear_console()
    print(f"{title}:")
    for option_nr in range(1, len(list_options)):
        print(f"({option_nr}) {list_options[option_nr]}")
    print(f"(0) {list_options[0]}\n")

def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print 
        numbers (like "@label: @value", floats with 2 digits after the decimal),
        lists/tuples (like "@label: \n  @item1; @item2"),
    and dictionaries (like "@label \n  @key1: @value1; @key2: @value2")
    """
    print


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(headers, table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    print("# /", "-"*TABLE_WIDTH)
    print("# |" + "|".join(word.center(CELL_WIDTH," ").upper() for word in headers) + "|")
    print("# /", "-"*TABLE_WIDTH)
    for line in table:
        print("# |" + "|".join(word.center(CELL_WIDTH," ") for word in line) + "|")
        print("# /", "-"*TABLE_WIDTH)


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return input(f"{label}\n")


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    return input(f"{labels}\n")


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)