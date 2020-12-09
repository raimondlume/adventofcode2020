lst = []
count = 0

lut = {"F": "0", "B": "1", "L": "0", "R": "1"}

# Opens the file.
with open("input.txt") as f:
    for line in f:
        row_bin = ""
        for char in line.strip()[:-3]:
            row_bin += lut[char]
        col_bin = ""
        for char in line.strip()[-3:]:
            col_bin += lut[char]

        row = int(row_bin, 2)
        col = int(col_bin, 2)

        ticket_id = row * 8 + col
        lst.append(ticket_id)
f.close()

lst.sort()
# print(lst)

for i in lst:
    if i + 2 in lst and i + 1 not in lst:
        print(i + 1)
