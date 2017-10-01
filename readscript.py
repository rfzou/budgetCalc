
debtStr_a = "name name2|cost|date"

# turns the raw input from input.py to a list of the known values
def break_input(input):
    input = input.split("|")
    print(input)

break_input(debtStr_a)