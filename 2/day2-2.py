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
        first_pos = int(two_parts[0].split(" ")[0].split("-")[0]) - 1
        second_pos = int(two_parts[0].split(" ")[0].split("-")[1]) - 1

        if ((password[first_pos] == letter) ^ (password[second_pos] == letter)):
            # print(f"required letter: {letter}, first letter: {password[first_pos]}, second letter: {password[second_pos]}")
            lst.append(password)

f.close()

print(len(lst))
print(count)