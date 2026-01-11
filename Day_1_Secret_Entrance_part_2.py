from pathlib import Path
import math

def compute_password(folder_name: str, file_name: str) -> int:
    path = Path(folder_name) / file_name

    pos = 50
    counter_of_zeros = 0

    with path.open("r", encoding="utf-8") as f:
        for line_num, raw in enumerate(f, start=1):
            line = raw.strip()

            op = line[0]
            if op not in ("L", "R"):
                raise ValueError(f"Line {line_num}: invalid character: {op!r}")

            # do not assume the number of characters for the number
            try:
                value = int(line[1:])
            except ValueError as e:
                raise ValueError(f"Line {line_num}: invalid number: {line[1:]!r}") from e

            if op == "L":
                pos_init = pos
                pos -= value
                counter_of_zeros += (pos_init-1)//100 - (pos-1)//100
                pos %= 100
            else:  # op == "R":
                pos += value
                counter_of_zeros += pos//100
                pos %= 100 # between 0 and 99

    return counter_of_zeros


if __name__ == "__main__":
    password = compute_password("Input_folder", "Day_1_puzzle_input.txt")
    print(f"Password: ", password)