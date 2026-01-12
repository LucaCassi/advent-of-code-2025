from pathlib import Path
import numpy as np                           # used here for fixed-size integer arrays

TOTAL_DIGITS = 12

def compute_maximum_joltage_sum(folder_name: str, file_name: str) -> int:
    joltage_sum = 0

    path = Path(folder_name)/file_name

    with path.open("r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()                       # remove newline characters

            ordered_digits_index = np.zeros(TOTAL_DIGITS,int)  # stores indices of selected digits (fixed length)
            last_used_index = -1

            for current_digit in range(len(ordered_digits_index)):
                trailing_value = 0                  # maximum digit found for the current position

                for index in range(last_used_index + 1   ,   len(line) - len(ordered_digits_index) + current_digit + 1):
                    if int(line[index]) > trailing_value:
                        ordered_digits_index[current_digit] = index  # store index of best candidate
                        last_used_index = index                       # update last used index
                        trailing_value = int(line[index])             # update maximum digit

                    if trailing_value == 9: break                   # optional early exit

                joltage_sum += int(line[ordered_digits_index[current_digit]]) * 10**(len(ordered_digits_index) - current_digit - 1)
                # place the selected digit at the correct decimal position and accumulate

    return joltage_sum                               # final joltage sum


if __name__ == "__main__":
    maximum_joltage_sum = compute_maximum_joltage_sum("Input_folder","Day_3_puzzle_input.txt")
    print("Maximum Joltage Sum :", maximum_joltage_sum)
