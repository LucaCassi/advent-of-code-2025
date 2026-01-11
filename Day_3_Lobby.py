from pathlib import Path

def compute_maximum_joltage_sum(folder_name: str, file_name: str) -> int:
    joltage_sum = 0
    path = Path(folder_name)/file_name
    with path.open("r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip() # without .strip, does not work, likely sees "\n"
            max_digit = 0
            for index in range(len(line)-1): # look for the highest first digit
                if int(line[index]) > max_digit:
                    first_digit_index = index
                    max_digit = int(line[index])
                if max_digit == 9: break
            max_digit = 0
            for index in range(first_digit_index+1,len(line)): # look for the highest second digit)
                if int(line[index]) > max_digit:
                    second_digit_index = index
                    max_digit = int(line[index])
                if max_digit == 9: break
            joltage_sum += int(line[first_digit_index])*10 + int(line[second_digit_index])
    return joltage_sum
                               


if __name__ == "__main__":
    maximum_joltage_sum = compute_maximum_joltage_sum("Input_folder","Day_3_puzzle_input.txt")
    print("Maximum Joltage Sum :", maximum_joltage_sum)