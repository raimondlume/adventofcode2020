import copy

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


jmp_or_nop_lst = filter(lambda l: l["op"] in ["jmp", "nop"], lines)

for case in jmp_or_nop_lst:
    acc = 0
    nxt = 0
    history = []
    temp = copy.deepcopy(lines)
    temp[int(case["index"])]["op"] = "jmp" if temp[case["index"]]["op"] == "nop" else "nop"

    while True:
        line = temp[nxt]
        history.append(nxt)

        if line["op"] == "jmp":
            nxt += line["arg"]

        if line["op"] == "nop":
            nxt += 1

        if line["op"] == "acc":
            acc += line["arg"]
            nxt += 1

        if nxt in history:
            # print(f"Fail: nxt is {nxt}")
            break

        if nxt == len(temp):
            print(f"Success: {acc}")
            break
