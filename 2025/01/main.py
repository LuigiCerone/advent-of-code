from utils import read_instructions


def run_1(instructions_list: list[tuple[str, int]]) -> int:
    curr_value = 50
    count = 0

    for dir, value in instructions_list:
        if dir == "L":
            curr_value = (curr_value - value) % 100
        else:
            curr_value = (curr_value + value) % 100

        if curr_value == 0:
            count += 1

    return count


def run_2(instructions_list: list[tuple[str, int]]) -> int:
    curr_value = 50
    count = 0

    for dir, value in instructions_list:
        if dir == "L":
            if curr_value == 0:
                count += value // 100
            elif value >= curr_value:
                count += 1 + (value - curr_value) // 100
            curr_value = (curr_value - value) % 100
        else:
            count += (curr_value + value) // 100
            curr_value = (curr_value + value) % 100

    return count


if __name__ == "__main__":
    instructions = read_instructions("input.txt")
    r1 = run_1(instructions)
    print(r1)

    r2 = run_2(instructions)
    print(r2)
