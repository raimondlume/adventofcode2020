body = []
# Opens the file.
with open("input.txt") as f:
    for line in f:
        body.append(int(line))

count = 0
total_loops = 0
cache = {}
preamble_length = 25
for num in body:
    indx = count + 1
    while sum(body[count:indx]) < 88311123:
        if sum(body[count:indx]) == 88311122:
            min1 = min(body[count:indx])
            max1 = max(body[count:indx])
            print(f"max: {max1}, min: {min1}, min+max: {min1+max1}")
            break
        else:
            total_loops += 1
            indx += 1

    count += 1

print(total_loops)