import copy
import math
from nine_holes import *
from minmax_utils import *

# first call is minimax_play(depth, -inf, inf, maxmizing_player)
#alpha and beta represent best score each side can achieve, assuming best 
#play from opponent. so -inf is worst case for alpha
# if beta < alpha, means minimizing player had better option earlier
# on in tree, so we prune. 
# value of alpha, beta keep track of worst case for max, min players
def minimax_play(board, depth, alpha, beta, maximizing_player):
	game_end = game_over(board)[0]	
	
	if game_end or depth == 0:
		#print(board, depth)
		return[play_heuristic(board, depth), board]
	
	team = 1
	if not maximizing_player:
		team = 2
	children = next_moves_play(board, team)
	
	if maximizing_player:
		maxEval = -math.inf
		score_board = [maxEval, board]
		
		for child in children:
			#if depth == 5:
			#	print(child)
			eval = minimax_play(child, depth - 1, alpha, beta, 0)[0]
			
			
			old_eval = maxEval
			maxEval = max(maxEval, eval)
			if old_eval != maxEval:
				score_board = [maxEval, child]
			alpha = max(alpha, eval)
			if beta <= alpha: #best/worst case for a player?
				#print("done")
				break # don't explore what other team will do
		return score_board
	
	else: #red team - minimizing
		minEval = math.inf
		score_board = [minEval, board]
		
		for child in children:
			eval = minimax_play(child, depth - 1, alpha, beta, 1)[0] # change to alpha, beta
			old_eval = minEval
			minEval = min(eval, minEval)
			if old_eval != minEval: 
				score_board = [minEval, child]
			beta = min(beta, eval)
			if beta <= alpha:
				break
		return score_board
	
#next moves returns list of next board states for game
# when called on this file w/ premade board, it works
# only returns old board when called from pvsai
def next_moves_play(board, team):
	#print("team: ", team)
	children = []
	legal_pos = range(3)
	
	for i in range(3):
		for j in range(3):
			if board[i][j] == team:
				for di in range(-1,2):
					for dj in range(-1,2):
						if i + di in legal_pos and j + dj in legal_pos:
							if legal_ai(board,i,di, j,dj):
								new_board = get_new_board(board, i,di, j,dj,team)
								#print("new_board", new_board)
								children.append(new_board)
	return children
								
def legal_ai(board, i,di, j,dj):
	if abs(di) + abs(dj) > 1:
		return False
	target = board[i + di][j + dj]
	if(target != 0):
		return False
	return True

# guaranteed that get_new_board has received a legal move	
def get_new_board(board, i,di,j,dj,team):
	#print("get new board: ")
	#print(i,di,j,dj,team)
	new_board = copy.deepcopy(board)
	new_board[i + di][j+ dj] = team
	new_board[i][j] = 0
	#print(new_board)
	return new_board
	
# need to improve this	
def play_heuristic(board, depth):
	game = game_over(board)
	if game[0]:
		if game[1] == 1:
			return 1000 * depth #math.inf
		if game[1] == 2:
			return -1000 * depth
	#twos = count_twos(board)
	#return twos[0] - twos[1]
	return 0

#board = [[1,0,0],[2,1,1],[2,2,0]]
#print(minimax_play(board, 3, -math.inf, math.inf, 1))	

#problem: stopping at first solution it finds in DFS? so if solution in earlier layer along different path, don't evaluate?			
#print(next_moves_play(board, 1))
#print(board)
		