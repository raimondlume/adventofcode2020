lst = []

# Opens the file.
with open("../input.txt") as f:

    # Loops over the file one line at a time.
    for line in f:
    # Prints the current line
        lst.append(line[:-1])

f.close()

print(lst)
                
