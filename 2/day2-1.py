lst = []
count = 0

# Opens the file.
with open("../input.txt") as f:

    # Loops over the file one line at a time.
    for line in f:
    # Prints the current line
        count += 1
        line = line[:-1] # remove /n
        two_parts = line.split(": ")
        # print(two_parts)

        password = two_parts[1]
        letter = two_parts[0].split(" ")[1]
        min_amount = int(two_parts[0].split(" ")[0].split("-")[0])
        max_amount = int(two_parts[0].split(" ")[0].split("-")[1])

        letter_count = password.count(letter)

        if (min_amount <= letter_count <= max_amount):
            lst.append(password)

f.close()

print(len(lst))
print(count)