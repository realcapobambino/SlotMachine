
import random

INITIAL_BALANCE = 0

MIN_DEPOSIT = 100

MAX_LINES = 4
MAX_BET = 1000
MIN_BET = 5

# reels in slot machine
ROWS = 4
COLS = 3

# dictionary
# symbols to choose in each reel
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
    "E": 10
}

# set score multipliers
symbol_value = {
    "A": 4.5, 
    "B": 3.5,
    "C": 2.5,
    "D": 1.5,
    "E": 1
}

def check_winnings(columns, lines, bet, symbol_value):

    winnings = 0

    winning_lines = []

    # loop through every row the user bet on
    for line in range(lines):
        # check the symbol of the first column of the current row - because all symbols need to be the same in order to win
        symbol = columns[0][line]
        # loop every column and check for the symbol
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break # break the for-loop
        else:
            winnings += symbol_value[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines




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
                print(column[row], end=" | ") # end="\n" - default: new line - tells print statement what to end with
            else:
                print(column[row], end="")
        
        print()


# collect user input
def deposit(balance):
    
    while True:
        amount = 0
        amount = input(f"Enter your deposit. Kes. (Minimum Deposit is Kes. {MIN_DEPOSIT}): ")
        print()
        # check if amount is a number
        if amount.isdigit():
            # convert to int
            amount = int(amount)
            # check if amount is greater than 100
            if amount >= MIN_DEPOSIT:
                balance += amount
                print(f"Deposit Successful!. Your new balance is Kes. {balance}")
                print()
                break
            else:
                print(f"Deposit must be atleast Kes. {MIN_DEPOSIT} and above!")
                print()
        else:
            print("Please enter a number.")
            print()
    # balance = INITIAL_BALANCE + amount
        
    return amount


def get_number_of_lines():
    while True:
        print("Let's begin...")
        lines = input("Enter the number of lines to bet on. (1 - " + str(MAX_LINES) + ")? ")
        print()
        # check if lines is a number
        if lines.isdigit():
            # convert to int
            lines = int(lines)
            # check if lines is between 1 and maximum set lines
            if 1 <= lines <= MAX_LINES:
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
            # check if amount is within betting limits
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount MUST be between Kes. {MIN_BET} - Kes. {MAX_BET}.")
                print()
        else:
            print("Please enter a number.")
            print()
    return amount


def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Sorry. You do not have enough to bet that amount.")
            print(f"Your total bet is {total_bet}")
            print(f"Your current balance is: Kes. {balance}")
            print()
        else:
            break    
    print(f"You are betting Kes. {bet} on {lines} lines.", end="\n")
    print(f"Your total bet is: Kes. {total_bet}.")
    print(f"Your remaining balance will be Kes. {balance - total_bet}")
    print()

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print()
    print(f"You won Kes. {winnings}.")
    print(f"You won on lines: ", *winning_lines) # * is a splat/unpack operator - pass every single line from the winning lines list to the print function


    print()

    return winnings - total_bet

def main():
    print("Welcome to the SLOT Machine!!")
    print()
    print("Please make a deposit first")
    print()
    balance = INITIAL_BALANCE
    # balance += deposit()
    while True:
        print(f"Current balance is Kes. {balance}")
        print()
        prompt = input(f"Press P to Play. Press d to deposit. (q to quit) : ")
        print()
        if prompt == "q" or prompt == "Q":
            break        
        elif prompt == "d" or prompt == "D":
            balance += deposit(balance)
        elif prompt == "p" or prompt == "P":
            if balance < 10:
                print("Balance too low to play.")
                print(f"Your balance is Kes. {balance}.")
                print()
                prompt_two = input("press d to deposit (q to quit) : ")
                print()
                if prompt_two == "q" or prompt == "Q":
                    break
                elif prompt_two == "d" or prompt == "D":
                    balance += deposit(balance)
                else:
                    print("wrong key pressed. try again.")
                    print()
            balance += spin(balance)
        else:
            print("wrong key pressed. try again...")
            print()
       
    print(f"You left with Kes. {balance}")

main()