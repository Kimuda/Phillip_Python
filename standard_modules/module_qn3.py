#Qn3- Create a list that represents the cards of a poker deck e.g. A-Diamonds, 2-Diamonds, 3-Diamonds, etc. Then ask the user for a number of players, and give 5 random cards to each


#this programs below just randomly pics a card.
#import random
#rank = random.choice(('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'))
#suit = random.choice(('clubs','diamonds','hearts','spades'))
#card = rank +" "+ suit
#print (card) 


import random
#creating the deck of cards
cards = ['AS', 'KS', 'QS', 'JS', '10S', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S',\
         'AD', 'KD', 'QD', 'JD', '10D', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D',\
         'AC', 'KC', 'QC', 'JC', '10C', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C',\
         'AH', 'KH', 'QH', 'JH', '10H', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H']
#5 hands
hand1 = []
hand2 = []
hand3 = []
hand4 = []
hand5 = []
#shuffle the cards
random.shuffle(cards)
num = int(input('How many cards to deal to each player? '))
while num > 0:
    hand1.append(cards.pop(0)) #take the first item from list cards,its now less one card
    hand2.append(cards.pop(0)) #take the first  item from list cards,it's now less two cards
    hand3.append(cards.pop(0)) #take the first item from list cards, it's now less three cards
    hand4.append(cards.pop(0)) #the while loop will do this the number of num-specified times
    hand5.append(cards.pop(0)) 
    num = num - 1

print ('hand one is: ',hand1)
print ('hand two is: ',hand2)
print ('hand three is: ',hand3)
print ('hand four is: ',hand4)
print ('hand five is: ',hand5)
print ('the cards remaining in the deck are: ',cards)

