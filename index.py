from combinations import *

quantityOfCardsToBeOnHand = input('How many cards MUST be on hand?')
quantityOfCardsToBeOnTheTable = input('How many cards MUST be on the table?')
quantityOfCardsToBeAvailable = quantityOfCardsToBeOnHand + quantityOfCardsToBeOnTheTable


def cards_on_hand():
    """
    Creates a list of cards that are on hand.
    """
    cardsOnHand = []
    quantityOfCardsOnHand = input('How many cards ARE on hand?')
    for el in xrange(quantityOfCardsOnHand):
        card = raw_input('Input card on hand #{}'.format(el))
        cardsOnHand.append(card)
    return cardsOnHand


def cards_on_the_table():
    """
    Creates a list of cards that are on the table.
    """
    cardsOnTheTable = []
    quantityOfCardsOnTheTable = input('How many cards ARE on the table?')
    for el in xrange(quantityOfCardsOnTheTable):
        card = raw_input('Input card on the table #{}'.format(el))
        cardsOnTheTable.append(card)
    return cardsOnTheTable


cardsOnHand = cards_on_hand()
cardsOnTheTable = cards_on_the_table()
availableCards = cardsOnHand + cardsOnTheTable


def factorial(n):
    """
    Calculates the factorial of a number.
    """

    for el in xrange(n):
        f = n * (n - 1)
        n = n - 1
    return f


def probability_of_a_combination(allItems, selectedItems):
    """
    Calculates the probability of a combination.
    """
    return factorial(allItems) / (factorial(selectedItems) * factorial(allItems - selectedItems))


def missing_cards(availableCards, aCombination):
    """
    Creates a matrix where each list is a list of items that are missing for the particular combination.
    """
    missingCardsMatrix = []
    for combinationList in aCombination:
        missingCardsList = []
        for card in combinationList:
            if card not in availableCards:
                missingCardsList.append(card)
        missingCardsMatrix.append(missingCardsList)
    return missingCardsMatrix


missingCardsInRoyalFlushForUser = missing_cards(availableCards, royalFlush)
missingCardsInStraightFlushForUser = missing_cards(availableCards, straightFlush)
missingCardsInFourOfAKindForUser = missing_cards(availableCards, fourOfAKind)
missingCardsInFullHouseForUser = missing_cards(availableCards, fullHouse)
missingCardsInFlushForUser = missing_cards(availableCards, flush)
#missingCardsInStraightForUser = missing_cards(availableCards, straight)
missingCardsInThreeOfAKindForUser = missing_cards(availableCards, threeOfAKind)
missingCardsInTwoPairsForUser = missing_cards(availableCards, twoPairs)
missingCardsInOnePairForUser = missing_cards(availableCards, onePair)

missingCardsInRoyalFlushForOpponent = missing_cards(cardsOnTheTable, royalFlush)
missingCardsInStraightFlushForOpponent = missing_cards(cardsOnTheTable, straightFlush)
missingCardsInFourOfAKindForOpponent = missing_cards(cardsOnTheTable, fourOfAKind)
missingCardsInFullHouseForOpponent = missing_cards(cardsOnTheTable, fullHouse)
missingCardsInFlushForOpponent = missing_cards(cardsOnTheTable, flush)
#missingCardsInStraightForOpponent = missing_cards(cardsOnTheTable, straight)
missingCardsInThreeOfAKindForOpponent = missing_cards(cardsOnTheTable, threeOfAKind)
missingCardsInTwoPairsForOpponent = missing_cards(cardsOnTheTable, twoPairs)
missingCardsInOnePairForOpponent = missing_cards(cardsOnTheTable, onePair)


