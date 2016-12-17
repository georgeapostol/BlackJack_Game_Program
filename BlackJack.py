from Deck import Deck
from Hand import Hand

new_deck = Deck()

print(new_deck.cards)

print "Welcome to the game Black Jack!"

continue_playing = True
while continue_playing:


    my_hand = Hand()
    dealer_hand = Hand()

    # both players draw 2
    drawn_card = new_deck.draw_card()
    drawn_card_2 = new_deck.draw_card()

    dealer_card = new_deck.draw_card()
    dealer_card_2 = new_deck.draw_card()
    dealer_hand.add_card(dealer_card)
    dealer_hand.add_card(dealer_card_2)
    my_hand.add_card(drawn_card)
    my_hand.add_card(drawn_card_2)

    # human draws or not

    my_hand.print_hand()
    dealer_hand.print_hand()

    hit = raw_input("Would you like to hit?").lower() == "yes"

    while hit:
        my_hand.add_card(new_deck.draw_card())

        #check if busted
        my_hand.print_hand()
        if my_hand.is_busted():
            hit = False
        else:
            hit = raw_input("Would you like to hit?").lower() == "yes"

    # if human still in the game, dealer draws if < 17

    hand_lose = False

    if my_hand.is_busted():
        print "You lose "
        hand_lose = True
    else:
        if dealer_hand.get_score() < 17:
            dealer_hand.add_card(new_deck.draw_card())

    if hand_lose == False:
        if dealer_hand.is_busted():
            print "You win!"
        elif my_hand.get_score() > dealer_hand.get_score():
            print "You win!"
        else:
            print "You lose"
    my_hand.print_hand()
    dealer_hand.print_hand()

    response = raw_input("Do you wish to continue Playing?: ")
    if response.lower() == "no":
        continue_playing = False

