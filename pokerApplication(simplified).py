spades = ('as', 'ks', 'qs', 'js', '10s', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s')
clubs = ('ac', 'kc', 'qc', 'jc', '10c', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c')
diamonds = ('ad', 'kd', 'qd', 'jd', '10d', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d')
hearts = ('ah', 'kh', 'qh', 'jh', '10h', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h')

suits = (spades, clubs, diamonds, hearts)
allCards = (spades + clubs + diamonds + hearts)

for suit in suits:
    suitLength = len(suit)
    highestSuitIndex = suitLength - 1


quantityOfPlayers = input('How many players are playing?')


quantityOfCardsToBeOnHand = input('How many cards MUST be on hand?')
quantityOfCardsToBeOnTheTable = input('How many cards MUST be on the table?')
quantityOfCardsToBeAvailable = quantityOfCardsToBeOnHand + quantityOfCardsToBeOnTheTable


def cards_on_hand():
    comparisonElement = 1
    cardsOnHand = []
    quantityOfCardsOnHand = input('How many cards ARE on hand?')
    while quantityOfCardsOnHand >= comparisonElement:
        card = raw_input('Input card on hand #{}'.format(comparisonElement))
        cardsOnHand.append(card)
        comparisonElement += 1
    return cardsOnHand


def cards_on_the_table():
    comparisonElement = 1
    cardsOnTheTable = []
    quantityOfCardsOnTheTable = input('How many cards ARE on the table?')
    while quantityOfCardsOnTheTable >= comparisonElement:
        card = raw_input('Input card the table #{}'.format(comparisonElement))
        cardsOnTheTable.append(card)
        comparisonElement += 1
    return cardsOnTheTable


availableCards = cards_on_hand() + cards_on_the_table()
quantityOfAvailableCards = len(availableCards)


#finding factorial of number n
#n! = 1*2*3*...*n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


#combination formula for selecting r items from n is
#nCr= n!/r!(n-r)!
#nCr= n!/r!(n-r)! = probability_of_a_combination
#n = allItems
#r = selectedItems
def probability_of_a_combination(allItems, selectedItems):
    return factorial(allItems) / (factorial(selectedItems) * factorial(allItems - selectedItems))


#(5C2 * 4C1)/9C3
#(5C2 * 4C1) = number_of_favorable_outcomes
def high_hand():
    pass


def one_pair():
    pass


def two_pairs():
    pass


def three_of_a_kind():
    combinationLength = 3
    a = probability_of_a_combination(len(suits[0]), 1)
    b = probability_of_a_combination(len(suits), combinationLength)
    c = probability_of_a_combination(12, 2)
    d = probability_of_a_combination(len(suits), 1)


def straight():
    combinationLength = 5
    a = probability_of_a_combination(len(suits), 1)
    return 10 * a * a * a * a * a


def flush():
    combinationLength = 5
    return probability_of_a_combination(len(suits), 1) * (probability_of_a_combination(len(suits[0]), combinationLength) - 10)


def full_house():
    pass


def four_of_a_kind():
    combinationLength = 4
    return probability_of_a_combination(len(suits[0]), 1) * probability_of_a_combination(len(suits), combinationLength) * probability_of_a_combination((len(allCards) - len(suits), 1))


def straight_flush():
    combinationLength = 5
    return probability_of_a_combination(len(suits), 1) * (len(suits[0]) - (combinationLength + 1))


def royal_flush():
#    combinationLength = 5
#    comparisonElement = 1
#    comparisonIndex = 0
#    royalFlush = []
#    for suit in suits:
#        suitLength = len(suit)
#    while combinationLength >= comparisonElement:
#        royalFlush[]
#    return probability_of_a_combination(len(suits), 1)
    pass


#(5C2 * 4C1)/9C3
#9C3 = total_number_of_outcomes
def total_number_of_outcomes():
    return probability_of_a_combination(len(allCards), quantityOfCardsToBeAvailable)


#P(A)
#(5C2 * 4C1)/9C3 = probability_of_combination
#(5C2 * 4C1) = number_of_favorable_outcomes
#9C3 = total_number_of_outcomes
def probability_of_the_combination(numberOfFavorableOutcomes):
    return numberOfFavorableOutcomes / total_number_of_outcomes()

