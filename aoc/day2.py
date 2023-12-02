def check_dice(dice: list, color: str) -> int:
    for cube in dice:
        if color in cube:
            num = cube.split(" ", 1)
            return num[0]
    return 0


def format_data() -> list:
    """
    Each turn in a game is stored as a tuple. The cubes are indexed as follows:
    blue: 0
    red: 1
    green: 2
    """
    game_data: list = []
    with open("files/day2", "r") as fp:
        lines = fp.readlines()
    for line in lines:
        game = line.split(": ")
        turns = game[1].split("; ")
        turn_data: list = []
        for turn in turns:
            dice = turn.split(", ")
            blue = check_dice(dice=dice, color="blue")
            red = check_dice(dice=dice, color="red")
            green = check_dice(dice=dice, color="green")
            turn_data.append((int(blue), int(red), int(green)))
        game_data.append(turn_data)

    return game_data


game_data = format_data()


def get_part_b() -> int:
    powers: list = []
    for game in game_data:
        blue, red, green = 0, 0, 0
        for turn in game:
            blue = turn[0] if turn[0] > blue else blue
            red = turn[1] if turn[1] > red else red
            green = turn[2] if turn[2] > green else green
        powers.append(blue * red * green)
    return sum(powers)


def get_part_a() -> int:
    red, green, blue = 12, 13, 14
    game_ids: list = []
    for game in game_data:
        okay = True
        for turn in game:
            if turn[0] > blue or turn[1] > red or turn[2] > green:
                okay = False
                break
        if okay:
            game_ids.append(game_data.index(game) + 1)
    return sum(game_ids)


def main():
    answer_a = get_part_a()
    print(f"Part a) {answer_a}")

    answer_b = get_part_b()
    print(f"Part b) {answer_b}")


if __name__ == "__main__":
    main()
