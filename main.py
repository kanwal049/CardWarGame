import random
values = {'Ace': 14, 'King': 13, 'Queen': 12, 'Jack': 11, 'Two': 2,
          'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, "Eight": 8, "Nine": 9, 'Ten': 10}

suits = ('Diamonds', 'Hearts', 'Clubs', 'Spades')
ranks = ('Ace', 'King', 'Queen', 'Jack', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', "Eight", 'Nine', 'Ten')
game_on = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop(0)


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, cards):
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


while game_on:

    while True:
        try:
            start = input("Start Game? (Y or N): ")
            if start not in ['y', 'Y', 'N', 'n']:
                raise TypeError()
        except:
            print('Wrong Input!!!')

        else:
            break

    if start in ['N', 'n']:
        break

    else:
        print('Welcome to Card War!!!')

        #create Players
        player_one = Player('Kanwal')
        player_two = Player('Shahzeb')


        #create a deck
        new_deck = Deck()

        #Shuffle deck
        new_deck.shuffle()

        #devide the deck cards into 2
        player_one.add_cards(new_deck.all_cards[:26])
        player_two.add_cards(new_deck.all_cards[26:])

        #make sure both players have enough cards to player
        player_one_cards_in_hand = []
        player_two_cards_in_hand = []
        players_have_card = True

        #print(player_one.remove_one())
        #print(player_one.remove_one())
        #print(len(player_one.all_cards))


        while players_have_card:

            if len(player_one.all_cards) < 1:
                print(f'{player_one.name} out of cards. {player_two.name} Won !!!')
                players_have_card = False
                break

            elif len(player_two.all_cards) < 1:
                print(f'{player_two.name} out of cards. {player_one.name} Won !!!')
                players_have_card = False
                break

            else:
                #start dealing
                player_one_cards_in_hand.append(player_one.remove_one())
                #print(f'After remove player one has {len(player_one.all_cards)}')
                player_two_cards_in_hand.append(player_two.remove_one())
                #print(f'After remove player two has {len(player_two.all_cards)}')

                #Show player cards
                print(f"{player_one.name}'s card is {player_one_cards_in_hand[0]}")
                print(f"{player_two.name}'s card is {player_two_cards_in_hand[0]}")

                if player_one_cards_in_hand[0].value > player_two_cards_in_hand[0].value:
                    print(f"{player_one.name}'s card is bigger in value than {player_two.name}'s card")
                    print(f"{player_one.name} will get all the cards!!!")
                    # add both players cards at the end of player one's cards
                    player_one.all_cards.extend(player_one_cards_in_hand + player_two_cards_in_hand)

                    player_one_cards_in_hand = []
                    player_two_cards_in_hand = []

                    print(f"player one has {len(player_one.all_cards)} number of cards")
                    print(f"player two has {len(player_two.all_cards)} number of cards")

                elif player_one_cards_in_hand[0].value < player_two_cards_in_hand[0].value:
                    print(f"{player_two.name}'s card is bigger in value than {player_one.name}'s card")
                    print(f"{player_two.name} will get all the cards!!!")
                    # add both players cards at the end of player two's cards
                    player_two.all_cards.extend(player_one_cards_in_hand + player_two_cards_in_hand)

                    player_one_cards_in_hand = []
                    player_two_cards_in_hand = []

                    print(f"player one has {len(player_one.all_cards)} number of cards")
                    print(f"player two has {len(player_two.all_cards)} number of cards")


                
                # check war situation
                else:

                    print(f"{player_two.name}'s card and {player_one.name}'s card is equal in value.")
                    print("LET THE WAR BEGIN!!!")
                    war = True
                    while war:
                        #check if both player have 5 cards to draw
                        if len(player_one.all_cards) < 15:
                            print(f'{player_one.name} out of cards. {player_two.name} Won !!!')
                            players_have_card = False
                            break

                        elif len(player_two.all_cards) < 15:
                            print(f'{player_two.name} out of cards. {player_one.name} Won !!!')
                            players_have_card = False
                            break

                        else:
                            #both players have 5 cards
                            #deal 5 cards each
                            for card in range(1, 15):
                                player_one_cards_in_hand.insert(0, player_one.remove_one())
                                player_two_cards_in_hand.insert(0, player_two.remove_one())

                            if player_one_cards_in_hand[0].value > player_two_cards_in_hand[0].value:

                                print(f"{player_one.name}'s card is bigger in value than {player_two.name}'s card")
                                print(f"{player_one.name} will get all the cards!!!")

                                # add both players cards at the end of player one's cards
                                player_one.all_cards.extend(player_one_cards_in_hand + player_two_cards_in_hand)

                                player_one_cards_in_hand = []
                                player_two_cards_in_hand = []

                                print(f"player one has {len(player_one.all_cards)} number of cards")
                                print(f"player two has {len(player_two.all_cards)} number of cards")

                            elif player_one_cards_in_hand[0].value < player_two_cards_in_hand[0].value:
                                print(f"{player_two.name}'s card is bigger in value than {player_one.name}'s card")
                                print(f"{player_two.name} will get all the cards!!!")

                                # add both players cards at the end of player one's cards
                                player_two.all_cards.extend(player_one_cards_in_hand + player_two_cards_in_hand)

                                player_one_cards_in_hand = []
                                player_two_cards_in_hand = []

                                print(f"player one has {len(player_one.all_cards)} number of cards")
                                print(f"player two has {len(player_two.all_cards)} number of cards")

                                break

                            else:
                                print(f"{player_two.name}'s card and {player_one.name}'s card is equal in value.")
                                print("LET THE WAR BEGIN!!!")
                                continue























