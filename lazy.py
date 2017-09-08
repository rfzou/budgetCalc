import os
import sys
import time

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


init = input("Type of action (expense, income, debt, or other): ")

loi = []

if init == "expense":
    ex_item = input("What did you buy? ")
    ex_cost = input("How much was it? ")

elif init == "income":
    inc_action = input("How did you earn the money? ")
    inc_value = input("How much did you earn? ")
elif init == "debt":
    debt_person = input("Who owes you? ")
    debt_amount = input("How much does" + debt_person + "owe you? ")
elif init == "other":
    other_item = input("What did you spend it on? ")
    other_cost = input("How much was it?")
else:
    print("That is not a valid input, please try again.")
    restart_program()

