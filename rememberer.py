import sys

def rememberer(thing):
    #open file
    with open("database.text", "a") as file:
        # write thing to file
        file.write(thing+"\n")


def show():
    # open file
    with open('database.txt') as file:
        for line in file:
            print(line)
    # print out each line in file
    # close file
    pass

if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        rememeberer(' '.join(sys.argv[1:]))