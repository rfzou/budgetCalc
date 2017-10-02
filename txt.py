import os
import sys

# Checks which type of input it is, then appends the data to the text file
def write(type, input):
        file = open("data/" + type + ".txt", "a")
        file.write(input)
        file.close()

write("debt", "thing")

def readPrint(type):
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
        quit()


# Deletes the last line of any file if the user made a mistake

def undo(type):
    file = open("data/" + type + ".txt", "r+", encoding="utf-8")

    # Move the pointer (similar to a cursor in a text editor) to the end of the file.
    file.seek(0, os.SEEK_END)

    # This code means the following code skips the very last character in the file -
    # i.e. in the case the last line is null we delete the last line
    # and the penultimate one
    pos = file.tell() - 1

    # Read each character in the file one at a time from the penultimate
    # character going backwards, searching for a newline character
    # If we find a new line, exit the search
    while pos > 0 and file.read(1) != "\n":
        pos -= 1
        file.seek(pos, os.SEEK_SET)

    # So long as we're not at the start of the file, delete all the characters ahead of this position
    if pos > 0:
        file.seek(pos, os.SEEK_SET)
        file.truncate()

    file.close()

