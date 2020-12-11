with open("input.txt") as f:
    rows = [line.strip() for line in f.readlines()]

seats = {}
for y, row in enumerate(rows):
    for x, seat in enumerate(row):
        seats[(x, y)] = seat

finished = False
new_seats = seats.copy()


def seat_in_direction(x, y, dx, dy, _seats):
    while True:
        x += dx
        y += dy

        if (x, y) not in _seats:
            return '.'

        seat = _seats.get((x, y))
        if seat == 'L':
            return 'L'
        if seat == '#':
            return '#'


while not finished:
    finished = True
    seats = new_seats.copy()
    new_seats = {}

    for (x, y), seat in seats.items():
        directions = [(-1, -1), (0, -1), (1, -1),
                      (-1,  0),          (1,  0),
                      (-1,  1), (0,  1), (1,  1)]
        neighbor_count = [seat_in_direction(x, y, direction[0], direction[1], seats) for direction in directions].count('#')

        if seat == 'L' and neighbor_count == 0:
            new_seats[(x, y)] = '#'
            finished = False
        elif seat == '#' and neighbor_count >= 5:
            new_seats[(x, y)] = 'L'
            finished = False
        else:
            new_seats[(x, y)] = seat

print(f'{list(new_seats.values()).count("#")} seats occupied')
