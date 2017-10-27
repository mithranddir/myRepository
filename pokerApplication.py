class Combination():

    def __init__(self):
        self.spades = ('as', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks')
        self.clubs = ('ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc')
        self.diamonds = ('ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd')
        self.hearts = ('ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh')

        self.deckOfCards = (Combination.spades, Combination.clubs, Combination.diamonds, Combination.hearts)
        self.cardsOnHand = []
        self.cardsOnTheTable = []
        self.availableCards = [Combination.cardsOnHand, Combination.cardsOnTheTable]

    #finding factorial of number n
    #n! = 1*2*3*...*n
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * Combination.factorial(n - 1)

    #combination formula for selecting r items from n is
    #nCr= n!/r!(n-r)!
    #nCr= n!/r!(n-r)! = probability_of_a_combination
    #n = allItems
    #r = selectedItems
    def probability_of_a_combination(self, allItems, selectedItems):
        allItems = len(allItems)
        selectedItems = len(selectedItems)
        return Combination.factorial(allItems) / (Combination.factorial(selectedItems) * (Combination.factorial(allItems) - Combination.factorial(selectedItems)))


    #(5C2 * 4C1)/9C3
    #(5C2 * 4C1) = number_of_favorable_outcomes
    def number_of_favorable_outcomes(self):
        pass

    #(5C2 * 4C1)/9C3
    #9C3 = total_number_of_outcomes
    def total_number_of_outcomes(self):
        retutn Combination.probability_of_a_combination(Combination.deckOfCards, Combination.availableCards)


    #P(A)
    #(5C2 * 4C1)/9C3 = probability_of_combination
    #(5C2 * 4C1) = number_of_favorable_outcomes
    #9C3 = total_number_of_outcomes
    def probability_of_combination(self):
        return Combination.number_of_favorable_outcomes() / Combination.total_number_of_outcomes()


class HighHand(Combination):
    def __init__(self):


class OnePair(Combination):
    def number_of_favorable_outcomes(self):
        for comparisonElement in range(0, 13):
            pass
        for elementInSpades in self.spades:
            pass
        for elementInClubs in self.clubs:
            pass
        for elementInDiamonds in self.diamonds:
            pass
        for elementInDiamonds in self.diamonds:
            pass
        return Combination.probability_of_a_combination()


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


