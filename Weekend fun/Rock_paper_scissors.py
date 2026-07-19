# name: Rock_paper_scissors
# read rock, paper or scissors from player_1
# read rock, paper or scissors from player_2
# if player_1 == Player_2 tie
# elif player_1 == rock 
# nested if player_2 == scissors print "player_1 wins"
# nested else (player_2 == paper) print "player 2 wins"
# elif player_1 == paper
# nested if player_2 == rock print "player_1 wins"
# nested else (player_2 == scissors) print "player 2 wins"
# elif player_1 == scissors
# nested if player_2 == paper print "player_1 wins"
# nested else (player_2 == rock) print "player 2 wins"
# 

Player_1 = input("Player 1 to enter 'rock', 'paper' or 'scissors': ")

Player_2 = input("Player 2 to enter 'rock', 'paper' or 'scissors': ")

if Player_1 == Player_2 :
	print("Tie")
elif Player_1 == "rock" :
	if Player_2 == "scissors" :
		print("Player 1 wins")
	else :
		print("Player 2 wins")
elif Player_1 == "paper" :
	if Player_2 == "rock" :
		print("Player 1 wins")
	else :
		print("Player 2 wins")
elif Player_1 == "scissors" :
	if Player_2 == "paper" :
		print("Player 1 wins")
	else :
		print("Player 2 wins")