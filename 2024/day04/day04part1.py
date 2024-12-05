with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")  # Use splitlines for better splitting
    print(f"Lines: {lines}")  # Debugging: check how lines are being split
fin.close()
n = len(lines)
print(f"Number of rows (n): {n}")
if n > 0:
    m = len(lines[0])
else:
    m = 0
print(f"Number of columns (m): {m}")

# Generate all directions
dd = []
for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx != 0 or dy != 0:
            dd.append((dx, dy))

# dd = [(-1, -1), (-1, 0), (-1, 1),
#       (0, -1),           (0, 1),
#       (1, -1), (1, 0), (1, 1)]

def has_xmas(i, j, d):
    dx, dy = d
    for k, x in enumerate("XMAS"):
        ii = i + k * dx
        jj = j + k * dy
        if not (0 <= ii < n and 0 <= jj < m):
            return False
        if lines[ii][jj] != x:
            return False
    return True

# Count up every cell and every direction
ans = 0
for i in range(n):
    for j in range(m):
        for d in dd:
            ans += has_xmas(i, j, d)

print(ans)