import os
import sys

# restarts the current program.
# Note: this function does not return. Any cleanup action (like saving data) must be done before calling this function.
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

ui = input("test: ")

if ui == "1":
    print(ui)
elif ui == "2":
    print(ui)
else:
    restart_program()
