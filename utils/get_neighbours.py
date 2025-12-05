def get_neighbours(arr : list, row : int, col : int, include_diagonals : bool = True, allow_wrapping : bool = False) -> list:
    ROW_LENGTH = len(arr)
    COL_LENGTH = len(arr[row])
    
    neighbours = []

    offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    if include_diagonals:
        offsets.extend([(-1, -1), (-1, 1), (1, -1), (1, 1)])

    for row_offset, col_offset in offsets:
        row_index = row + row_offset
        col_index = col + col_offset

        if allow_wrapping:
            row_index %= ROW_LENGTH
            col_index %= COL_LENGTH
        else:
            if 0 > row_index or row_index >= ROW_LENGTH: continue
            if 0 > col_index or col_index >= COL_LENGTH: continue

        neighbours.append(arr[row_index][col_index])
    return neighbours
        