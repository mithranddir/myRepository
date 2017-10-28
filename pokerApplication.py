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
    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * Combination.factorial(n - 1)

    #combination formula for selecting r items from n is
    #nCr= n!/r!(n-r)!
    #nCr= n!/r!(n-r)! = probability_of_a_combination
    #n = allItems
    #r = selectedItems
    @staticmethod
    def probability_of_a_combination(allItems, selectedItems):
        allItems = len(allItems)
        selectedItems = len(selectedItems)
        return Combination.factorial(allItems) / (Combination.factorial(selectedItems) * (Combination.factorial(allItems) - Combination.factorial(selectedItems)))


    #(5C2 * 4C1)/9C3
    #(5C2 * 4C1) = number_of_favorable_outcomes
    def number_of_favorable_outcomes(self):
        raise NotImplemented

    #(5C2 * 4C1)/9C3
    #9C3 = total_number_of_outcomes
    def total_number_of_outcomes(self):
        return Combination.probability_of_a_combination(self.deckOfCards, self.availableCards)

        #P(A)
        #(5C2 * 4C1)/9C3 = probability_of_combination
        #(5C2 * 4C1) = number_of_favorable_outcomes
        #9C3 = total_number_of_outcomes
    def probability_of_combination(self):
        return Combination.number_of_favorable_outcomes() / Combination.total_number_of_outcomes()


class HighHand(Combination):
    pass

class OnePair(Combination):
    def __init__(self):
        super(OnePair, self).__init__()

    def number_of_favorable_outcomes(self):
        return Combination.probability_of_a_combination()


class TwoPairs(Combination):
    pass


class ThreeOfAKind(Combination):
    pass


class Straight(Combination):
    pass


class Flush(Combination):
    pass


class FullHouse(Combination):
    pass


class FourOfAKind(Combination):
    pass


class StraightFlush(Combination):
    pass


class RoyalFlush(Combination):
    pass

