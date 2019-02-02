import pygame 
import random 

#define variables for game
FPS = 60

#size of our window
Window_Width = 400
Window_Height = 400

#size of our paddle
Paddle_Width = 10
Paddle_height = 60

#size of our ball
Ball_Width = 10
Ball_Height = 10

#Speed of our paddle & ball
Paddle_speed = 2
Ball_x_Speed = 3
BAll_Y_SPEED = 2

#RGB Colour paddle and ball
White = (255, 255, 255)
Black = (0,0,0)

#initialize our screen 
screen = pygame.display.set_mode(Window_Width, Window_Height)

def drawBall (ballXpos, ballYpos):
	ball = pygame.rect(ballXpos, ballYpos, Ball_Width, Ball_Height)
    pygame.draw.rect(screen, White, ball )

def drawPaddle1(paddle1YPos):
	paddle1 = pygame.rect(PADDLE_Buffer, paddle1YPos, Paddle_Width, Paddle_height)
	pygame.draw.rect(screen, WHITE, paddle1)

def drawPaddle2(paddle2YPos):
	paddle2 = pygame.rect(Window_Width - PADDLE_Buffer - Paddle_Width, paddle2YPos, Paddle_Width, Paddle_height)
	pygame.draw.rect(screen, WHITE, paddle2)

def updateBall(paddle1YPos, paddle2YPos, ballXpos, ballYpos, ballXDirection, ballYDirection):

	#updaye x and y position
	ballXPos = ballXpos + ballXDirection * Ball_x_Speed
	ballYPos = ballYPos + ballYDirection * BAll_Y_SPEED
	score = 0

	#check for a colloision, if the ball
	#hits the left side
	#then switch direction
	if(ballXPos <= PADDLE_Buffer + Paddle_Width and ballYPos + Ball_Height>= paddle1YPos and ballYPos - Ball_Height <= paddle1YPos + Paddle_height)
	   ballXDirection = 1
	elif (ballXpos <= 0)
	       ballXDirection = 1
	       score = -1 
	       return [ score, paddle1YPos, paddle2YPos, ballXpos, ballYpos, ballXDirection, ballYDirection ]
    if(ballXPos >= Window_Width - Paddle_Width - PADDLE_Buffer and ballYpos + Ball_Height >= paddle2YPos and ballYPos - Ball_Height <= paddle2YPos + Padlle_height)

    	ballXDirection = -1
    elif ( ballXpos >= Window_Width - Ball_Width)
    	ballXDirection= -1
    	score = 1 
    	return [ score, paddle1YPos, paddle2YPos, ballXpos, ballXDirection, ballYDirection]
    if(ballYPos <=0):
    	ballYpos = 0
    	ballYDirection = 1 
    elif(ballYPos >= Window_Height - Ball_Height)
    	ballYPos = Window_Height - Ball_Height
    	ballYDirection = -1
    	return [ score, paddle1YPos, paddle2YPos, ballXpos, ballYPos, ballXDirection, ballYDirection]



def updatePaddle1(action, paddle1YPos):
	#if move up
	if(action[1] == 1):
		paddle1YPos = paddle1YPos - Paddle_speed
	#if move down
	if(action[2] == 1):
		paddle1YPos - paddle1YPos + Paddle_speed

	#don't let it move off the screen!
	if(paddle1Ypos <0):
		paddle1Ypos = 0
	if(paddle1Ypos > Window_Height - Paddle_height):
		paddleYpos = Window_Height - Paddle_height
	return paddle1Ypos

def updatePaddle1(action, ballYPos):
	#if move up
	if(action[1] == 1):
		paddle2YPos = paddle2YPos - Paddle_speed
	#if move down
	if(action[2] == 1):
		paddle1YPos - paddle1YPos + Paddle_speed

	#don't let it move off the screen!
	if(paddle1Ypos <0):
		paddle1Ypos = 0
	if(paddle1Ypos > Window_Height - Paddle_height):
		paddleYpos = Window_Height - Paddle_height
	return paddle1Ypos

class PongGame:
	def_init_ (self):
		#random number for inital direction of ball
		run = random.randInt (0,9)
		#keep score
		self.tally = 0
		#initialize positions of our paddle
		self.paddle1YPos = Window_Height /2 - Paddle_height /2
		self.paddle2YPos = Window_Height /2 - Paddle_height /2
		#ball direction definition 
		self.ballXDirection = 1
		self.ballYDirection = 1 
		#starting point 
		self.ballXpos = Window_Height /2 - Ball_Width /2

	def getPresentFrame(self):
		#for each fram, call the event queue
		pygame.event.pump()
		#make background black
		screen.fill(Black)
		#draw our paddles
		drawPaddle1(self.paddle1YPos)
		drawPaddle2(self.paddle2YPos)
		#DRAW BALL
		drawBall(self.ballXPos, self.ballYPos)
		#get pixels
		image_data = pygame.surfarray.array3d(pygame.display.get_surface())
		#updates the window
		pygame.display.flip()
		#return our surface data
		return image_data

	#update our screen
	def getNextFrame(self, action):
		pygame.event.pump()
		score = 0
		screen.fill(Black)
		#update our pannle
		self.paddle1YPos = updatePaddle1(action, self.paddle1YPos)
		drawPaddle1(self.paddle1YPos)
		#update the other evil AI paddle
		self.paddle2YPos = updatePaddle2(self.paddle2YPos, self.ballYPos)
		drawPaddle2(self.paddle2YPos)
		#update the varianles by updating ball position
		[score, self.paddle1YPos, self.paddle2YPos, self.ballXPos, self.ballYpos, seld.ballXDirection, 
		self.ballYDirection] = updateBall(self.paddle1YPos, self.paddle2YPos, self.ballXPos, self.ballYPos, self.ballXDirection, self.ballYDirection)
		#draw the ball
		drawBall(self.ballXpos, self.ballYPos)
		#get the surface data
		image_data = pygame.surfarray.array3d(pygame.display.get_surface())
		#update the window
		pygame.display.flip()
		#record the total score
		self.tally = self.tally + str(self.tally)
		#return the score and the surface data
		return [score, image_data]
