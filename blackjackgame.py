import random
import art
import os

def clear():os.system('cls') #on Windows System

def draw():
    card = cards[random.randint(0,len(cards)-1)]

    card_val = 0

    if card != "A" and card != "J" and card != "Q" and card != "K":
        card_val = int(card)

    elif card == "A":
        card_val = 1
        card_val2 = 11
    else:
        card_val = 11
    draw = [card,card_val]
    return draw

def hit():
    user_hand.append(draw())
    user_score = 0
    user_cards = []
    for card in user_hand:
        user_score += card[1]
        user_cards.append(card[0])
    return user_cards,user_score

def hit_dealer():
    dealer_hand.append(draw())
    dealer_score = 0
    dealer_cards = []
    for card in dealer_hand:
        dealer_score += card[1]
        dealer_cards.append(card[0])  
    return dealer_cards,dealer_score

def check_game(user_score,dealer_score):
    if user_score == 21 and user_score > dealer_score:
        print("YOU WON!!!")
    if user_score <=21 and user_score > dealer_score:
        print("YOU WON!!!")
    if user_score < 21 and user_score < dealer_score and dealer_score <= 21:
        print("YOU LOSE!!!")
    elif user_score == dealer_score:
        print("DRAW!!!")
    elif user_score > 21:
        print("YOU LOSE!!!")

print(art.logo)

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

game_on = True

game_play = input("Do you want to play a game of Blackjack? Type [y] or [n]:")

if game_play == "y":
    game_on = True
elif game_play == "n":
    game_on = False

while game_on:

    user_hand= [draw(),draw()]
    user_score = user_hand[0][1]+user_hand[1][1]
    user_cards = [user_hand[0][0],user_hand[1][0]]

    dealer_hand= [draw(),draw()]
    dealer_score1 = dealer_hand[0][1]
    dealer_cards1 = dealer_hand[0][0]
    dealer_score = dealer_hand[0][1]+dealer_hand[1][1]
    dealer_cards = [dealer_hand[0][0],dealer_hand[1][0]]

    print(f"Your cards: {user_cards}, current score: {user_score} \n")
    print(f"Dealer's first card: {dealer_cards1}, current dealer score: {dealer_score1}\n ")

    hit_on = True

    while hit_on: 
        
        if user_score == 21:
            while dealer_score < 17:
                dealer_cards, dealer_score = hit_dealer()

            hit_on = False
            
            break
        elif user_score > 21:
            hit_on = False
            
            break
        choice = input("Type [y] to get another card, type [n] to pass:")
        if choice == "y":
            user_cards, user_score = hit()
            print(f"Your cards: {user_cards}, current score: {user_score}\n ")
            print(f"Dealer's cards: {dealer_cards1}, current dealer score: {dealer_score1} \n")
        
            if user_score >21:
                hit_on = False
            elif user_score<21:
                next
        elif choice == "n":
            hit_on = False
            
    while dealer_score < 17:
        dealer_cards, dealer_score = hit_dealer()        
        

    print(f"Your final hand: {user_cards}, your final score: {user_score} \n")
    print(f"Dealer's final cards: {dealer_cards}, dealer final score: {dealer_score} \n")
    check_game(user_score,dealer_score)
            
    game_play = input("Do you want to play again? Type [y] or [n]:")
    if game_play == "y":
        game_on = True
        clear()
    elif game_play == "n":
        break


print("Thank you for playing!!!")
