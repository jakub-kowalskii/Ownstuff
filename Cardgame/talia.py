import random

class Card(object):
    def __init__(self, tarcza, symbol):
        self.tarcza = tarcza
        self.symbol = symbol
    def __unicode__(self):
        return self.show()
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()

    def show(self):
        if self.symbol == 1:
            symbol = "As"
        elif self.symbol == 11:
            symbol = "Walet"
        elif self.symbol == 12:
            symbol = "Królowa"
        elif self.symbol == 13:
            symbol = "Król"
        else:
            symbol = self.symbol

        return "{} {}".format(symbol, self.tarcza)


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    
    def show(self):
        for card in self.cards:
            print (card.show())

    def build(self):
        self.cards = []
        for tarcza in ['kier','trefl','karo','pik']:
            for symbol in range(1,14):
                self.cards.append(Card(tarcza,symbol))

    def shuffle(self, num=1):
        lenght = len(self.cards)
        for i in range (num):
            for a in range(lenght-1, 0, -1):
                randnum = random.randint(0,1)
                if a == randnum:
                    continue
                self.cards[a], self.cards[randnum] = self.cards[randnum], self.cards[a]

    def deal(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name, result=0):
        self.name = name
        self.hand = []
        self.result = result

    def draw(self, deck, num=1):
        for i in range (num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    def showHand(self):
        print ("Karty {} to: {}".format(self.name, self.hand))
        return self

    def discard(self):
        return self.hand.pop()

    def score(self):
        for card in self.hand:
            if card.tarcza == "kier":
                self.result += card.symbol
            elif card.tarcza == "trefl":
                self.result += card.symbol * 2
            elif card.tarcza == "karo":
                self.result += card.symbol * 3
            else:
                self.result += card.symbol * 4


myDeck = Deck()
myDeck.shuffle()
# myDeck.show()


Nickname = str(input("Yer card master name: "))
P1 = Player(f"{Nickname}" + "a", 0)
P2 = Player("", 0)


for e in range(1, 11):
    if e % 2 != 0:
        P1.draw(myDeck, 1)
    else:
        P2.draw(myDeck, 1)


P1.score()
P2.score()

P1.showHand()
P2.showHand()

if P1.result > P2.result:
    print (f"{P1.name} scored {P1.result} and {P2.name} scored {P2.result}. {P1.name} wins!")
elif P1.result < P2.result:
    print (f"{P1.name} scored {P1.result} and {P2.name} scored {P2.result}. {P2.name} wins!")
else:
    print (f"{P1.name} scored {P1.result} and {P2.name} scored {P2.result}. It's a draw!")