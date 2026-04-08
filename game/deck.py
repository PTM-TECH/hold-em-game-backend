from card import Card
import random

class Deck():
    def __init__(self):
        ranks=Card.RANKS
        suites=Card.SUITES
        deck=[]
        
        for rank in ranks:
            for suite in suites:
                card=Card(suite=suite, rank=rank)
                deck.append(card)
        self.deck=deck
            
    def shuffle(self):
        new_deck=[]
        deck=self.deck
        while True:
            if len(deck) == 1:
                card=deck[0]
                new_deck.append(card)
                break
            n=random.randint(0,len(deck)-1)
            
            card=deck[n]
            deck.pop(n)
            new_deck.append(card)
        self.deck = new_deck
        
    def print_deck(self):
        deck=self.deck
        print("Deck size is", len(deck))
        print("-"*10)
        for card in deck:
            card.print_card()
            print("-"*10)
        
    def burn_card(self):
        print("Before burning deck")
        self.print_deck()
        print("After burning")
        top_card=self.deck[0]
        self.deck.pop(0)
        self.deck.append(top_card)
        self.print_deck()
        
    def give_card(self):
        top_card=self.deck[0]
        self.deck.pop(0)
        return top_card
    
if __name__=="__main__":
    d1=Deck()
    d1.shuffle()
    # d1.burn_card()
    card=d1.give_card()
    print("Given card is")
    card.print_card()
    d1.print_deck()