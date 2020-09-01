# Blackjack
import random
import time

# Dealer Cards:
dealer_cards = []
# Player Cards:
player_cards = []

# Dealing the Cards (Dealer Cards):

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has: X and", dealer_cards[1])

# Dealing the Cards (Player Cards):

while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have: " + str(sum(player_cards)) + " =", player_cards)

# The Game:

while sum(player_cards) < 21:
    action_taken = str(input("\nHit or Stay "))
    if action_taken == "Hit" or action_taken == "hit":
        player_cards.append(random. randint(1, 11))
        print("You now have: " + str(sum(player_cards)) + " =", player_cards)
        if sum(player_cards) == 21:
            print("You have Blackjack! " + str(sum(player_cards)) + " =", player_cards)
        elif sum(player_cards) > 21:
            print("You have Busted! Dealer Wins!")

    elif action_taken == "Stay" or action_taken == "stay":
        while sum(dealer_cards) < 17:
            dealer_cards.append(random.randint(1, 11))
            print("Dealer has: " + str(sum(dealer_cards)) + " =", dealer_cards)
            time.sleep(1)
            if sum(dealer_cards) == 21:
                print("Dealer has Blackjack!")
            elif sum(dealer_cards) > 21:
                print("Dealer has Busted! You Win!")
        break


