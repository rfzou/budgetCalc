
# Checks which type of input it is, then appends the data to the text file

def write(type, input):
        file = open("data/" + type + ".txt", "a")
        file.write(input + "\n")
        file.close()

def read(type):
    # when the user wants to print all expenses logged (will require
    # timed logging of inputs and creating of new files eventually)
    if type == "all":
        debtFile = open("data/debt.txt", "r+")
        for line in debtFile:
            print(line)
        debtFile.close()

        expenseFile = open("data/expense.txt", "r+")
        for line in expenseFile:
            print(line)
        expenseFile.close()

        incomeFile = open("data/income.txt", "r+")
        for line in incomeFile:
            print(line)
        incomeFile.close()

        otherFile = open("data/other.txt", "r+")
        for line in otherFile:
            print(line)
        otherFile.close()

    else:
        pass

read("all")

# make a .delete function to delete the last line of a file
