import random
import time


class PlayingCard:
    card = (6, 7, 8, 9, 10, 'J', "D", 'K', 'A')
    trumps = ("❤️", "♠️", "♦️", "✝️")

    def __init__(self, rank, suit):
        if rank not in self.card:
            raise Exception("Invalid Rank")
        else:
            self.rank = rank
            self.suit = suit

    def __repr__(self):
        return f"Rank: {self.rank}\nSuit: {self.suit}"


card_1 = PlayingCard(random.choice(PlayingCard.card), random.choice(PlayingCard.trumps))
card_2 = PlayingCard(random.choice(PlayingCard.card), random.choice(
    [suit for suit in PlayingCard.trumps if suit != card_1.suit]))


trump = random.choice(PlayingCard.trumps)

print(f"\n{trump.upper()} ARE TRUMP \n")
time.sleep(2)
print(f'{card_1}\n')
time.sleep(2)
print(f'{card_2}\n')
time.sleep(2)

if card_1.suit == trump and card_2.suit == trump:

    if card_1.card.index(card_1.rank) > card_2.card.index(card_2.rank):
        print(f"{card_1.rank} {card_1.suit.upper()} IS WIN")
    else:
        print(f"{card_2.rank} {card_2.suit.upper()} IS WIN")

elif card_1.suit == trump and card_2.suit != trump:
    print(f"{card_1.rank} {card_1.suit.upper()} IS WIN")

elif card_1.suit != trump and card_2.suit == trump:
    print(f"{card_2.rank} {card_2.suit.upper()} IS WIN")

elif card_1.suit != trump and card_2.suit != trump:

    if card_1.card.index(card_1.rank) > card_2.card.index(card_2.rank):
        print(f"{card_1.rank} {card_1.suit.upper()} IS WIN")
    else:
        print(f"{card_2.rank} {card_2.suit.upper()} IS WIN")
