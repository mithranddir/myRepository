from combinations import *

quantityOfCardsToBeOnHand = input('How many cards MUST be on hand?')
quantityOfCardsToBeOnTheTable = input('How many cards MUST be on the table?')
quantityOfCardsToBeAvailable = quantityOfCardsToBeOnHand + quantityOfCardsToBeOnTheTable


def cards_on_hand():
    """
    Creates a list of cards that are on hand.

    :return: list of cards that are on hand.
    """
    comparisonElement = 1
    cardsOnHand = []
    quantityOfCardsOnHand = input('How many cards ARE on hand?')
    while quantityOfCardsOnHand >= comparisonElement:
        card = raw_input('Input card on hand #{}'.format(comparisonElement))
        cardsOnHand.append(card)
        comparisonElement += 1
    return cardsOnHand


def cards_on_the_table():
    """
    Creates a list of cards that are on the table.

    :return: list of cards that are on the table.
    """
    comparisonElement = 1
    cardsOnTheTable = []
    quantityOfCardsOnTheTable = input('How many cards ARE on the table?')
    while quantityOfCardsOnTheTable >= comparisonElement:
        card = raw_input('Input card on the table #{}'.format(comparisonElement))
        cardsOnTheTable.append(card)
        comparisonElement += 1
    return cardsOnTheTable

cardsOnHand = cards_on_hand()
cardsOnTheTable = cards_on_the_table()
availableCards = cardsOnHand + cardsOnTheTable


def factorial(n):
    """
    Calculates the factorial of a number.

    :param n: the number to get the factorial of.
    :return: the factorial of n.
    """
    comparisonElement = 1.0
    while n >= 1:
        comparisonElement = comparisonElement * n
        n = n - 1
    return comparisonElement


def probability_of_a_combination(allItems, selectedItems):
    """
    Calculates the probability of a combination.

    :param allItems: the items from which items will be selected.
    :param selectedItems: the items that will be selected.
    :return: the probability of selecting 'selectedItems' from "allItems".
    """
    return factorial(allItems) / (factorial(selectedItems) * factorial(allItems - selectedItems))