def probability_of_missing_cards(missingCards, availableCards):
    """
    Calculates the probability of selecting missing cards out of all cards.
    """
    theCardProbability = probability_of_a_combination(1, 1)#probability of selecting a unique card
    quantityOfCardsThatWillBeAvailable = quantityOfCardsToBeAvailable - len(availableCards)#quantity of cards that will be available, but not yet available
    missingCardsLength = []
    for missingCardsList in missingCards:#converts missingCards into list with its lists lengths
        listLength = len(missingCardsList)
        missingCardsLength.append(listLength)
    missingCardsLength.sort()
    allMissingCardsProbability = 0
    if missingCardsLength[0] == 0:#combination is selected
        allMissingCardsProbability = True
    elif missingCardsLength[0] > (quantityOfCardsToBeAvailable - len(availableCards)):#combination cannot be selected
        allMissingCardsProbability = False
    else:#combinatio can be selected, but not yet selected
        theMissingCardsProbability = 0
        for card in missingCardsLength:
            probabilityOfUnrelatedCards = probability_of_a_combination(len(allCards) - len(availableCards), quantityOfCardsThatWillBeAvailable - card)#probability of selecting cards that are irralavant to the combination
            probabilityOfTheCards = 1
            comparisonElement = 0
            while (quantityOfCardsThatWillBeAvailable - card) >= comparisonElement:
                probabilityOfTheCards = probabilityOfTheCards * theCardProbability
                comparisonElement += 1
            theMissingCardsProbability = probabilityOfUnrelatedCards * probabilityOfTheCards
            allMissingCardsProbability = allMissingCardsProbability + theMissingCardsProbability
    return allMissingCardsProbability


favorableOutcomesInRoyalFlushForUser = probability_of_missing_cards(missingCardsInRoyalFlushForUser, availableCards)
# favorableOutcomesInStraightFlushForUser = probability_of_missing_cards(missingCardsInStraightFlushForUser, availableCards)
# favorableOutcomesInFourOfAKindForUser = probability_of_missing_cards(missingCardsInFourOfAKindForUser, availableCards)
# favorableOutcomesInFullHouseForUser = probability_of_missing_cards(missingCardsInFullHouseForUser, availableCards)
# favorableOutcomesInFlushForUser = probability_of_missing_cards(missingCardsInFlushForUser, availableCards)
# favorableOutcomesInStraightForUser = probability_of_missing_cards(missingCardsInStraightForUser, availableCards)
# favorableOutcomesInThreeOfAKindForUser = probability_of_missing_cards(missingCardsInThreeOfAKindForUser, availableCards)
# favorableOutcomesInTwoPairsForUser = probability_of_missing_cards(missingCardsInTwoPairsForUser, availableCards)
# favorableOutcomesInOnePairForUser = probability_of_missing_cards(missingCardsInOnePairForUser, availableCards)
#
# favorableOutcomesInRoyalFlushForOpponent = probability_of_missing_cards(missingCardsInRoyalFlushForOpponent, cardsOnTheTable)
# favorableOutcomesInStraightFlushForOpponent = probability_of_missing_cards(missingCardsInStraightFlushForOpponent, cardsOnTheTable)
# favorableOutcomesInFourOfAKindForOpponent = probability_of_missing_cards(missingCardsInFourOfAKindForOpponent, cardsOnTheTable)
# favorableOutcomesInFullHouseForOpponent = probability_of_missing_cards(missingCardsInFullHouseForOpponent, cardsOnTheTable)
# favorableOutcomesInFlushForOpponent = probability_of_missing_cards(missingCardsInFlushForOpponent, cardsOnTheTable)
# favorableOutcomesInStraightForOpponent = probability_of_missing_cards(missingCardsInStraightForOpponent, cardsOnTheTable)
# favorableOutcomesInThreeOfAKindForOpponent = probability_of_missing_cards(missingCardsInThreeOfAKindForOpponent, cardsOnTheTable)
# favorableOutcomesInTwoPairsForOpponent = probability_of_missing_cards(missingCardsInTwoPairsForOpponent, cardsOnTheTable)
# favorableOutcomesInOnePairForOpponent = probability_of_missing_cards(missingCardsInOnePairForOpponent, cardsOnTheTable)


