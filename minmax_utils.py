from nine_holes import *
import copy
import math #math.inf
import numpy as np
from minimax_play import *

#board = [[0 for i in range(3)] for i in range(3)]
#board = [[1,0,0],[2,0,1],[2,2,1]]


# returns list of next board states during setup phase
# team is 1 for blue, 2 for red
def next_moves_setup(board, team): 
	next_boards = []
	for i in range(3):
		for j in range(3):
			if board[i][j] == 0:
				new_board = copy.deepcopy(board)
				new_board[i][j] = team
				next_boards.append(new_board)
	return next_boards

#blue is positive, red is negative
#returns infinities if game over
#returns number of blue twos minus number of red twos
def setup_heuristic(board, maximizing_player,depth):				
	# old code			
	game = game_over(board)
	if game[0]:
		if game[1] == 1:
			return math.inf
		if game[1] == 2:
			return -math.inf
				
	
	twos = count_twos(board)
	
	if maximizing_player:
		return -twos[1] #twos[0] - 2*twos[1] 
	else:
		return twos[0]  #2*twos[0] - twos[1]
	
# returns number of two in a row sequences
def count_twos(board):
	num_diagonals = [0,0] # first for blue(1), second for red(2)
	
	for i in range(3):
		for j in range(3):
			current_val = board[i][j]
			if(i < 2):
				right_val = board[i + 1][j]
				if right_val == current_val:
					if right_val == 1:
						num_diagonals[0] += 1
					if right_val == 2:
						num_diagonals[1] += 1
			if(j < 2):
				lower_val = board[i][j+1]
				if lower_val == current_val:
					if lower_val == 1:
						num_diagonals[0] += 1
					if lower_val == 2:
						num_diagonals[1] += 1
			if(j < 2 and i < 2):
				diag_val = board[i + 1][j+1]
				if diag_val == current_val:
					if diag_val == 1:
						num_diagonals[0] += 1
					if diag_val == 2:
						num_diagonals[1] += 1
	return num_diagonals
						
	

# blue(team = 1) is maximizing player, so for red, team = 0
# num_pieces is equivalent to depth. max_depth= 6
# returns list of [score, board]

##to do -- setup alpha/beta pruning for this?
def minimax_setup(board, depth, maximizing_player):
	game_end = game_over(board)[0]
	if game_end:
		return [setup_heuristic(board, maximizing_player, depth), board]
	if depth == 6: #play game for two rounds and see what happens
		if maximizing_player:
			score = minimax_play(board, 1, -math.inf, math.inf, 1)[0]
			return [score, board]
		else:
			score = minimax_play(board, 1, -math.inf, math.inf, 2)[0]
			return [score, board]
	
	team = 1
	if not maximizing_player:
		team = 2	
	children = next_moves_setup(board, team)
	
	if maximizing_player: # blue team - maximizing
		maxEval = -math.inf
		score_board = [maxEval, board]
		
		for child in children:
			eval = minimax_setup(child, depth + 1, 0)[0]
			old_eval = maxEval
			maxEval = max(maxEval, eval)
			if old_eval != maxEval:
				score_board = [maxEval, child]
				
		return score_board
	
	else: # red team - minimizing
		minEval = math.inf
		score_board = [minEval, board]
		
		for child in children:
			eval = minimax_setup(child, depth + 1, 1)[0]
			old_eval = minEval
			minEval = min(eval, minEval)
			if old_eval != minEval:
				score_board = [minEval, child]

		return score_board
			
			

					
			
			
#board = [[1,1,0],[0,2,2],[0,0,0]]
#print(minimax_setup(board, 4, 1))	
#print(board)		
			