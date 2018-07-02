from nine_display import * 
import math 


board = [[0 for i in range(3)] for i in range(3)] # code 1 for blue, 2 for red. BOARD IS LIST OF COLUMNS!s
board_loc = [[0 for i in range(3)] for i in range(3)]

blue_tokens = [0 for i in range(3)]
red_tokens = [0 for i in range(3)]

def initialize(L):
	initialize_boardloc(L)
	win = display_board(L)
	place_tokens(win,L)
	play_game(win, L)
	win.getMouse()
	win.close()
	
	
def initialize_boardloc(L):
	for i in range(3):
		for j in range(3):
			board_loc[i][j] = [L/4 + i * L/4, L/4 + j* L/4]

# returns list of index for closest board point			
def find_closest_loc(point): 
	x = point.getX()
	y = point.getY()
	closest = [0,0] #index of closest point
	min_dist = 1000000
	
	for i in range(3):
		for j in range(3):
			distance = pow(board_loc[i][j][0] - x, 2) + pow(board_loc[i][j][1] - y, 2)
			if distance < min_dist:
				min_dist = distance
				closest = [i, j]
	return closest
			
			
			
def place_tokens(win,L):
	b_i = 0
	r_i = 0
	
	for i in range(6):
	
		good_move = False
		
		if game_over(board)[0]:
			print("game over")
			win.getMouse()
			win.close()
		
		while(not(good_move)):
			loc = win.getMouse()
			closest = find_closest_loc(loc)
			if(is_legal_place(closest)):
				if(i % 2 == 0):
					blue_tokens[b_i] = Token(Point(closest[0]* L/4 + L/4, closest[1]*L/4 + L/4), 30, closest,1)
					board[closest[0]][closest[1]] = 1
					blue_tokens[b_i].draw(win)
					blue_tokens[b_i].setFill("blue")
					b_i += 1
					
				
				if(i % 2 == 1):
					red_tokens[r_i] = Token(Point(closest[0]* L/4 + L/4, closest[1]*L/4 + L/4), 30,closest,2)
					
					board[closest[0]][closest[1]] = 2
					red_tokens[r_i].draw(win)
					red_tokens[r_i].setFill("red")
					r_i += 1
				
				good_move = True
					
					
		
		
		
		
# is space empty and is space one step away?	
def is_legal(token, destination):
	old_loc = token.loc # location is list [i,j] of coordinates
	distance = pow(old_loc[0] - destination[0], 2) + pow(old_loc[1]-destination[1],2)
	
	if board[destination[0]][destination[1]] != 0: # location is occupied
		return False
	
	if distance != 1:
		return False
	return True

def is_legal_place(destination):
	if board[destination[0]][destination[1]] != 0: # location is occupied
		return False
	return True

	
# return list [game_over?, winner]	
def game_over(board):
	for i in range(3): 
		if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
			return [True, board[i][0]]
		if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
			return [True, board[0][i]]
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0: # check diagonal
		return [True, board[0][0]]
	if board[2][0] == board[1][1] == board[0][2] and board[2][0] != 0: # check diagonal
		return [True, board[2][0]]
	
	return [False,0]
		

def play_game(win, L):
	# blue goes first
	turn = 0
	current_pieces = []
	g_over = False
	while(not g_over):
		if(turn % 2 == 0): 
			current_pieces = blue_tokens
		else:
			current_pieces = red_tokens
		
		
		selected_token = False
		while(not selected_token):
			selection = find_closest_loc(win.getMouse())
			selected_token = get_token_from_loc(selection, current_pieces)
			print(selection)
			
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
	
	print("game over")
			
def move_token(selected_token, legal_destination,L):
	old_loc = selected_token.loc
	board[old_loc[0]][old_loc[1]] = 0
	selected_token.loc = legal_destination
	board[legal_destination[0]][legal_destination[1]] = selected_token.team
	selected_token.move((legal_destination[0] - old_loc[0])* L/4, (legal_destination[1] - old_loc[1]) * L/4)
	
def get_token_from_loc(index, current_pieces):
	token = False
	
	for i in range(3):
		loc = current_pieces[i].loc
		
		if(index[0] == loc[0] and index[1] == loc[1]):
			token = current_pieces[i]
			
	
	return token
	
	
	
	
	


#initialize(800)   #OPEN THE GAME






#win.getMouse()
#win.close()