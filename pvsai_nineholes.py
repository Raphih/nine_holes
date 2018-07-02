from nine_display import * 
from nine_holes import *
from graphics import *
from minmax_utils import *
from minimax_play import *
import random

player_id = 0
ai_id = 0

def initialize_pvai(L):
	initialize_boardloc(L)
	win = display_board(L)
	place_tokens_pvsai(win,L)
	#print(board)
	play_game_pvsai(win, L)
	win.getMouse()
	win.close()
	
def place_tokens_pvsai(win, L):

	player = 0
	ai = 0
	player_select = random.choice([0,1]) # is player blue(0) or red(1)?
	b_i = 0
	r_i = 0
	global player_id
	global ai_id
	
	if player_select == 0: # assign player, ai identity of blue, red on board
		player = [1, blue_tokens, b_i, "blue"] # [board_id, tokenlist, index, color]
		ai = [2,red_tokens, r_i,"red"]
		player_id = 1
		ai_id = 2
	else:
		player = [2,red_tokens, r_i,"red"]
		ai = [1, blue_tokens, b_i, "blue"]
		player_id = 2
		ai_id = 1
	
			
	print("ai_id: ", ai_id)
	for i in range(6):
		good_move = False
		
		if game_over(board)[0]:
			print("game over")
			win.getMouse()
			win.close()
	
		while(not(good_move)):
			
			if i % 2 != player_select: # Turn is ai
				#print("ai turn")
				new_board = minimax_setup(board, i,-math.inf, math.inf,player_select)[1] # get ai move
				move_ai(board, new_board,ai,win) # update board and tokens list
				good_move = True
			else: # turn is players
				#print("player turn")
				loc = win.getMouse()
				closest = find_closest_loc(loc)
				if(is_legal_place(closest)):
					player[1][player[2]] = Token(Point(closest[0]* L/4 + L/4, closest[1]*L/4 + L/4), 30, closest,player[0])
					player[1][player[2]].draw(win)
					player[1][player[2]].setFill(player[3])					
					player[2] += 1
					board[closest[0]][closest[1]] = player[0]
					#print(board)
					#print("board updated")
				good_move = True
	if game_over(board)[0]:
		print("game over")
					
			
# find difference between old board and new board, 
# make new token, update 	

		
def move_ai(board, new_board, ai,win):
	
	new_pos = get_difference(board, new_board)
	print(new_pos)
	
	ai[1][ai[2]] = Token(Point(new_pos[0]* L/4 + L/4, new_pos[1]*L/4 + L/4), 30, new_pos,ai[0])
	ai[1][ai[2]].draw(win)
	ai[1][ai[2]].setFill(ai[3])
	ai[2] += 1
	board[new_pos[0]][new_pos[1]] = ai[0]


# returns location of difference 
# between old and new board	
def get_difference(board, new_board):
	loc = []
	for i in range(3):
		for j in range(3):
			if board[i][j] != new_board[i][j]:
				
				loc = [i,j]
	return loc
	
def play_game_pvsai(win, L):
	# blue goes first
	turn = 1
	sides = [2,1]
	current_pieces = []
	g_over = False
	#print("ai_id", ai_id)
	while(not g_over):
		
	
		if sides[turn % 2] == player_id: # player's turn
			#print("player_turn")
			#print(board)
			if player_id == 1:
				current_pieces = blue_tokens
			else:
				current_pieces = red_tokens
			
			selected_token = False
			while(not selected_token):
				selection = find_closest_loc(win.getMouse())
				selected_token = get_token_from_loc(selection, current_pieces)
			selected_token.setOutline("green")
			
			move_resolved = False
			while(not move_resolved):
				destination = find_closest_loc(win.getMouse())
				if is_legal(selected_token, destination):
					move_token(selected_token, destination,L)
					selected_token.setOutline("black")
					move_resolved = True
				
			turn += 1
			g_over = game_over(board)[0]
		
		else: # ai's turn
			
		
			maximizing_player = 0
			if player_id == 1:
				current_tokens = red_tokens
			else:
				current_tokens = blue_tokens
				maximizing_player = 1
			
			move = minimax_play(board, 4, -math.inf, math.inf, maximizing_player)[1]#next_moves_play(board, ai_id)[0] # get first next legal move - just to test out rest of function
			change_loc = get_difference_both(board, move)
			#print("change_loc", change_loc)
			
			update_ai(change_loc, ai_id)
			turn += 1
			g_over = game_over(board)[0]
			
	print("game over")
			
			
			
	
	
#returns list of [old_location, new_location] for a token	
def get_difference_both(old_board, new_board):
	#print("old_board")
	#print(old_board)
	#print("new_board")
	#print(new_board)
	old_loc = []
	new_loc = []
	for i in range(3):
		for j in range(3):
			if board[i][j] != new_board[i][j]:
				if board[i][j] != 0: # token was moved from this loc
					old_loc = [i,j]
				else: # token moved to this loc
					new_loc = [i,j]
					
	return [old_loc, new_loc]
			
# input: list of [old_loc, new_loc] for token and ai's team
# output: nothing, but updates board and tokens
def update_ai(change_loc, ai_id):
	#print("old_board", board)
	
	#print("change_loc ", change_loc)
	token_list = []
	old_loc = change_loc[0]
	new_loc = change_loc[1]
	if ai_id == 1:
		token_list = blue_tokens
	else: 
		token_list = red_tokens
	selected_token = 0
	
	for token in token_list: 
		#print("old_token_loc ", token.loc)
		if token.loc[0] == old_loc[0] and token.loc[1] == old_loc[1]:
			selected_token = token
			#print("selected this token: ", token.loc)
			break # for some reason this break is necessary
			
	board[old_loc[0]][old_loc[1]] = 0
	token.loc = new_loc
	board[new_loc[0]][new_loc[1]] = ai_id
	selected_token.move((new_loc[0] - old_loc[0])* L/4, (new_loc[1] - old_loc[1]) * L/4)
		

initialize_pvai(800)