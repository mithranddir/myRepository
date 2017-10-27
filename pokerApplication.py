class Combination():

    def __init__(self):
        self.spades = ('as', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks')
        self.clubs = ('ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc')
        self.diamonds = ('ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd')
        self.hearts = ('ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh')
        self.deckOfCards = (self.spades, self.clubs, self.diamonds, self.hearts)
        self.cardsOnHand = []
        self.cardsOnTheTable = []
        self.availableCards = [self.cardsOnHand, self.cardsOnTheTable]

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

    def number_of_favorable_outcomes(self):

    def total_number_of_outcomes(self):
        return factorial(self.deckOfCards) / (factorial(self.cardsInTheCombination) * factorial(self.deckOfCards - self.cardsInTheCombination))


    # P(A)
    # probability of event A
    def probability_of_one_event(self):
        return number_of_favorable_outcomes() / total_number_of_outcomes()


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


