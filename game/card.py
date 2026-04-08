class Card():
    RANKS = ["A","J","K","Q","10","9","8","7","6","5","4","3","2"]
    SUITES = ["HEART", "DIAMOND", "CLUB", "SPADE"]
    def __init__(self, suite, rank):
        
        if not isinstance(suite, str):
            raise TypeError(f"Suite expected to be a strong got {type(suite).__name__}")
        if not isinstance(rank, str):
            raise TypeError(f"Rank expected to be a string got {type(rank).__name__}")
        suiteUpper=suite.upper()
        rankUpper=rank.upper()
        if rankUpper in Card.RANKS:
            pass
        else:
            raise TypeError(f"Added rank not in rank list{acceptedRanks}")
        if suiteUpper in Card.SUITES:
            pass
        else: 
            raise TypeError(f"Added suite not in suite list {acceptedSuites}")
        
        self.rank=rankUpper
        self.suite=suiteUpper
    
    def print_card(self):
        print("Rank", self.rank)
        print("Suite", self.suite)

if __name__ == "__main__":
    card1=Card(suite="heart", rank="A")
    card1.print_card()
    
    card2=Card(suite="Club", rank="3")
    card2.print_card()