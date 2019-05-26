import itertools
from math import factorial

# --------------------combinations--------------------
spades = ['as', 'ks', 'qs', 'js', '1s', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s']
clubs = ['ac', 'kc', 'qc', 'jc', '1c', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c']
diamonds = ['ad', 'kd', 'qd', 'jd', '1d', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d']
hearts = ['ah', 'kh', 'qh', 'jh', '1h', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h']

allCards = [spades + clubs + diamonds + hearts]
suits = [spades, clubs, diamonds, hearts]
ranks = [suit for suit in zip(spades, clubs, diamonds, hearts)]

def straightFlush():
    result = []
    for suit in suits:
        ind1 = 1
        ind2 = 6
        while ind2 < 14:
            result.append(suit[ind1:ind2])
            ind1 += 1
            ind2 += 1
    return result

def pairs(combinationLength):
    """
    Creates Pair and Three of a Kind combinations
    """
    suitsIndex = [0, 1, 2, 3]
    indexCombinations = [el for el in itertools.combinations(suitsIndex, combinationLength)]

    result = []
    for indexes in indexCombinations:
        listOne = suits[indexes[0]]
        listTwo = suits[indexes[1]]
        if combinationLength == 2:
            result = result + [(index1, index2) for index1, index2 in zip(listOne, listTwo)]
        elif combinationLength == 3:
            listThree = suits[indexes[2]]
            result = result + [(index1, index2, index3) for index1, index2, index3 in zip(listOne, listTwo, listThree)]
    return result

royalFlush = [theList[:5] for theList in suits]

straightFlush = straightFlush()

flush = [result for theList in suits for result in itertools.combinations(theList, 5)]

straight = []

fourOfAKind = ranks

threeOfAKind = pairs(3)

onePair = pairs(2)

fullHouse = [(aPair, aSet) for aPair in onePair for aSet in threeOfAKind]

twoPairs = [(thePair, aPair) for thePair in onePair for aPair in onePair]
# --------------------combinations--------------------

# --------------------input--------------------
quantityOfCardsToBeOnHand = int(input('How many cards MUST be on hand?'))
quantityOfCardsToBeOnTheTable = int(input('How many cards MUST be on the table?'))
quantityOfCardsToBeAvailable = quantityOfCardsToBeOnHand + quantityOfCardsToBeOnTheTable

quantityOfCardsOnHand = int(input('How many cards ARE on hand?'))
cardsOnHand = [input('Input card on hand #{}'.format(el)) for el in range(quantityOfCardsOnHand)]

quantityOfCardsOnTheTable = int(input('How many cards ARE on the table?'))
cardsOnTheTable = [input('Input card on the table #{}'.format(el)) for el in range(quantityOfCardsOnTheTable)]

availableCards = cardsOnHand + cardsOnTheTable
# --------------------input--------------------

# --------------------calculator-------------------
probability_of_a_combination = lambda allItems, selectedItems: factorial(allItems) / (factorial(selectedItems) * factorial(allItems - selectedItems))

sub_missing_cards = lambda availableCards, combinationList: [card for card in combinationList if card not in availableCards]
missing_cards = lambda availableCards, aCombination: [sub_missing_cards(availableCards, combinationList) for combinationList in aCombination]

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
favorableOutcomesInStraightFlushForUser = probability_of_missing_cards(missingCardsInStraightFlushForUser, availableCards)
favorableOutcomesInFourOfAKindForUser = probability_of_missing_cards(missingCardsInFourOfAKindForUser, availableCards)
favorableOutcomesInFullHouseForUser = probability_of_missing_cards(missingCardsInFullHouseForUser, availableCards)
favorableOutcomesInFlushForUser = probability_of_missing_cards(missingCardsInFlushForUser, availableCards)
favorableOutcomesInStraightForUser = probability_of_missing_cards(missingCardsInStraightForUser, availableCards)
favorableOutcomesInThreeOfAKindForUser = probability_of_missing_cards(missingCardsInThreeOfAKindForUser, availableCards)
favorableOutcomesInTwoPairsForUser = probability_of_missing_cards(missingCardsInTwoPairsForUser, availableCards)
favorableOutcomesInOnePairForUser = probability_of_missing_cards(missingCardsInOnePairForUser, availableCards)

favorableOutcomesInRoyalFlushForOpponent = probability_of_missing_cards(missingCardsInRoyalFlushForOpponent, cardsOnTheTable)
favorableOutcomesInStraightFlushForOpponent = probability_of_missing_cards(missingCardsInStraightFlushForOpponent, cardsOnTheTable)
favorableOutcomesInFourOfAKindForOpponent = probability_of_missing_cards(missingCardsInFourOfAKindForOpponent, cardsOnTheTable)
favorableOutcomesInFullHouseForOpponent = probability_of_missing_cards(missingCardsInFullHouseForOpponent, cardsOnTheTable)
favorableOutcomesInFlushForOpponent = probability_of_missing_cards(missingCardsInFlushForOpponent, cardsOnTheTable)
favorableOutcomesInStraightForOpponent = probability_of_missing_cards(missingCardsInStraightForOpponent, cardsOnTheTable)
favorableOutcomesInThreeOfAKindForOpponent = probability_of_missing_cards(missingCardsInThreeOfAKindForOpponent, cardsOnTheTable)
favorableOutcomesInTwoPairsForOpponent = probability_of_missing_cards(missingCardsInTwoPairsForOpponent, cardsOnTheTable)
favorableOutcomesInOnePairForOpponent = probability_of_missing_cards(missingCardsInOnePairForOpponent, cardsOnTheTable)

total_number_of_outcomes = lambda allCards, availableCards: probability_of_a_combination(len(allCards) - len(availableCards), quantityOfCardsToBeAvailable - len(availableCards))

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
# --------------------calculator--------------------
