# deck unlimited in size
# no jokers
# jack/queen/king = 10
# ace = 11 or 1
# cards have equal probability of being drawn
# cards are not removed from deck when drawn

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def randNum():
    return random.randint(0, 12)

def currScore(list):
    sum = 0
    for i in list:
        sum += i
    return sum

def secondScore(list):
    sum = 0
    for i in list:
        sum += i
        if (i == 11):
            sum -= 10
    return sum

playGame = 'y'

while(playGame == 'y'):
    myCards = []
    compCards = []
    myCards.append(cards[randNum()])
    myCards.append(cards[randNum()])
    compCards.append(cards[randNum()])

    myScore1 = currScore(myCards)
    myScore2 = secondScore(myCards)
    compScore1 = currScore(compCards)

    if(myScore1 == myScore2):
        print(f"Your cards: {myCards}, current score: {myScore1}")
    else:
        print(f"Your cards: {myCards}, current score: {myScore1} or {myScore2}")
    print(f"Dealer's cards: {compCards}, current score: {compScore1}")
    
    drawCard = input('Do you wish to draw again? Type \'y\' or \'n\': ')
    while(drawCard != 'y' and drawCard != 'n'):
        drawCard = input('Invalid input. Do you wish to draw again? Type \'y\' or \'n\': ')
    while(drawCard == 'y'):
        myCards.append(cards[randNum()])
        myScore1 = currScore(myCards)
        myScore2 = secondScore(myCards)
        if(myScore1 == myScore2):
            print(f"Your cards: {myCards}, current score: {myScore1}")
        else:
            print(f"Your cards: {myCards}, current score: {myScore1} or {myScore2}")
        if(currScore(compCards) <= 16):
            compCards.append(cards[randNum()])
            compScore1 = currScore(compCards)
            print(f"Dealer's cards: {compCards}, current score: {compScore1}")
        else:
            print(f"Dealer's final hand: {compCards}, final score: {compScore1}")
        
        drawCard = input('Do you wish to draw again? Type \'y\' or \'n\': ')
        while(drawCard != 'y' and drawCard != 'n'):
            drawCard = input('Invalid input. Do you wish to draw again? Type \'y\' or \'n\': ')

    while (currScore(compCards) <= 16):
            compCards.append(cards[randNum()])
            compScore1 = currScore(compCards)
            print(f"Dealer's cards: {compCards}, current score: {compScore1}")
    
    finalScore = myScore2
    if(myScore1 == 21):
        print(f"Your final hand: {myCards}, current score: {myScore1}")
        finalScore = myScore1
    elif (myScore2 == 21):
        print(f"Your cards: {myCards}, current score: {myScore2}")
    elif (myScore2 < 21 and myScore1 > 21):
        print(f"Your cards: {myCards}, current score: {myScore2}")
    else:
        print(f"Your cards: {myCards}, current score: {myScore2}")

    print(f"Dealer's final hand: {compCards}, final score: {compScore1}")

    if(finalScore > 21):
        print("You bust! You lose.")
    elif(finalScore == compScore1):
        print("Draw!")
    elif (finalScore > compScore1 or compScore1 > 21):
        print("You have won!")
    else:
        print("You have lost!")


    playGame = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')
    while(playGame != 'y' and playGame != 'n'):
        playGame = input('Invalid input. Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')