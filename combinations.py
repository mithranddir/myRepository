import itertools

spades = ['as', 'ks', 'qs', 'js', '10s', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s']
clubs = ['ac', 'kc', 'qc', 'jc', '10c', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c']
diamonds = ['ad', 'kd', 'qd', 'jd', '10d', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d']
hearts = ['ah', 'kh', 'qh', 'jh', '10h', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h']

allCards = [spades + clubs + diamonds + hearts]
suits = [spades, clubs, diamonds, hearts]


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


def pairs(combinationLength):
    suitsIndex = [0, 1, 2, 3]
    indexCombinations = [el for el in itertools.combinations(suitsIndex, combinationLength)]

    def result(indexes):
        zip_lists = [suits[index] for index in indexes]
        return zip(zip_lists)

    lists = [result(indexes) for indexes in indexCombinations]

    return lists


a = pairs(3)
print a