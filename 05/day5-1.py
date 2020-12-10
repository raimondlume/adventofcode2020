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

        print(f"Line: {line.strip()}, row {row} col {col} id {ticket_id}, row_bin {row_bin}, col_bin {col_bin}")

f.close()

print(max(lst))
