import random

points = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
signs = ['HEART', 'CLUB', 'DIAMOND', 'SPADE']


def create_deck(points, signs):
    deck = []
    for sign in signs:
        for point in points:
            deck.append(sign + "-" + point)
    return deck


def display_deck(deck):
    for position, card in enumerate(deck, start=1):
        print(f"Position {position}: {card}")


def king_positions(deck):
    kings = [position for position, card in enumerate(deck, start=1) if "-K" in card]
    return kings
    

deck = create_deck(points, signs)

print('Initial Deck')
display_deck(deck)

print("Initial positions of all Kings:")
print(king_positions(deck))

random.shuffle(deck)

print("\nShuffled Deck:")
display_deck(deck)

print("Shuffled positions of all Kings:")
print(king_positions(deck))