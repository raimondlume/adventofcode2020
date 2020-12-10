adapters = []

# Opens the file.
with open("input.txt") as f:
    for line in f:
        adapters.append((int(line.strip())))

device_joltage = max(adapters) + 3
current_joltage = 0

one = 0
three = 0

while current_joltage != device_joltage:
    if current_joltage + 1 in adapters:
        one += 1
        current_joltage += 1
        continue
    if current_joltage + 2 in adapters:
        current_joltage += 2
        continue
    if current_joltage + 3 in adapters:
        three += 1
        current_joltage += 3
        continue
    break

print(one)
print(three + 1)  # +1 for final adapter

print(one*(three + 1))
