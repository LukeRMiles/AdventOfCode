from utils import *

def is_hori(p1, p2):
    return p1[1] == p2[1]

def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def check_vert_intersect(hori_segments, p1, p2):
    xv = p1[0]
    y1, y2 = sorted((p1[1], p2[1]))

    for a, b in hori_segments:
        yh = a[1]
        xh1, xh2 = sorted((a[0], b[0]))

        if not (y1 <= yh <= y2):
            continue
        if not (xh1 <= xv <= xh2):
            continue

        intersection = (xv, yh)

        if intersection == p1 or intersection == p2 or intersection == a or intersection == b:
            continue
        return True

    return False

def check_hori_intersect(vert_segments, p1, p2):
    yv = p1[1]
    x1, x2 = sorted((p1[0], p2[0]))

    for a, b in vert_segments:
        xv = a[0]
        yv1, yv2 = sorted((a[1], b[1]))

        if not (x1 <= xv <= x2):
            continue
        if not (yv1 <= yv <= yv2):
            continue

        intersection = (xv, yv)

        if intersection == p1 or intersection == p2 or intersection == a or intersection == b:
            continue

        return True
    return False

def point_on_segment(pt, a, b):
    x, y = pt
    x1, y1 = a
    x2, y2 = b

    if x1 == x2:
        if x != x1:
            return False
        return min(y1, y2) <= y <= max(y1, y2)

    if y1 == y2:
        if y != y1:
            return False
        return min(x1, x2) <= x <= max(x1, x2)
    return False

def point_in_or_on_polygon(pt, vertices):
    if pt in vertices:
        return True

    for i in range(len(vertices)):
        if point_on_segment(pt, vertices[i], vertices[(i+1) % len(vertices)]):
            return True

    x, y = pt
    inside = False
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1) % len(vertices)]

        if (y1 > y) != (y2 > y):
            x_int = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
            if x_int > x:
                inside = not inside
    return inside

def solution(lines : list[str]):
    reds = []

    hori_segments = set()
    vert_segments = set()

    for line in lines:
        reds.append(tuple(map(int, line.split(","))))

    for i in range(len(reds)):
        first = reds[i]
        second = reds[(i + 1) % len(reds)]

        if is_hori(first, second):
            hori_segments.add((first, second))
        else:
            vert_segments.add((first, second))

    curr_max = 0
    for i, first in enumerate(reds):
        for second in reds[i + 1:]:
            a = area(first, second)

            if a < curr_max:
                continue

            if first[0] == second[0] or first[1] == second[1]:
                continue

            corner1 = (first[0], second[1])
            corner2 = (second[0], first[1])

            if (check_vert_intersect(hori_segments, first, corner1) or
                check_hori_intersect(vert_segments, corner1, second) or
                check_vert_intersect(hori_segments, second, corner2) or
                check_hori_intersect(vert_segments, corner2, first)):
                continue

            if (not point_in_or_on_polygon(corner1, reds) or
                not point_in_or_on_polygon(corner2, reds)):
                continue

            curr_max = a
    return curr_max
    

if __name__ == "__main__":
    lines = read_input("2025/day9_input.txt")

    print(solution(lines))