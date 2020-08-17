import random
import time


dealer_cards = []
player_cards = []


def dealer_rules():
    if sum(dealer_cards) == 21:
        print("Dealer has Blackjack!")
        return
    elif sum(dealer_cards) > 21:
        print("Dealer has Busted! You Win!")
        return
    elif sum(dealer_cards) < 21:
        if sum(dealer_cards) > sum(player_cards):
            return print("Dealer Wins!")


def player_rules():
    if sum(player_cards) == 21:
        print("You have Blackjack!")
        return
    elif sum(player_cards) > 21:
        print("You have Busted!")
        return
    elif sum(dealer_cards) < 21:
        if sum(dealer_cards) < sum(player_cards):
            return print("You Win!")


def winner():
    if sum(dealer_cards) > sum(player_cards):
        dealer_rules()
        return
    elif sum(dealer_cards) < sum(player_cards):
        player_rules()
        return
    elif sum(dealer_cards) == sum(player_cards):
        return print("Tie!")


def dealer_hand():
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 11))
        if len(dealer_cards) == 2:
            print("Dealer has: X and", dealer_cards[1])


def player_hand():
    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 11))
        if len(player_cards) == 2:
            print("You have: " + str(sum(player_cards)) + " =", player_cards)


dealer_hand()
player_hand()


def dealer_turn():
    time.sleep(1)
    print("Dealer has: " + str(sum(dealer_cards)) + " =", dealer_cards)
    time.sleep(1)
    if sum(dealer_cards) > sum(player_cards):
        winner()
    else:
        while sum(dealer_cards) < 17:
            dealer_cards.append(random.randint(1, 11))
            print("Dealer has: " + str(sum(dealer_cards)) + " =", dealer_cards)
            time.sleep(1)
            if 17 <= sum(dealer_cards) <= 21:
                winner()
            elif sum(dealer_cards) > 21:
                dealer_rules()


def player_turn():
    if sum(player_cards) == 21:
        winner()
    elif sum(player_cards) > 21:
        player_rules()
    while sum(player_cards) < 21:
        option = str(input("\nHit or Stay "))
        if option == "Hit" or option == "hit":
            player_cards.append(random.randint(1, 11))
            print("You have: " + str(sum(player_cards)) + " =", player_cards)
            if sum(player_cards) == 21:
                winner()
            elif sum(player_cards) > 21:
                winner()
        elif option == "Stay" or option == "stay":
            dealer_turn()
            return


def game():
    player_turn()


game()