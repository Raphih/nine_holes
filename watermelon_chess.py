from graphics_test import *

space_connections = {1:[12,13,2], 2:[1,13,3],3:[2,14,4],
			   4:[3,5,14],5:[4,14,6], 6:[5,7,15],
			   7:[6,15,8], 8:[7,15,9], 9:[8,10,16],
			   10:[9,11,16], 11: [10,16,12], 12:[11,1,13],
			   13:[12,1,2,18], 14:[3,4,5,19], 15:[6,7,8,20],
			   16:[9,10,11, 17], 17:[16,18,21,20], 18: [13,19,17,21],
			   19:[14,18,20,21], 20:[17,19,15,21], 21:[17,18,19,20]
			   }

space_locations = {} #to be filled during board initialization

board = [0 for i in range(21)] 
initial_blue = [12,11,10,9,8,16]
initial_white = [2,3,4,5,6,14]

def initialize():
	# fill tokens on board
	# Note: indexed board positions starting from one, so subtract one to get 
	# location in board array
	for x in initial_blue:
		board[x - 1] = 1
	for y in initial_white:
		board[y-1] = 2
	win = initialize_board(800)
	initialize_spots(win)
	win.getMouse() # pause for click in window
	win.close()
		
		
		
initialize()

		
	
