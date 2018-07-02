# f = Circle(Point(L/2,L/4), L/8) # North Circle
 #   f.draw(win)
    
 #   Y = Line(Point(L/2, 3*L/4), Point(L/2, L/4))
 #   Y.draw(win)
 
 #win.getMouse() # pause for click in window
 #win.close()

from graphics import *
L = 800


def display_board(L):

	win = GraphWin("nine_holes", L, L)
	
	square = Rectangle(Point(L/4,L/4),Point(3*L/4, 3*L/4))
	square.draw(win)
	
	hor_1 = Line(Point(L/4, L/2), Point(3*L/4, L/2))
	hor_1.draw(win)
	
	
	ver_1 = Line(Point(L/2, L/4), Point(L/2, 3*L/4))
	ver_1.draw(win)
	
	return win
	
	#token_1 = Token(Point(L/8, L/8), L/32)
	#token_1.draw(win)
	#print(token_1.size)
	
	#win.getMouse()
	#win.close()

class Token(Circle):
	def __init__(self, center, radius,closest,team):
		Circle.__init__(self, center, radius)
		self.loc = closest
		self.team = team
		

#display_board(800)