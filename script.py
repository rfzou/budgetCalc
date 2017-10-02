
def dataMorph(type):
    file = open("data/" + type + ".txt")
    lines = file.readlines()
    for line in file:
        line = line.split("|")
        return(line)
    file.close()

print(dataMorph("debt"))