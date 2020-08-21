''' This is a Text based shkobba game written in Python By Musab Schluck
it is simple but it has all the logic og the game.
and has two agents that plays randomly
it needs development in terms of making the agents play in a smarter way
This could be a valuable asset for anyone who wants to make a shkobba game, because it hase all the logic of the game
'''
from random import shuffle, randint, choice

class Player():
    def __init__(self, name):
        self.name = name
        self.has_eaten_the_last_wakla = False
        self.hand = []		# What a player has in his hand at a specific time
        self.cards = []		# What a player ate from cards.
        self.shkobbat = []
        self.score = 0		# player's score throughout the game
        

    def eat_or_put(self, board_cards, other, dick):
    	while True:
	        q = ["n"]
	        q += board_cards
	        wakla_list = choice(q) # input("example 'd6' or 'd6 + c2'\nif you have nothing to eat type'n'\nwhat do you wanna eat: ")
	        wakla_list = wakla_list.split(" + ")
	        # deciding whhat to eat
	        if set(wakla_list).issubset(set(board_cards)) or wakla_list == ["n"]:
	        	pass
	        else:
	        	# print("what you wanna eat is not valid")
	        	continue

	        card_put = choice(self.hand) # input("choose a card from your hand to put on the table: ")
	        # deciding what to put
	        if card_put in self.hand:
	        	pass
	        else:
	        	# print("you can't put this card")
	        	continue

	        # cick if you can eat what you want with what you wanna put
	        if wakla_list == ["n"]:
	        	board_cards.append(self.hand.pop(self.hand.index(card_put)))
	        	break

	        elif int(card_put[1:]) == sum(list_of_cards_to_list_of_numbers(wakla_list)):
	        	self.cards.append(self.hand.pop(self.hand.index(card_put)))
	        	for i in wakla_list:
	        		self.cards.append(board_cards.pop(board_cards.index(i)))
	        	self.has_eaten_the_last_wakla = True
	        	other.has_eaten_the_last_wakla = False
	        	# cecking if it's shkobba
	        	if board_cards == [] and len(self.hand) + len(other.hand) != 6:
	        		if len(dick) == 0 and len(self.hand) == 3 and self.name == "p2":
	        			pass
	        		else:
	        			self.shkobbat.append(card_put)
	        	break

	        else:
	        	# print("what you put can't eat what you wanna eat")
	        	continue

 
