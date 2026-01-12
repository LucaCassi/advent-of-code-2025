from pathlib import Path


def compute_maximum_joltage_sum(folder_name: str, file_name: str) -> int:
    joltage_sum = 0

    path = Path(folder_name)/file_name

    with path.open("r", encoding="utf-8") as f:
        for raw in f:                                 # cannot use the raw directly
            line = raw.strip()                        # remove newline characters (e.g. "\n")

            max_digit = 0                             # tracks the maximum digit found so far

            for index in range(len(line)-1):
                if int(line[index]) > max_digit:
                    first_digit_index = index         # store the (first) index of the highest digit
                    max_digit = int(line[index])

                if max_digit == 9: break              # early exit: 9 is the maximum possible digit

            max_digit = 0                             # reset for second digit search

            for index in range(first_digit_index+1,len(line)):
                if int(line[index]) > max_digit:
                    second_digit_index = index
                    max_digit = int(line[index])

                if max_digit == 9: break              # early exit

            joltage_sum += int(line[first_digit_index])*10 + int(line[second_digit_index])

    return joltage_sum


if __name__ == "__main__":
    maximum_joltage_sum = compute_maximum_joltage_sum("Input_folder","Day_3_puzzle_input.txt")
    print("Maximum Joltage Sum :", maximum_joltage_sum)
