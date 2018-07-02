from graphics import *
def initialize_board(L):
    win = GraphWin("My Circle", L, L)
    
    a = Circle(Point(L/2,L/2), L/16) #inner circle (width , length)
    a.draw(win)
    
    b = Circle(Point(L/2,L/2), L/4) # outer circle
    b.draw(win)
    
    c = Circle(Point(L/2,3*L/4), L/8) #south circle
    c.draw(win)
    
    d = Circle(Point(3*L/4,L/2), L/8) #Right circle
    d.draw(win)
    
    e = Circle(Point(L/4,L/2), L/8) # Left circle
    e.draw(win)
    
    f = Circle(Point(L/2,L/4), L/8) # North Circle
    f.draw(win)
    
    Y = Line(Point(L/2, 3*L/4), Point(L/2, L/4))
    Y.draw(win)
    
    X = Line(Point(3*L/4, L/2), Point(L/4, L/2))
    X.draw(win)
    
    initialize_spots(win)
    return win
    
# takes in board visual and initializes locations
# returns list of location objects

def initialize_spots(win):
	L = 800
	test = Circle(Point(L/4 + L/40, L/2 - L/8), L/50)
	test.setFill("black")
	test.draw(win)
	
# Takes in window and place tokens. 
# returns list of tokens
#def initialize_tokens(win):
	