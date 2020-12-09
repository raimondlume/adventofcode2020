passports = []
current_passport = {}
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# Opens the file.
with open("input.txt") as f:
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

    if field_missing: continue

    # birth year
    if len(passport["byr"]) != 4: continue
    birth_year = int(passport["byr"])
    if not 1920 <= birth_year <= 2002: continue

    # issue year
    if len(passport["iyr"]) != 4:
        continue
    issue_year = int(passport["iyr"])
    if not 2010 <= issue_year <= 2020: continue

    # exp year
    if len(passport["eyr"]) != 4: continue
    exp_year = int(passport["eyr"])
    if not 2020 <= exp_year <= 2030: continue

    # height
    hgt = passport["hgt"]
    if len(hgt) < 3: continue

    unit = hgt[-2:]
    if not unit.isalpha(): continue
    if unit != "cm" and unit != "in": continue

    value = hgt[:-2]
    if unit == "cm" and not (150 <= int(value) <= 193): continue
    if unit == "in" and not (59 <= int(value) <= 76): continue

    # hair color
    hcl = passport["hcl"]
    allowed_char = "0123456789abcdef"

    if len(hcl) != 7: continue
    if hcl[0] != "#": continue

    for char in list(hcl[1:]):
        if char not in list(allowed_char): continue

    # eye color
    allowed_valued = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if passport["ecl"] not in allowed_valued: continue

    # passport id
    if len(passport["pid"]) != 9 or not passport["pid"].isnumeric(): continue

    valid_passports_count += 1

print(valid_passports_count)
