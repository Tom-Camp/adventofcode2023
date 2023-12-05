import re

with open("files/day4", "r") as fp:
    scratch_cards = fp.readlines()


def get_winners(card: str) -> list:
    game_data = card.split(": ", 1)[1].split(" | ")
    card_numbers = [int(cn) for cn in re.findall(r"\b\d+\b", game_data[0])]
    my_numbers = [int(mn) for mn in re.findall(r"\b\d+\b", game_data[1])]
    winners = list(set(card_numbers).intersection(my_numbers))
    return winners


def part_two() -> list:
    all_cards: list = [c for c in scratch_cards]
    count: int = 0
    for card in all_cards:
        winners = get_winners(card)
        for w in range(count, len(winners)):
            all_cards.append(all_cards[w])
    return all_cards


def part_one() -> list:
    card_totals: list = []
    for card in scratch_cards:
        winners = get_winners(card)
        if winners:
            total: int = 1
            for x in range(2, len(winners) + 1):
                total = total * 2
            card_totals.append(total)
    return card_totals


def main():
    one = part_one()
    print(sum(one))
    two = part_two()
    print(len(two))


if __name__ == "__main__":
    main()
