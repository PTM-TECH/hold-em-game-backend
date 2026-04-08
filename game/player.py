#human, pc

class Player():
    def __init__(self, type='pc', cards=[], total_bet_amount=0, name="", amount=0):
        self.name=name
        self.type=type
        self.cards=cards
        self.total_bet_amount=total_bet_amount
        self.amount=amount
        
        