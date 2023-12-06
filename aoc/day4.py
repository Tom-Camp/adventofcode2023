from typing import List

with open("files/day4", "r") as fp:
    scratch_cards = fp.readlines()


def part_two():
    cards = [1] * len(scratch_cards)
    for index, line in enumerate(scratch_cards):
        card_numbers, my_numbers = map(str.split, line.split("|"))
        copy_count = len(set(card_numbers) & set(my_numbers))
        for copy in range(index + 1, min(index + 1 + copy_count, len(scratch_cards))):
            cards[copy] += cards[index]
    return sum(cards)


def part_one() -> list:
    card_totals: list = []
    for card in scratch_cards:
        card_numbers, my_numbers = map(str.split, card.split("|"))
        winners: List[str] = list(set(card_numbers).intersection(my_numbers))
        if winners:
            total: int = 1
            for x in range(2, len(winners) + 1):
                total = total * 2
            card_totals.append(total)
    return card_totals


def main():
    one = part_one()
    print(f"Part a: {sum(one)}")
    two = part_two()
    print(f"Part b: {two}")


if __name__ == "__main__":
    main()
