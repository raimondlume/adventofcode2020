lst = []
x = 5
y = 0
trees = 0
flip = 3

while True:
    # Opens the file.
    with open("../input.txt") as f:
        for line in f:
            line = line[:-1]  # remove /n

            if y == 0:
                y += 1
                continue

            line = line * 10

            x += flip

            if x % 30 == 0:
                flip = flip * -1

            s = list(line)
            s[x] = "🎅"

            if line[x] == "#":
                trees += 1
                s[x] = "💥"

            for index, item in enumerate(s):
                if item == ".":
                    s[index] = "  "
                if item == "#":
                    s[index] = "🎄"
            print("".join(s))
            y += 1

    f.close()

print(trees)