def total_number_of_outcomes(allCards, availableCards):
    """
    Calculates probability of selecting missing cards out of all cards.
    """
    return probability_of_a_combination(len(allCards) - len(availableCards), quantityOfCardsToBeAvailable - len(availableCards))


totalNumberOfOutcomesForUser = total_number_of_outcomes(allCards, availableCards)
totalNumberOfOutcomesForOpponent = total_number_of_outcomes(allCards, cardsOnTheTable)


def probability_of_the_combination(numberOfFavorableOutcomes, totalNumberOfOutcomes):
    """
    Calculates probability of a particular combination.
    """
    if numberOfFavorableOutcomes == True:
        probabilityOfTheCombination = 1
    elif numberOfFavorableOutcomes == False:
        probabilityOfTheCombination = 0
    else:
        probabilityOfTheCombination = numberOfFavorableOutcomes / totalNumberOfOutcomes
    return probabilityOfTheCombination


probabilityOfRoyalFlushForUser = probability_of_the_combination(favorableOutcomesInRoyalFlushForUser, totalNumberOfOutcomesForUser)
# probabilityOfStraightFlushForUser = probability_of_the_combination(favorableOutcomesInStraightFlushForUser, totalNumberOfOutcomesForUser)
# probabilityOfFourOfAKindForUser = probability_of_the_combination(favorableOutcomesInFourOfAKindForUser, totalNumberOfOutcomesForUser)
# probabilityOfFullHouseForUser = probability_of_the_combination(favorableOutcomesInFullHouseForUser, totalNumberOfOutcomesForUser)
# probabilityOfFlushForUser = probability_of_the_combination(favorableOutcomesInFlushForUser, totalNumberOfOutcomesForUser)
# probabilityOfStraightForUser = probability_of_the_combination(favorableOutcomesInStraightForUser, totalNumberOfOutcomesForUser)
# probabilityOfThreeOfAKindForUser = probability_of_the_combination(favorableOutcomesInThreeOfAKindForUser, totalNumberOfOutcomesForUser)
# probabilityOfTwoPairsForUser = probability_of_the_combination(favorableOutcomesInTwoPairsForUser, totalNumberOfOutcomesForUser)
# probabilityOfOnePairForUser = probability_of_the_combination(favorableOutcomesInOnePairForUser, totalNumberOfOutcomesForUser)
#
# probabilityOfRoyalFlushForOpponent = probability_of_the_combination(favorableOutcomesInRoyalFlushForOpponent, totalNumberOfOutcomesForOpponent)
# probabilityOfStraightFlushForOpponent = probability_of_the_combination(favorableOutcomesInStraightFlushForOpponent, totalNumberOfOutcomesForOpponent)
# probabilityOfFourOfAKindForOpponent = probability_of_the_combination(favorableOutcomesInFourOfAKindForOpponent, totalNumberOfOutcomesForOpponent)
# probabilityOfFullHouseForOpponent = probability_of_the_combination(favorableOutcomesInFullHouseForOpponent, totalNumberOfOutcomesForOpponent)
# probabilityOfFlushForOpponent = probability_of_the_combination(favorableOutcomesInFlushForOpponent, totalNumberOfOutcomesForOpponent)
# probabilityOfStraightForOpponent = probability_of_the_combination(favorableOutcomesInStraightForOpponent, totalNumberOfOutcomesForOpponent)
# probabilityOfThreeOfAKindForOpponent = probability_of_the_combination(favorableOutcomesInThreeOfAKindForOpponent, totalNumberOfOutcomesForOpponent)
# probabilityOfTwoPairsForOpponent = probability_of_the_combination(favorableOutcomesInTwoPairsForOpponent, totalNumberOfOutcomesForOpponent)
# probabilityOfOnePairForOpponent = probability_of_the_combination(favorableOutcomesInOnePairForOpponent, totalNumberOfOutcomesForOpponent)

print(missingCardsInRoyalFlushForUser)