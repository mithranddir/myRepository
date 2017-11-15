spades = ('as', 'ks', 'qs', 'js', '10s', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s')
clubs = ('ac', 'kc', 'qc', 'jc', '10c', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c')
diamonds = ('ad', 'kd', 'qd', 'jd', '10d', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d')
hearts = ('ah', 'kh', 'qh', 'jh', '10h', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h')


royalFlushSpades = ['as', 'ks', 'qs', 'js', '10s']
royalFlushClubs = ['ac', 'kc', 'qc', 'jc', '10c']
royalFlushDiamonds = ['ad', 'kd', 'qd', 'jd', '10d']
royalFlushHearts = ['ah', 'kh', 'qh', 'jh', '10h']

royalFlush = [royalFlushSpades, royalFlushClubs, royalFlushDiamonds, royalFlushHearts]


straightFlushSpadesKing = ['ks', 'qs', 'js', '10s', '9s']
straightFlushSpadesQueen = ['qs', 'js', '10s', '9s', '8s']
straightFlushSpadesJack = ['js', '10s', '9s', '8s', '7s']
straightFlushSpadesTen = ['10s', '9s', '8s', '7s', '6s']
straightFlushSpadesNine = ['9s', '8s', '7s', '6s', '5s']
straightFlushSpadesEight = ['8s', '7s', '6s', '5s', '4s']
straightFlushSpadesSeven = ['7s', '6s', '5s', '4s', '3s']
straightFlushSpadesSix = ['6s', '5s', '4s', '3s', '2s']
straightFlushSpadesFive = ['5s', '4s', '3s', '2s', 'as']
straightFlushSpades = [straightFlushSpadesKing, straightFlushSpadesQueen, straightFlushSpadesJack, straightFlushSpadesTen, straightFlushSpadesNine, straightFlushSpadesEight, straightFlushSpadesSeven, straightFlushSpadesSix, straightFlushSpadesFive]
straightFlushClubsKing = ['kc', 'qc', 'jc', '10c', '9c']
straightFlushClubsQueen = ['qc', 'jc', '10c', '9c', '8c']
straightFlushClubsJack = ['jc', '10c', '9c', '8c', '7c']
straightFlushClubsTen = ['10c', '9c', '8c', '7c', '6c']
straightFlushClubsNine = ['9c', '8c', '7c', '6c', '5c']
straightFlushClubsEight = ['8c', '7c', '6c', '5c', '4c']
straightFlushClubsSeven = ['7c', '6c', '5c', '4c', '3c']
straightFlushClubsSix = ['6c', '5c', '4c', '3c', '2c']
straightFlushClubsFive = ['5c', '4c', '3c', '2c', 'ac']
straightFlushClubs = [straightFlushClubsKing, straightFlushClubsQueen, straightFlushClubsJack, straightFlushClubsTen, straightFlushClubsNine, straightFlushClubsEight, straightFlushClubsSeven, straightFlushClubsSix, straightFlushClubsFive]
straightFlushDiamondsKing = ['kd', 'qd', 'jd', '10d', '9d']
straightFlushDiamondsQueen = ['qd', 'jd', '10d', '9d', '8d']
straightFlushDiamondsJack = ['jd', '10d', '9d', '8d', '7d']
straightFlushDiamondsTen = ['10d', '9d', '8d', '7d', '6d']
straightFlushDiamondsNine = ['9d', '8d', '7d', '6d', '5d']
straightFlushDiamondsEight = ['8d', '7d', '6d', '5d', '4d']
straightFlushDiamondsSeven = ['7d', '6d', '5d', '4d', '3d']
straightFlushDiamondsSix = ['6d', '5d', '4d', '3d', '2d']
straightFlushDiamondsFive = ['5d', '4d', '3d', '2d', 'ad']
straightFlushDiamonds = [straightFlushDiamondsKing, straightFlushDiamondsQueen, straightFlushDiamondsJack, straightFlushDiamondsTen, straightFlushDiamondsNine, straightFlushDiamondsEight, straightFlushDiamondsSeven, straightFlushDiamondsSix, straightFlushDiamondsFive]
straightFlushHeartsKing = ['kh', 'qh', 'jh', '10h', '9h']
straightFlushHeartsQueen = ['qh', 'jh', '10h', '9h', '8h']
straightFlushHeartsJack = ['jh', '10h', '9h', '8h', '7h']
straightFlushHeartsTen = ['10h', '9h', '8h', '7h', '6h']
straightFlushHeartsNine = ['9h', '8h', '7h', '6h', '5h']
straightFlushHeartsEight = ['8h', '7h', '6h', '5h', '4h']
straightFlushHeartsSeven = ['7h', '6h', '5h', '4h', '3h']
straightFlushHeartsSix = ['6h', '5h', '4h', '3h', '2h']
straightFlushHeartsFive = ['5h', '4h', '3h', '2h', 'ah']
straightFlushHearts = [straightFlushHeartsKing, straightFlushHeartsQueen, straightFlushHeartsJack, straightFlushHeartsTen, straightFlushHeartsNine, straightFlushHeartsEight, straightFlushHeartsSeven, straightFlushHeartsSix, straightFlushHeartsFive]

straightFlush = [straightFlushSpades + straightFlushClubs + straightFlushDiamonds + straightFlushHearts]


fourAces = ['as', 'ac', 'ad', 'ah']
fourKings = ['ks', 'kc', 'kd', 'kh']
fourQueens = ['qs', 'qc', 'qd', 'qh']
fourJacks = ['js', 'jc', 'jd', 'jh']
fourTens = ['10s', '10c', '10d', '10h']
fourNines = ['9s', '9c', '9d', '9h']
fourEights = ['8s', '8c', '8d', '8h']
fourSevens = ['7s', '7c', '7d', '7h']
fourSixes = ['6s', '6c', '6d', '6h']
fourFives = ['5s', '5c', '5d', '5h']
fourFours = ['4s', '4c', '4d', '4h']
fourThrees = ['3s', '3c', '3d', '3h']
fourTwos = ['2s', '2c', '2d', '2h']

fourOfAKind = [fourAces, fourKings, fourQueens, fourJacks, fourTens, fourNines, fourEights, fourSevens, fourSixes, fourFives, fourFours, fourThrees, fourTwos]


fullHouse = []


flush = []


straightSpadesKing = []
straightSpadesQueen = []
straightSpadesJack = []
straightSpadesTen = []
straightSpadesNine = []
straightSpadesEight = []
straightSpadesSeven = []
straightSpadesSix = []
straightSpadesFive = []
straightSpades = [straightSpadesKing, straightSpadesQueen, straightSpadesJack, straightSpadesTen, straightSpadesNine, straightSpadesEight, straightSpadesSeven, straightSpadesSix, straightSpadesFive]
straightClubsKing = []
straightClubsQueen = []
straightClubsJack = []
straightClubsTen = []
straightClubsNine = []
straightClubsEight = []
straightClubsSeven = []
straightClubsSix = []
straightClubsFive = []
straightClubs = [straightClubsKing, straightClubsQueen, straightClubsJack, straightClubsTen, straightClubsNine, straightClubsEight, straightClubsSeven, straightClubsSix, straightClubsFive]
straightDiamondsKing = []
straightDiamondsQueen = []
straightDiamondsJack = []
straightDiamondsTen = []
straightDiamondsNine = []
straightDiamondsEight = []
straightDiamondsSeven = []
straightDiamondsSix = []
straightDiamondsFive = []
straightDiamonds = [straightDiamondsKing, straightDiamondsQueen, straightDiamondsJack, straightDiamondsTen, straightDiamondsNine, straightDiamondsEight, straightDiamondsSeven, straightDiamondsSix, straightDiamondsFive]
straightHeartsKing = []
straightHeartsQueen = []
straightHeartsJack = []
straightHeartsTen = []
straightHeartsNine = []
straightHeartsEight = []
straightHeartsSeven = []
straightHeartsSix = []
straightHeartsFive = []
straightHearts = [straightHeartsKing, straightHeartsQueen, straightHeartsJack, straightHeartsTen, straightHeartsNine, straightHeartsEight, straightHeartsSeven, straightHeartsSix, straightHeartsFive]

straight = [straightSpades + straightClubs + straightDiamonds + straightHearts]


threeAces = [['as', 'ac', 'ad'], ['as', 'ac', 'ah'], ['as', 'ad', 'ah'], ['ac', 'ad', 'ah']]
threeKings = [['ks', 'kc', 'kd'], ['ks', 'kc', 'kh'], ['ks', 'kd', 'kh'], ['kc', 'kd', 'kh']]
threeQueens = [['qs', 'qc', 'qd'], ['qs', 'qc', 'qh'], ['qs', 'qd', 'qh'], ['qc', 'qd', 'qh']]
threeJacks = [['js', 'jc', 'jd'], ['js', 'jc', 'jh'], ['js', 'jd', 'jh'], ['jc', 'jd', 'jh']]
threeTens = [['10s', '10c', '10d'], ['10s', '10c', '10h'], ['10s', '10d', '10h'], ['10c', '10d', '10h']]
threeNines = [['9s', '9c', '9d'], ['9s', '9c', '9h'], ['9s', '9d', '9h'], ['9c', '9d', '9h']]
threeEights = [['8s', '8c', '8d'], ['8s', '8c', '8h'], ['8s', '8d', '8h'], ['8c', '8d', '8h']]
threeSevens = [['7s', '7c', '7d'], ['7s', '7c', '7h'], ['7s', '7d', '7h'], ['7c', '7d', '7h']]
threeSixes = [['6s', '6c', '6d'], ['6s', '6c', '6h'], ['6s', '6d', '6h'], ['6c', '6d', '6h']]
threeFives = [['5s', '5c', '5d'], ['5s', '5c', '5h'], ['5s', '5d', '5h'], ['5c', '5d', '5h']]
threeFours = [['4s', '4c', '4d'], ['4s', '4c', '4h'], ['4s', '4d', '4h'], ['4c', '4d', '4h']]
threeThrees = [['3s', '3c', '3d'], ['3s', '3c', '3h'], ['3s', '3d', '3h'], ['3c', '3d', '3h']]
threeTwos = [['2s', '2c', '2d'], ['2s', '2c', '2h'], ['2s', '2d', '2h'], ['2c', '2d', '2h']]

threeOfAKind = [threeAces + threeKings + threeQueens + threeJacks + threeTens + threeNines + threeEights + threeSevens + threeSixes + threeFives + threeFours + threeThrees + threeTwos]


twoPairs = []


twoAces = [['as', 'ac'], ['ad', 'ah'], ['as', 'ah'], ['ac', 'ad'], ['as', 'ad'], ['ac' 'ah']]
twoKings = [['ks', 'kc'], ['kd', 'kh'], ['ks', 'kh'], ['kc', 'kd'], ['ks', 'kd'], ['kc' 'kh']]
twoQueens = [['qs', 'qc'], ['qd', 'qh'], ['qs', 'qh'], ['qc', 'qd'], ['qs', 'qd'], ['qc' 'qh']]
twoJacks = [['js', 'jc'], ['jd', 'jh'], ['js', 'jh'], ['jc', 'jd'], ['js', 'jd'], ['jc' 'jh']]
twoTens = [['10s', '10c'], ['10d', '10h'], ['10s', '10h'], ['10c', '10d'], ['10s', '10d'], ['10c' '10h']]
twoNines = [['9s', '9c'], ['9d', '9h'], ['9s', '9h'], ['9c', '9d'], ['9s', '9d'], ['9c' '9h']]
twoEights = [['8s', '8c'], ['8d', '8h'], ['8s', '8h'], ['8c', '8d'], ['8s', '8d'], ['8c' '8h']]
twoSevens = [['7s', '7c'], ['7d', '7h'], ['7s', '7h'], ['7c', '7d'], ['7s', '7d'], ['7c' '7h']]
twoSixes = [['6s', '6c'], ['6d', '6h'], ['6s', '6h'], ['6c', '6d'], ['6s', '6d'], ['6c' '6h']]
twoFives = [['5s', '5c'], ['5d', '5h'], ['5s', '5h'], ['5c', '5d'], ['5s', '5d'], ['5c' '5h']]
twoFours = [['4s', '4c'], ['4d', '4h'], ['4s', '4h'], ['4c', '4d'], ['4s', '4d'], ['4c' '4h']]
twoThrees = [['3s', '3c'], ['3d', '3h'], ['3s', '3h'], ['3c', '3d'], ['3s', '3d'], ['3c' '3h']]
twoTwos = [['2s', '2c'], ['2d', '2h'], ['2s', '2h'], ['2c', '2d'], ['2s', '2d'], ['2c' '2h']]

onePair = [twoAces + twoKings + twoQueens + twoJacks + twoTens + twoNines + twoEights + twoSevens + twoSixes + twoFives + twoFours + twoThrees + twoTwos]


allCards = (spades + clubs + diamonds + hearts)


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
        card = raw_input('Input card on the table #{}'.format(comparisonElement))
        cardsOnTheTable.append(card)
        comparisonElement += 1
    return cardsOnTheTable


cardsOnHand = cards_on_hand()
cardsOnTheTable = cards_on_the_table()
availableCards = cardsOnHand + cardsOnTheTable

#allCardsForOpponent = allCards - cardsOnHand


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
    Creates a matrix, where each list is the items that must be open in order for a combination to be selected.
    :param availableCards: items that are open to a user.
    :param aCombination: a list of items, that is a combination.
    :return: list of lists, for each item in 'aCombination' that is not in 'availableCards' is put in a list.
    """
    missingCardsList = []
    for combinationList in aCombination:
        missingCards = []
        for card in combinationList:
            if card not in availableCards:
                missingCards.append(card)
        missingCardsList.append(missingCards)
    return missingCardsList


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


def probability_of_missing_cards(missingCards, availableCards, allCards):
    """
    Calculates the probability of selecting a combination with existing items.
    :param missingCards:
    :param availableCards:
    :param allCards: 
    :return: probability of selecting 'missingCards' out of 'availableCards'.
    """
    theElement = 0
    for missingCardsList in missingCards:
        if (quantityOfCardsToBeAvailable - len(availableCards)) > missingCards:
            groundElement = probability_of_a_combination(len(missingCardsList), len(missingCardsList))
        else:
            groundElement = probability_of_a_combination(len(missingCardsList), (quantityOfCardsToBeAvailable - len(availableCards)))
        theElement = theElement + groundElement
    return theElement


favorableOutcomesInRoyalFlushForUser = probability_of_missing_cards(availableCards, missingCardsInRoyalFlushForUser)
favorableOutcomesInStraightFlushForUser = probability_of_missing_cards(availableCards, missingCardsInStraightFlushForUser)
favorableOutcomesInFourOfAKindForUser = probability_of_missing_cards(availableCards, missingCardsInFourOfAKindForUser)
favorableOutcomesInFullHouseForUser = probability_of_missing_cards(availableCards, missingCardsInFullHouseForUser)
favorableOutcomesInFlushForUser = probability_of_missing_cards(availableCards, missingCardsInFlushForUser)
favorableOutcomesInStraightForUser = probability_of_missing_cards(availableCards, missingCardsInStraightForUser)
favorableOutcomesInThreeOfAKindForUser = probability_of_missing_cards(availableCards, missingCardsInThreeOfAKindForUser)
favorableOutcomesInTwoPairsForUser = probability_of_missing_cards(availableCards, missingCardsInTwoPairsForUser)
favorableOutcomesInOnePairForUser = probability_of_missing_cards(availableCards, missingCardsInOnePairForUser)

favorableOutcomesInRoyalFlushForOpponent = probability_of_missing_cards(cardsOnTheTable, missingCardsInRoyalFlushForOpponent)
favorableOutcomesInStraightFlushForOpponent = probability_of_missing_cards(cardsOnTheTable, missingCardsInStraightFlushForOpponent)
favorableOutcomesInFourOfAKindForOpponent = probability_of_missing_cards(cardsOnTheTable, missingCardsInFourOfAKindForOpponent)
favorableOutcomesInFullHouseForOpponent = probability_of_missing_cards(cardsOnTheTable, missingCardsInFullHouseForOpponent)
favorableOutcomesInFlushForOpponent = probability_of_missing_cards(cardsOnTheTable, missingCardsInFlushForOpponent)
favorableOutcomesInStraightForOpponent = probability_of_missing_cards(cardsOnTheTable, missingCardsInStraightForOpponent)
favorableOutcomesInThreeOfAKindForOpponent = probability_of_missing_cards(cardsOnTheTable, missingCardsInThreeOfAKindForOpponent)
favorableOutcomesInTwoPairsForOpponent = probability_of_missing_cards(cardsOnTheTable, missingCardsInTwoPairsForOpponent)
favorableOutcomesInOnePairForOpponent = probability_of_missing_cards(cardsOnTheTable, missingCardsInOnePairForOpponent)


def total_number_of_outcomes(allCards, availableCards):
    return probability_of_a_combination(len(allCards) - len(availableCards), quantityOfCardsToBeAvailable - len(availableCards))


totalNumberOfOutcomesForUser = total_number_of_outcomes(allCards, availableCards)
#change this to (allCards - cardsOnHand)
totalNumberOfOutcomesForOpponent = total_number_of_outcomes(allCards, cardsOnTheTable)


def probability_of_the_combination(numberOfFavorableOutcomes, totalNumberOfOutcomes):
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


def formating(result, combinationString):
    return 'The Probability of {}:{}'.format(combinationString, result)