lines = []
count = 0
# Opens the file.
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if len(line) < 1: continue
        line = line.split()
        lines.append({"index": count, "op": line[0], "arg": int(line[1])})
        count += 1

acc = 0
nxt = 0
history = []

while True:
    line = lines[nxt]
    history.append(nxt)

    if line["op"] == "jmp":
        nxt += line["arg"]

    if line["op"] == "nop":
        nxt += 1

    if line["op"] == "acc":
        acc += line["arg"]
        nxt += 1

    if nxt in history:
        break

print(acc)
