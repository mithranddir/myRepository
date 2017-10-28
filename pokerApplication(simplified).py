spades = ('as', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks')
clubs = ('ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc')
diamonds = ('ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd')
hearts = ('ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh')

suits = (spades, clubs, diamonds, hearts)
allCards = (spades + clubs + diamonds + hearts)


quantityOfCardsToBeOnHand = input('How many cards must be on hand?')
quantityOfCardsToBeOnTheTable = input('How many cards must be on the table?')
quantityOfCardsToBeAvailable = quantityOfCardsToBeOnHand + quantityOfCardsToBeOnTheTable

quantityOfCardsOnHand = input('How many cards are on hand?')
quantityOfCardsOnTheTable = input('How many cards are on the table?')
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


cardsOnHand = cards_on_hand()
cardsOnTheTable = cards_on_the_table()
availableCards = cardsOnHand + cardsOnTheTable


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
    return factorial(allItems) / (factorial(selectedItems) * factorial((allItems) - (selectedItems)))

#(5C2 * 4C1)/9C3
#9C3 = total_number_of_outcomes
def total_number_of_outcomes():
    return probability_of_a_combination(len(allCards), quantityOfCardsToBeAvailable)


#(5C2 * 4C1)/9C3
#(5C2 * 4C1) = number_of_favorable_outcomes
def high_hand():
    pass


def one_pair():
    return probability_of_a_combination() * 13


def two_pairs():
    return one_pair() * one_pair()


def three_of_a_kind():
    return probability_of_a_combination(4, 3) * 13


def straight():
    pass


def flush():
    pass


def full_house():
    return one_pair() * three_of_a_kind()


def four_of_a_kind():
    return probability_of_a_combination(4, 4) * 13


def straight_flush():
    pass


def royal_flush():
    pass


#P(A)
#(5C2 * 4C1)/9C3 = probability_of_combination
#(5C2 * 4C1) = number_of_favorable_outcomes
#9C3 = total_number_of_outcomes
def probability_of_combination(numberOfFavorableOutcomes):
    return numberOfFavorableOutcomes / total_number_of_outcomes()