passports = []
current_passport = {}
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# Opens the file.
with open("../input.txt") as f:
    for line in f:
        line = line.strip()

        if len(line) < 1:
            passports.append(current_passport)
            current_passport = {}
            continue

        for item in line.split(" "):
            x = item.split(":")
            current_passport[x[0]] = x[1]

f.close()

valid_passports_count = 0
for passport in passports:
    field_missing = False
    for field in required_fields:
        if field not in passport.keys():
            field_missing = True

    if not field_missing:
        valid_passports_count += 1

print(valid_passports_count)
