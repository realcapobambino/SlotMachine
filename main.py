
import random


MIN_DEPOSIT = 100

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

# reels in slot machine
ROWS = 3
COLS = 3

# dictionary
# symbols to choose in each reel
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin(rows, cols, symbols):
    # list of all symbols
    all_symbols =[]
    # iterate though the list dictionary to get values and their keys
    for symbol, symbol_count in symbols.items():
        # _ is an anonymous variable
        for _ in range(symbol_count):
            all_symbols.append(symbol) # e.g symbol A is added 2 times to the list

    # select the values that go to each column

    # an empty list of columns
    columns = [] # will be a nested list [[], [], []]
    # generate column values depending on the number of columns
    for _ in range(cols):
        column = []        
        # make a copy of the all symbols list
        current_symbols = all_symbols[:] # the colon [:] is a slice operator
        # loop through number of values needed which depend on the number of rows in the slot machine
        for _ in range(rows):
            value = random.choice(current_symbols)
            # remove selected value from all symbols list so that it is not selected again
            current_symbols.remove(value)
            # add value to column
            column.append(value)

        # add the generated column to the columns list
        columns.append(column)

    return columns


# transposing(a matrix) to print the columns selected as rows. From _ to |
def print_slot_machine(columns): 
    # detemine the number of rows we have based on the number of elements in each column
    for row in range(len(columns[0])): # assume there is at least 1 column (index 0)
        # loop through all columns and print first value of whatever the index of the current row
        for i, column in enumerate(columns): # enumerate gives the index and item ie column
            # check index; len(columns) - 1 is the max index to access a column in the list
            # to print the pipe
            if i != len(columns) - 1:
                print(column[row], "|")
            else:
                print(column[row])


# collect user input
def deposit():
    print("Welcome to the SLOT Machine!!")
    print()
    while True:        
        amount = input(f"Enter your deposit. Kes. (Minimum Deposit is Kes. {MIN_DEPOSIT}): ")
        print()
        # check if amount is a number
        if amount.isdigit():
            # convert to int
            amount = int(amount)
            # check if amount is greater than 100
            if amount >= MIN_DEPOSIT:
                break
            else:
                print(f"Deposit must be Kes. {MIN_DEPOSIT} and above!")
                print()
        else:
            print("Please enter a number.")
            print()
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on. (1 - " + str(MAX_LINES) + ")? ")
        print()
        # check if lines is a number
        if lines.isdigit():
            # convert to int
            lines = int(lines)
            # check if lines is between 1 and max
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
                print()
        else:
            print("Please enter a number.")
            print()
    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? Kes. ")
        print()
        # check if amount is a digit
        if amount.isdigit():
            # convert to int
            amount = int(amount)
            # check if amount is > 0
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount MUST be between Kes. {MIN_BET} - Kes. {MAX_BET}.")
                print()
        else:
            print("Please enter a number.")
            print()
    return amount





def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Sorry. You do not have enough to bet that amount.")
            print(f"Your current balance is: Kes. {balance}")
            print()
        else:
            break
    
    print(f"You are betting Kes. {bet} on . {lines}.")
    print(f"Your total bet is: Kes. {total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    # print(balance, lines) 


main()