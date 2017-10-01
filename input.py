import os
import sys
import time
import txt

localtime = time.strftime("%d/%m/%Y")

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Initial code that the terminal will run
init = input("Type of action (expense, income, debt, other, or check): ")

if init.lower() == "expense":
    ex_item = input("What did you buy? ")
    ex_cost = input("How much was it? ")
    ex_list = [ex_item, ex_cost, localtime]
    strl = "|".join(ex_list)
    txt.write("expense", strl)
elif init.lower() == "income":
    inc_action = input("How did you earn the money? ")
    inc_value = input("How much did you earn? ")
    inc_list = [inc_action, inc_value, localtime]
    strl = "|".join(inc_list)
    txt.write("income", strl)
elif init.lower() == "debt":
    debt_person = input("Who owes you? ")
    debt_amount = input("How much does " + debt_person + " owe you? ")
    debt_list = [debt_person, debt_amount, localtime]
    strl = "|".join(debt_list)
    txt.write("debt", strl)
elif init.lower() == "other":
    other_item = input("What did you spend it on? ")
    other_cost = input("How much was it?")
    other_list = [other_item, other_cost, localtime]
    strl = "|".join(other_list)
    txt.write("other", strl)
elif init.lower() == "check":
    print("Feature coming soon!")
else:
    print("That is not a valid input, please try again.")
    restart_program()

