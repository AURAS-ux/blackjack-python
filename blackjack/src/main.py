import os
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear():
    os.system("cls")
    
def draw_cards():
    drawn=[]
    drawn.append(cards[random.randint(0,len(cards)-1)])
    return drawn

def cards_sum(card=[]):
    sum=0 
    for i in range(len(card)):
        sum+=card[i][0]
    return sum

def game_mechanics(playerCards,dealerCards):
    if cards_sum(dealerCards)<16:
        dealerCards.append(draw_cards())
    elif cards_sum(playerCards)>21:
        print("BUST!You lose.") 
    elif cards_sum(dealerCards)>21:
        print("You win.")
    elif cards_sum(playerCards)>cards_sum(dealerCards):
        print("You win.")
    elif cards_sum(playerCards)==cards_sum(dealerCards):
        print("Draw.")
    elif cards_sum(playerCards)<cards_sum(dealerCards):
        print("You lose.")
        
endGame=False
while not endGame:
    yourCards=[]
    dealerCards=[]
    yourCards.append(draw_cards())
    yourCards.append(draw_cards())
    dealerCards.append(draw_cards())
    dealerCards.append(draw_cards())
    for i in range(len(yourCards)):
        print(f"Your cards are {yourCards[i][0]}")
    print(f"Dealer's first card is {dealerCards[0][0]}")
    choice=input("You wish to draw another card?\n Type yes(y) or no(n)\n")
    if choice=="yes" or choice=="y":
        yourCards.append(draw_cards())
        game_mechanics(yourCards,dealerCards)
        print(f"Your final hand was {yourCards}\nWhile dealer had {dealerCards}")
        endGame=True
    elif choice=="no" or choice=="n":
        game_mechanics(yourCards,dealerCards)
        print(f"Your final hand was {yourCards}\nWhile dealer had {dealerCards}")
        endGame=True
    