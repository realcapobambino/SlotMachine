# print("Hello World")

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

# collect user input
def deposit():
    while True:
        amount = input("Enter your deposit. Kshs.")
        # check if amount is an int
        if amount.isdigit():
            # convert to int
            amount = int(amount)
            # check if amount is > 0
            if amount > 0:
                break
            else:
                print("Amount MUST be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on. (1-" + str(MAX_LINES) + ")? ")
        # check if lines is a number
        if lines.isdigit():
            # convert to int
            lines = int(lines)
            # check if lines is between 1 and max
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Please enter a number.")
    return lines




def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()