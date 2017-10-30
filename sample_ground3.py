spades = ('as', 'ks', 'qs', 'js', '10s', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s')
clubs = ('ac', 'kc', 'qc', 'jc', '10c', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c')
diamonds = ('ad', 'kd', 'qd', 'jd', '10d', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d')
hearts = ('ah', 'kh', 'qh', 'jh', '10h', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h')

suits = (spades, clubs, diamonds, hearts)
allCards = (spades + clubs + diamonds + hearts)



def royal_flush_constructor():
    combinationLength = 5
    comparisonIndex = 0
    comparisonElement= 1
    royalFlush = []
    royalFlushSuit = []
    while len(suits) >= comparisonElement:
        comparisonIndexSuit = 0
        comparisonElementSuit = 1
        while combinationLength >= comparisonElementSuit:
            royalFlushSuit.append(suits[comparisonIndexSuit])
            comparisonElementSuit += 1
            comparisonIndexSuit += 1
            royalFlush.append(royalFlushSuit)
        comparisonElement += 1
        comparisonIndex += 1
    return royalFlush
print royal_flush_constructor()


#    royalFlushQuantity = 'how many royal flushes can fit in cardsToBeAvailable'
#    royalFlushInAll = 'how many royal flushes can fit in allCards'
#    return probability_of_a_combination(royalFlushInAll, royalFlushInOutcome)
