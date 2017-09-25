
# assumes for all write(), that the user wants to write onto numbers.txt
# will append instead of overwritng text
def write(input):
    f = open("numbers.txt", "a")
    f.write(input + "\n")
    f.close()

write("12")
