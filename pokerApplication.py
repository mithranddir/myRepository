# deckOfCards = (spades, clubs, diamonds, hearts)
# spades = ('as', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks')
# clubs = ('ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc')
# diamonds = ('ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd')
# hearts = ('ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh')

# myFirstCard = (raw_input('Input the first card on hand.'))
# mySecondCard = (raw_input('Input the second card on hand.'))
# firstCardOnTheTable = (raw_input('Input the first card on hand.'))
# secondCardOnTheTable = (raw_input('Input the second card on hand.'))
# thirdCardOnTheTable = (raw_input('Input the third card on hand.'))
# fourthCardOnTheTable = (raw_input('Input the fourth card on hand.'))
# fifthCardOnTheTable = (raw_input('Input the fifth card on hand.'))

class Combination():

    def __init__(self):
        self.deckOfCards = (spades, clubs, diamonds, hearts)
        self.spades = ('as', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks')
        self.clubs = ('ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc')
        self.diamonds = ('ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd')
        self.hearts = ('ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh')

    # n!
    # finding factorinal of number n
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    # combination formula for selecting r items from n is
    # nCr= n!/r!(n-r)!
    # n = deckOfCards
    # r = selectedItems
    def probability_of_a_combination(self):
        return factorial(deckOfCards) / (factorial(selectedItems) * factorial(deckOfCards - selectedItems))

    def numberOfFavorableOutcomes(self):

    def totalNumberOfOutcomes(self):


    # P(A)
    # probability of event A
    def probability_of_one_event(self):
        return numberOfFavorableOutcomes / totalNumberOfOutcomes


class HighHand(Combination):
    def __init__(self):


class OnePair(Combination):
    def __init__(self):


class TwoPairs(Combination):
    def __init__(self):


class ThreeOfAKind(Combination):
    def __init__(self):


class Straight(Combination):
    def __init__(self):


class Flush(Combination):
    def __init__(self):


class FullHouse(Combination):
    def __init__(self):


class FourOfAKind(Combination):
    def __init__(self):


class StraightFlush(Combination):
    def __init__(self):


class RoyalFlush(Combination):
    def __init__(self):