class Game():
    def __init__(self):
        self.running = True
        self.c_player = p1
        self.winning_number = 31
        self.dick = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10',
                     'd1','d2','d3','d4','d5','d6','d7','d8','d9','d10',
                     'h1','h2','h3','h4','h5','h6','h7','h8','h9','h10',
                     'c1','c2','c3','c4','c5','c6','c7','c8','c9','c10']
        shuffle(self.dick)
        
        self.floor = [self.dick.pop(),
                      self.dick.pop(),
                      self.dick.pop(),
                      self.dick.pop()]

    def calculate_score(self, player_1, player_2):
    	# 8, 9, 10 diamond points
        if list_of_cards_to_list_of_types(player_1.cards).count("d") in [0,1,2,8,9,10]:
            # 9 diamond
            if list_of_cards_to_list_of_types(player_1.cards).count("d") == 9:
                print("player 1 has collected 9 diamons")
                player_2.score = 0
            elif list_of_cards_to_list_of_types(player_2.cards).count("d") == 9:
                print("player 2 has collected 9 diamons")
                player_1.score = 0
	    	# 8 diamonds
            elif list_of_cards_to_list_of_types(player_1.cards).count("d") == 8:
                print("player 1 has collected 8 diamons")
                player_1.score += 10
            elif list_of_cards_to_list_of_types(player_2.cards).count("d") == 8:
                print("player 2 has collected 8 diamons")
                player_2.score += 10
        else:
        	# 6, 7 diamond point
        	if list_of_cards_to_list_of_types(player_1.cards).count("d") in [6, 7]:
        		player_1.score += 1
        	if list_of_cards_to_list_of_types(player_2.cards).count("d") in [6, 7]:
        		player_2.score += 1
        	# 7ya
        	if "d7" in player_1.cards:
        		player_1.score += 1
        	else:
        		player_2.score += 1
        	# karta point
        	if len(player_1.cards) > 20:
        		player_1.score += 1
        	elif len(player_2.cards) > 20:
        		player_2.score += 1
        	# bermela point
        	if list_of_cards_to_list_of_numbers(player_1.cards).count("7") > 2:
        		player_1.score += 1
        	elif list_of_cards_to_list_of_numbers(player_2.cards).count("7") > 2:
        		player_2.score += 1
        	elif list_of_cards_to_list_of_numbers(player_1.cards).count("6") > 2:
        		player_1.score += 1
        	elif list_of_cards_to_list_of_numbers(player_2.cards).count("6") > 2:
        		player_2.score += 1
        	# shkobba point & clearing the list
        	player_1.score += sum(list_of_cards_to_list_of_numbers(player_1.shkobbat))
        	player_2.score += sum(list_of_cards_to_list_of_numbers(player_2.shkobbat))
        	player_1.shkobbat.clear()
        	player_2.shkobbat.clear()

        print("\n\n##### Summary #####")
        print("player 1 cards", player_1.cards)
        print("player 1 number of cards: {}".format(len(player_1.cards)))
        print("player 1 score", player_1.score)
        print("player 2 cards", player_2.cards)
        print("player 2 number of cards: {}".format(len(player_2.cards)))
        print("player 2 score", player_2.score)
        print("floor cards: ", self.floor)
        # clearing players hands
        player_1.cards = []
        player_2.cards = []


    def check_if_a_player_won(self,player_1,player_2):
        # 10 diamond
    	if list_of_cards_to_list_of_types(player_1.cards).count("d") == 10:
    		print("player 1 has won by collecting 10 diamons")
    		self.running = False
    	elif list_of_cards_to_list_of_types(player_2.cards).count("d") == 10:
    		print("player 2 has won by collecting 10 diamons")
    		self.running = False
    	elif player_1.score >= self.winning_number and player_2.score < self.winning_number:
    		print("player 1 has won by passing the {} score alone".format(self.winning_number))
    		self.running = False
    	elif player_2.score >= self.winning_number and player_1.score < self.winning_number:
    		print("player 2 has won by passing the {} score alone".format(self.winning_number))
    		self.running = False
    	if player_1.score > self.winning_number and player_2.score > self.winning_number:
    		winning_number += 30

    
    def dist_card_for_each_round(self, player_1, player_2):
        for card in range(3):
            p1.hand.append(self.dick.pop())
            p2.hand.append(self.dick.pop())

    def giving_the_remaining_floor_cards_to_the_player_that_ate_last(self, player_1, player_2):
    	if len(self.dick) == 0 and len(player_1.hand) + len(player_2.hand) == 0:
    		if player_1.has_eaten_the_last_wakla == True:
    			player_1.cards += self.floor
    			self.floor.clear()
    		elif player_2.has_eaten_the_last_wakla == True:
    			player_2.cards += self.floor
    			self.floor.clear()



def list_of_cards_to_list_of_numbers(l1):
	return [int(x[1:]) for x in l1]

def list_of_cards_to_list_of_types(l1):
	return [x[0] for x in l1]


print("New Game")
p1 = Player("p1")
p2 = Player("p2")
new_game = Game()
while new_game.running == True:
	new_game = Game()
	for i in range(6):
		new_game.dist_card_for_each_round(p1, p2)
		for j in range(3):
			print("player 1 hand:", p1.hand)
			print("floor cards:", new_game.floor)
			print(len(new_game.dick))
			p1.eat_or_put(new_game.floor, p2, new_game.dick)
			print("player 2 hand:", p2.hand)
			print("floor cards:", new_game.floor)
			print(len(new_game.dick))
			p2.eat_or_put(new_game.floor, p1, new_game.dick)
			new_game.giving_the_remaining_floor_cards_to_the_player_that_ate_last(p1, p2)
	new_game.calculate_score(p1, p2)
	new_game.check_if_a_player_won(p1, p2) # if a player won new_game.running == False, this will terminate the loop



