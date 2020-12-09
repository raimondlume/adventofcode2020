count = 0
group_count = 0
d = set()
dct = {}

# Opens the file.
with open("../input.txt") as f:
    for line in f:
        line = line.strip()

        if len(line) < 1:
            for key in dct.keys():
                if dct[key] == group_count:
                    count += 1
            group_count = 0
            dct = {}
            continue

        group_count += 1
        for item in list(line):
            d.add(item)
            if item not in dct.keys():
                dct[item] = 1
            else:
                dct[item] += 1


f.close()

print(count)
