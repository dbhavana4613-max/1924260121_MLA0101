
from collections import deque

q = deque([(0, 0, [])])
seen = set()

while q:
    a, b, path = q.popleft()

    if (a, b) in seen:
        continue

    seen.add((a, b))
    path = path + [(a, b)]

    if a == 2:
        print("Solution found:")
        for s in path:
            print(s)
        break

    q.extend([
        (4, b, path),
        (a, 3, path),
        (0, b, path),
        (a, 0, path),
        (a - min(a, 3-b), b + min(a, 3-b), path),
        (a + min(b, 4-a), b - min(b, 4-a), path)
    ])
else:
    print("No solution found")
