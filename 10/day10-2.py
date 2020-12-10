import collections

adapters = []

# Opens the file.
with open("input.txt") as f:
    for line in f:
        adapters.append((int(line.strip())))

adapters.sort()
combinations = collections.defaultdict(int, {0: 1})

for adapter in adapters:
    combinations[adapter] = combinations[adapter - 1] + combinations[adapter - 2] + combinations[adapter - 3]

print(combinations[adapters[-1]])
