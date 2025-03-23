FILENAME = "count.txt"
def readNumber():
    with open(FILENAME) as f:
        number1 = int(f.read())
        return number1
# test it
num = readNumber()
print (num)