from pathlib import Path


def compute_sum_of_invalid_IDs(folder_name: str, file_name: str) -> int:
    path = Path(folder_name) / file_name

    full_text = path.read_text(encoding="utf-8").strip()  # read entire file as a single string
    string_id_list = full_text.split(",")

    sum_of_invalid_IDs = 0

    for string_interval in string_id_list:                 # (e.g. "123-456")
        lo_hi = string_interval.split("-")
        lowest_number = int(lo_hi[0])
        highest_number = int(lo_hi[1])

        for i in range(lowest_number, highest_number + 1):  # inclusive range
            string = str(i)
            n = len(string)

            '''
            if n % 2 == 0:
                half = n // 2
                if string[half:] == string[:half]:
                    sum_of_invalid_IDs += i
            '''

            invalid = False

            for k in range(1, n // 2 + 1):                  # possible block lengths
                if n % k != 0:
                    continue                                # block size must divide the string length

                block = string[:k]                          # candidate repeating block
                repeats = n // k                            # number of repetitions

                if block * repeats == string:               # check full reconstruction
                    invalid = True
                    break

            if invalid:
                sum_of_invalid_IDs += i

    return sum_of_invalid_IDs


if __name__ == "__main__":
    sum_of_invalid_IDs = compute_sum_of_invalid_IDs("Input_folder", "Day_2_puzzle_input.txt")
    print("Sum of Invalid IDs: ", sum_of_invalid_IDs)
