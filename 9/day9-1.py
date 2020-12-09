body = []
# Opens the file.
with open("../input.txt") as f:
    for line in f:
        body.append(int(line))

count = 0
cache = {}
preamble_length = 25
for num in body:
    possible_sums = []
    if count >= preamble_length:
        for x in body[count - preamble_length:count]:
            for y in body[count - preamble_length:count]:
                if x != y:
                    possible_sums.append(x+y)
        if num not in possible_sums:
            print(f"Answer: {num}")
            break
    count += 1
