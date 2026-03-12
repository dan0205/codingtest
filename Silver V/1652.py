N=int(input())
ROOM=[input() for _ in range(N)]


def count_seats(lines):
    count = 0
    for line in lines:
        for space in line.split('X'):
            if len(space) >= 2:
                count += 1
    return count

row_count = count_seats(ROOM)
col_count = count_seats("".join(row[i] for row in ROOM) for i in range(N))
print(row_count, col_count)