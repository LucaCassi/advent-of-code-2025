from pathlib import Path


def compute_sum_accessible_rolls(folder_name: str, file_name: str) -> int:
    path = Path(folder_name)/file_name

    sum = 0

    with path.open("r", encoding="utf-8") as f:
        grid = [line.strip() for line in f if line.strip()]    # read grid, removing newline characters and ignoring empty lines

        rows = len(grid)
        cols = len(grid[0])

        adjacent_offsets = [
            (-1, -1), (-1,  0), (-1,  1),
            ( 0, -1),           ( 0,  1),
            ( 1, -1), ( 1,  0), ( 1,  1)
                           ]                            # relative offsets for all 8 neighboring cells

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '@':
                    continue                            # skip non-roll cells

                close = 0

                for row_offset, col_offset in adjacent_offsets:
                    adjacent_row = r + row_offset
                    adjacent_col = c + col_offset
                    if (0 <= adjacent_row < rows and 0 <= adjacent_col < cols and grid[adjacent_row][adjacent_col] == '@'):
                        close += 1                      # valid neighboring roll found

                if close < 4:
                    sum += 1

    return sum



if __name__ == "__main__":
    number_of_accessible_rolls = compute_sum_accessible_rolls("Input_folder", "Day_4_puzzle_input.txt")
    print("Accessible rolls: ", number_of_accessible_rolls)
