import random
import os
def clear(): os.system('cls')

class Card:
    def __init__(self, suit, rank):
        self.suit = "Hearts" if suit == 1 else "Diamonds" if suit == 2 else "Clubs" if suit == 3 else "Spades"
        self.rank = "Ace" if rank == 1 else rank if rank < 11 else "Jack" if rank == 11 else "Queen" if rank == 12 else "King"
        self.value = 11 if rank == "Ace" else rank if rank < 11 else 10

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __int__(self):
        return self.value

class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(1, 5):
            for rank in range(1, 14):
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        if len(self.deck) == 0:
            self.repop()

        self.deck.remove(self.deck[0])
        return self.deck[0]

    def repop(self):
        self.deck = []
        for suit in range(1, 5):
            for rank in range(1, 14):
                self.deck.append(Card(suit, rank))
        self.shuffle()

    def sort(self):
        self.deck = []
        for suit in range(1, 5):
            for rank in range(1, 14):
                self.deck.append(Card(suit, rank))

    def print(self):
        for card in self.deck:
            print(card)

deck = Deck()
deck.shuffle()

nPlayers = int(input("Number of players: "))

dHand = []
pHands = [[] for i in range(nPlayers)]
pStatuses = ["Playing" for i in range(nPlayers)]
pHandValues = [0 for i in range(nPlayers)]

for n in range(2):
    dHand.append(deck.draw())
    for i in range(nPlayers):
        pHands[i].append(deck.draw())

print("Dealer's hand: ")
print(dHand[0])
if dHand[0].value == 11:
    print("Checking for blackjack...")
    if dHand[1].value > 9:
        print("Dealer has blackjack! Everyone loses.")
        pStatuses = ["Lost" for i in range(nPlayers)]
elif dHand[0].value > 9:
    print("Checking for blackjack...")
    if dHand[1].value == 11:
        print("Dealer has blackjack! Everyone loses.")
        pStatuses = ["Lost" for i in range(nPlayers)]

print()

if pStatuses[0] != "Lost":
    for i in range(nPlayers):
        print(f"Player {i+1}'s hand:")
        for card in pHands[i]:
            print(card)
        pHandValues[i] = sum([card.value for card in pHands[i]])
        if pHandValues[i] == 21:
            print(f"Blackjack! Player {i+1} wins.")
            pStatuses[i] = "Won"
        print()
    input("Press enter to continue...")
    clear()

for i in range(nPlayers):
    print(f"Player {i+1}'s turn.")
    while pStatuses[i] == "Playing":
        choice = int(input("1. Hit\n2. Stand"))
        clear()
        if choice == 1:
            pHands[i].append(deck.draw())
            print("Hand:")
            for card in pHands[i]:
                print(f"{card}")
            print()
            pHandValues[i] = sum([card.value for card in pHands[i]])
            if pHandValues[i] == 21:
                print("Win")
                pStatuses[i] = "Won"
            elif pHandValues[i] > 21:
                pHands[i].sort()
                if pHands[i][pHands[i].len() - 1].value == 11:
                    pHands[i][pHands[i].len() - 1].value = 1
                print("Bust")
                pStatuses[i] = "Lost"