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
