spades = ('2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks', 'as')
clubs = ('2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc', 'ac')
diamonds = ('2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd', 'ad')
hearts = ('2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh', 'ah')

suits = (spades, clubs, diamonds, hearts)
allCards = (spades + clubs + diamonds + hearts)


quantityOfPlayers = input('How many players are playing?')


quantityOfCardsToBeOnHand = input('How many cards MUST be on hand?')
quantityOfCardsToBeOnTheTable = input('How many cards MUST be on the table?')
quantityOfCardsToBeAvailable = quantityOfCardsToBeOnHand + quantityOfCardsToBeOnTheTable

quantityOfCardsOnHand = input('How many cards ARE on hand?')
quantityOfCardsOnTheTable = input('How many cards ARE on the table?')
quantityOfAvailableCards = quantityOfCardsOnHand + quantityOfCardsOnTheTable


def cards_on_hand():
    comparisonElement = 1
    cardsOnHand = []
    while quantityOfCardsOnHand >= comparisonElement:
        card = raw_input('Input card on hand #{}'.format(comparisonElement))
        cardsOnHand.append(card)
        comparisonElement += 1
    return cardsOnHand


def cards_on_the_table():
    comparisonElement = 1
    cardsOnTheTable = []
    while quantityOfCardsOnHand >= comparisonElement:
        card = raw_input('Input card the table #{}'.format(comparisonElement))
        cardsOnTheTable.append(card)
        comparisonElement += 1
    return cardsOnTheTable


availableCards = cards_on_hand() + cards_on_the_table()


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
#9C3 = total_number_of_outcomes
def total_number_of_outcomes():
    return probability_of_a_combination(len(allCards), quantityOfCardsToBeAvailable)


def high_hand():
    pass


#(5C2 * 4C1)/9C3
#(5C2 * 4C1) = number_of_favorable_outcomes
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
    combinationLength = 5
    return probability_of_a_combination(len(suits), 1)


#P(A)
#(5C2 * 4C1)/9C3 = probability_of_combination
#(5C2 * 4C1) = number_of_favorable_outcomes
#9C3 = total_number_of_outcomes
def probability_of_the_combination(numberOfFavorableOutcomes):
    return numberOfFavorableOutcomes / total_number_of_outcomes()

