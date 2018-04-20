import itertools

spades = ['as', 'ks', 'qs', 'js', '10s', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s']
clubs = ['ac', 'kc', 'qc', 'jc', '10c', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c']
diamonds = ['ad', 'kd', 'qd', 'jd', '10d', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d']
hearts = ['ah', 'kh', 'qh', 'jh', '10h', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h']

allCards = [spades + clubs + diamonds + hearts]
suits = [spades, clubs, diamonds, hearts]
ranks = [suit for suit in zip(spades, clubs, diamonds, hearts)]


def straightFlush():
    result = []
    for suit in suits:
        for start in suit:
            ind1 = 0
            ind2 = 5
            result.append(suit[ind1:ind2])
            ind1 += 1
            ind2 += 1
            if ind2 == 14:
                ind2 = 0
    return result


def pairs(combinationLength):
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

# straight = [result for theList in ranks for result in itertools.combinations(theList, 5)]

fourOfAKind = ranks

threeOfAKind = pairs(3)

onePair = pairs(2)

fullHouse = [(aPair, aSet) for aPair in onePair for aSet in threeOfAKind]

twoPairs = [(thePair, aPair) for thePair in onePair for aPair in onePair]

# print([el for el in itertools.permutations([0, 1, 2, 3], 4)])
#print(len(twoPairs))
