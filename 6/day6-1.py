count = 0
d = set()

# Opens the file.
with open("../input.txt") as f:
    for line in f:
        line = line.strip()

        if len(line) < 1:
            count += len(d)
            d = set()
            continue

        for item in list(line):
            d.add(item)

f.close()

print(count)