def missing_cards(availableCards, aCombination):
    """
    Creates a matrix where each list is a list of items that are missing for the particular combination.

    :param availableCards: items that are open to a user.
    :param aCombination: a list of items, that is a combination.
    :return: list of lists, for each item in 'aCombination' that is not in 'availableCards' is put in a list.
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
missingCardsInStraightForUser = missing_cards(availableCards, straight)
missingCardsInThreeOfAKindForUser = missing_cards(availableCards, threeOfAKind)
missingCardsInTwoPairsForUser = missing_cards(availableCards, twoPairs)
missingCardsInOnePairForUser = missing_cards(availableCards, onePair)

missingCardsInRoyalFlushForOpponent = missing_cards(cardsOnTheTable, royalFlush)
missingCardsInStraightFlushForOpponent = missing_cards(cardsOnTheTable, straightFlush)
missingCardsInFourOfAKindForOpponent = missing_cards(cardsOnTheTable, fourOfAKind)
missingCardsInFullHouseForOpponent = missing_cards(cardsOnTheTable, fullHouse)
missingCardsInFlushForOpponent = missing_cards(cardsOnTheTable, flush)
missingCardsInStraightForOpponent = missing_cards(cardsOnTheTable, straight)
missingCardsInThreeOfAKindForOpponent = missing_cards(cardsOnTheTable, threeOfAKind)
missingCardsInTwoPairsForOpponent = missing_cards(cardsOnTheTable, twoPairs)
missingCardsInOnePairForOpponent = missing_cards(cardsOnTheTable, onePair)


def probability_of_missing_cards(missingCards, allCards):
    """
    Calculates the probability of selecting missing cards out of all cards.

    :param missingCards: list of cards, where each card needs to be selected in order for combination to be open.
    :param allCards: list of cards, from which the "missingCards' will be selected.
    :return: probability of selecting 'missingCards' out of 'allCards'.
    """
    theElement = 0
    for missingCardsList in missingCards:
        if (quantityOfCardsToBeAvailable - len(availableCards)) < missingCards:
            theElement = 0
        elif len(missingCardsList) == 0:
            theElement = 1
        else:
            theElement = probability_of_a_combination(len(missingCardsList), (quantityOfCardsToBeAvailable - len(availableCards)))

        return theElement
    return theElement


favorableOutcomesInRoyalFlushForUser = probability_of_missing_cards(missingCardsInRoyalFlushForUser, allCards)
favorableOutcomesInStraightFlushForUser = probability_of_missing_cards(missingCardsInStraightFlushForUser, allCards)
favorableOutcomesInFourOfAKindForUser = probability_of_missing_cards(missingCardsInFourOfAKindForUser, allCards)
favorableOutcomesInFullHouseForUser = probability_of_missing_cards(missingCardsInFullHouseForUser, allCards)
favorableOutcomesInFlushForUser = probability_of_missing_cards(missingCardsInFlushForUser, allCards)
favorableOutcomesInStraightForUser = probability_of_missing_cards(missingCardsInStraightForUser, allCards)
favorableOutcomesInThreeOfAKindForUser = probability_of_missing_cards(missingCardsInThreeOfAKindForUser, allCards)
favorableOutcomesInTwoPairsForUser = probability_of_missing_cards(missingCardsInTwoPairsForUser, allCards)
favorableOutcomesInOnePairForUser = probability_of_missing_cards(missingCardsInOnePairForUser, allCards)

favorableOutcomesInRoyalFlushForOpponent = probability_of_missing_cards(missingCardsInRoyalFlushForOpponent, allCards)
favorableOutcomesInStraightFlushForOpponent = probability_of_missing_cards(missingCardsInStraightFlushForOpponent, allCards)
favorableOutcomesInFourOfAKindForOpponent = probability_of_missing_cards(missingCardsInFourOfAKindForOpponent, allCards)
favorableOutcomesInFullHouseForOpponent = probability_of_missing_cards(missingCardsInFullHouseForOpponent, allCards)
favorableOutcomesInFlushForOpponent = probability_of_missing_cards(missingCardsInFlushForOpponent, allCards)
favorableOutcomesInStraightForOpponent = probability_of_missing_cards(missingCardsInStraightForOpponent, allCards)
favorableOutcomesInThreeOfAKindForOpponent = probability_of_missing_cards(missingCardsInThreeOfAKindForOpponent, allCards)
favorableOutcomesInTwoPairsForOpponent = probability_of_missing_cards(missingCardsInTwoPairsForOpponent, allCards)
favorableOutcomesInOnePairForOpponent = probability_of_missing_cards(missingCardsInOnePairForOpponent, allCards)


def total_number_of_outcomes(allCards, availableCards):
    """
    Calculates probability of selecting missing cards out of all cards.

    :param allCards: list of cards, from which the cards will be selected.
    :param availableCards: list of cards, that are available for the user.
    :return: probability of selecting 'missing cards' out of 'all cards'.
    """
    return probability_of_a_combination(len(allCards) - len(availableCards), quantityOfCardsToBeAvailable - len(availableCards))


totalNumberOfOutcomesForUser = total_number_of_outcomes(allCards, availableCards)
totalNumberOfOutcomesForOpponent = total_number_of_outcomes(allCards, cardsOnTheTable)


def probability_of_the_combination(numberOfFavorableOutcomes, totalNumberOfOutcomes):
    """
    Calculates probability of a particular combination.

    :param numberOfFavorableOutcomes: probability of selecting missing cards out of all cards.
    :param totalNumberOfOutcomes: sum of probabilities of selecting each missing card.
    :return: probability of selecting a particular combination.
    """
    return numberOfFavorableOutcomes / totalNumberOfOutcomes


probabilityOfRoyalFlushForUser = probability_of_the_combination(favorableOutcomesInRoyalFlushForUser, totalNumberOfOutcomesForUser)
probabilityOfStraightFlushForUser = probability_of_the_combination(favorableOutcomesInStraightFlushForUser, totalNumberOfOutcomesForUser)
probabilityOfFourOfAKindForUser = probability_of_the_combination(favorableOutcomesInFourOfAKindForUser, totalNumberOfOutcomesForUser)
probabilityOfFullHouseForUser = probability_of_the_combination(favorableOutcomesInFullHouseForUser, totalNumberOfOutcomesForUser)
probabilityOfFlushForUser = probability_of_the_combination(favorableOutcomesInFlushForUser, totalNumberOfOutcomesForUser)
probabilityOfStraightForUser = probability_of_the_combination(favorableOutcomesInStraightForUser, totalNumberOfOutcomesForUser)
probabilityOfThreeOfAKindForUser = probability_of_the_combination(favorableOutcomesInThreeOfAKindForUser, totalNumberOfOutcomesForUser)
probabilityOfTwoPairsForUser = probability_of_the_combination(favorableOutcomesInTwoPairsForUser, totalNumberOfOutcomesForUser)
probabilityOfOnePairForUser = probability_of_the_combination(favorableOutcomesInOnePairForUser, totalNumberOfOutcomesForUser)

probabilityOfRoyalFlushForOpponent = probability_of_the_combination(favorableOutcomesInRoyalFlushForOpponent, totalNumberOfOutcomesForOpponent)
probabilityOfStraightFlushForOpponent = probability_of_the_combination(favorableOutcomesInStraightFlushForOpponent, totalNumberOfOutcomesForOpponent)
probabilityOfFourOfAKindForOpponent = probability_of_the_combination(favorableOutcomesInFourOfAKindForOpponent, totalNumberOfOutcomesForOpponent)
probabilityOfFullHouseForOpponent = probability_of_the_combination(favorableOutcomesInFullHouseForOpponent, totalNumberOfOutcomesForOpponent)
probabilityOfFlushForOpponent = probability_of_the_combination(favorableOutcomesInFlushForOpponent, totalNumberOfOutcomesForOpponent)
probabilityOfStraightForOpponent = probability_of_the_combination(favorableOutcomesInStraightForOpponent, totalNumberOfOutcomesForOpponent)
probabilityOfThreeOfAKindForOpponent = probability_of_the_combination(favorableOutcomesInThreeOfAKindForOpponent, totalNumberOfOutcomesForOpponent)
probabilityOfTwoPairsForOpponent = probability_of_the_combination(favorableOutcomesInTwoPairsForOpponent, totalNumberOfOutcomesForOpponent)
probabilityOfOnePairForOpponent = probability_of_the_combination(favorableOutcomesInOnePairForOpponent, totalNumberOfOutcomesForOpponent)

