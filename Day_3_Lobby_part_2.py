from pathlib import Path
import numpy as np
# DA FARE
def compute_maximum_joltage_sum(folder_name: str, file_name: str) -> int:
    joltage_sum = 0
    path = Path(folder_name)/file_name
    with path.open("r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip() # without .strip, does not work, likely sees "\n"
            ordered_digits_index = np.zeros(12,int)
            last_used_index = -1
            for current_digit in range(len(ordered_digits_index)):
                trailing_value = 0
                for index in range(last_used_index+1 , len(line)-len(ordered_digits_index)+current_digit+1):
                    if int(line[index]) > trailing_value:
                        ordered_digits_index[current_digit] = index
                        last_used_index = index
                        trailing_value = int(line[index])
                    # if trailing_value == 9: break
                joltage_sum += int(line[ordered_digits_index[current_digit]])* 10**(len(ordered_digits_index)-current_digit-1)
    return joltage_sum
                               


if __name__ == "__main__":
    maximum_joltage_sum = compute_maximum_joltage_sum("Input_folder","Day_3_puzzle_input.txt")
    print("Maximum Joltage Sum :", maximum_joltage_sum)