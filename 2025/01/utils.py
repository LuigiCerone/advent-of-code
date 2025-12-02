def read_instructions(filename: str) -> list[tuple[str, int]]:
    input_list = []
    with open(filename, "r") as file:
        input_list = [
            (line[0], int(line[1:])) for line in file.read().strip().split("\n")
        ]

    return input_list
