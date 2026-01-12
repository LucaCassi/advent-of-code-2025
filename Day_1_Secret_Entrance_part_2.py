from pathlib import Path # I try this one instead of os.path

def compute_password(folder_name: str, file_name: str) -> int:
    path = Path(folder_name) / file_name

    pos = 50   # initial position
    counter_of_zeros = 0

    with path.open("r", encoding="utf-8") as f: # f is a file object, closed at the end of the "with" block
        for line_num, raw in enumerate(f, start=1): # I can iterate over f lines; enumerate is used only for the messages of ValueError; will not use it in the next problems
            line = raw.strip()

            op = line[0]
            if op not in ("L", "R"):
                raise ValueError(f"Line {line_num}: invalid character: {op!r}")

            # do not assume the number of characters for the number
            try:
                value = int(line[1:])
            except ValueError as e:
                raise ValueError(f"Line {line_num}: invalid number: {line[1:]!r}") from e

            if op == "L":  # I do not find a way to not use the previous position
                pos_init = pos
                pos -= value
                counter_of_zeros += (pos_init-1)//100 - (pos-1)//100 # without "pos-1" I cannot recognize when I stop exactly at 0
                pos %= 100
            else:  # op == "R":
                pos += value
                counter_of_zeros += pos//100
                pos %= 100 # between 0 and 99

    return counter_of_zeros


if __name__ == "__main__":
    password = compute_password("Input_folder", "Day_1_puzzle_input.txt")
    print(f"Password: ", password)