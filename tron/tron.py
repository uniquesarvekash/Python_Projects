# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games
NOTE: THIS IS A STUDENT PROJECT - SHARED WITH PERMISSION

# Import SPGL
import spgl
import time
import turtle

# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 5
		self.direction = "up"
		self.score = 0
		self.lives = 3
		self.shapesize(0.5, 0.5, 0)
		self.wall = []
		
	def tick(self):
	
		self.stamp()
		self.wall.append((self.xcor(),self.ycor()))
	
		if self.direction == "right":
			self.goto(self.xcor() + self.speed, self.ycor())
			
		if self.direction == "left":
			self.goto(self.xcor() - self.speed, self.ycor())
			
		if self.direction == "up":
			self.goto(self.xcor(), self.ycor() + self.speed)
			
		if self.direction == "down":
			self.goto(self.xcor() , self.ycor()- self.speed)
				
			
	
	def turn_left(self):
		game.play_sound("turn.wav")
		if self.direction != "right":
			self.direction = "left"
			
			
		
	def turn_right(self):
		game.play_sound("turn.wav")
		if self.direction != "left":
			self.direction = "right"
		
		
	def turn_up(self):
		game.play_sound("turn.wav")
		if self.direction != "down":
			self.direction = "up"
		
	def turn_down(self):
		game.play_sound("turn.wav")
		if self.direction != "up":
			self.direction = "down"
		
		
# Create Functions

def end_game():
	game.exit()
	
#Draw border


# Initial Game setup
game = spgl.Game(800, 600, "black", "TRON",0)

# Create Sprites
player = Player ("square", "blue", 100, 0)
player2 = Player ("square", "red", -100, 0)
# Create Labels
lbl_player_score = spgl.Label("Player 1: 0", "white", 320, 280)
lbl_player2_score = spgl.Label("Player 2: 0", "white", -380, 280)

# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_LEFT, player.turn_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.turn_right)
game.set_keyboard_binding(spgl.KEY_UP, player.turn_up)
game.set_keyboard_binding(spgl.KEY_DOWN, player.turn_down)

game.set_keyboard_binding("a", player2.turn_left)
game.set_keyboard_binding("d", player2.turn_right)
game.set_keyboard_binding("w", player2.turn_up)
game.set_keyboard_binding("s", player2.turn_down)
game.set_keyboard_binding("q", end_game)

game.update_screen()
game.play_sound("start.wav")
time.sleep(16)
game.play_sound("background.mp3")

while True:
	# Call the game tick method
	game.tick()
	
	
    
    #check for collision with the walls
    
	#check for collision for player 1
	#blue touches red
	if (player.xcor(), player.ycor()) in player2.wall:
		print ("blue dies")
		player.clear()
		player2.clear()
		player.wall = []
		player2.wall = []
		player.goto(100, 0)
		player2.goto(-100, 0)
		player2.score += 1
		lbl_player2_score.update("Player 2: {}".format(player2.score))
		player2.direction = "up"
		player.direction = "up"
		game.update_screen()
		time.sleep(2)
		
	#red touches blue	
	if (player2.xcor(), player2.ycor()) in player.wall:
		print ("red dies")
		player.clear()
		player2.clear()
		player.wall = []
		player2.wall = []
		player2.goto(-100,0)
		player.goto(100,0)
		player.score += 1
		lbl_player_score.update("Player 1: {}".format(player.score))
		player2.direction = "up"
		player.direction = "up"
		game.update_screen()
		time.sleep(2)

	# blue touches blue	
	if (player.xcor(), player.ycor()) in player.wall:
		print ("blue dies")
		player.clear()
		player2.clear()
		player.wall = []
		player2.wall = []
		player.goto(100, 0)
		player2.goto(-100, 0)
		player2.score += 1
		lbl_player2_score.update("Player 2: {}".format(player2.score))
		player2.direction = "up"
		player.direction = "up"
		game.update_screen()
		time.sleep(2)
		
	# red touches red
	if (player2.xcor(), player2.ycor()) in player2.wall:
		print ("red dies")
		player.clear()
		player2.clear()
		player.wall = []
		player2.wall = []
		player2.goto(-100, 0)
		player.goto(100, 0)
		player.score += 1
		lbl_player_score.update("Player 1: {}".format(player.score))
		player2.direction = "up"
		player.direction = "up"
		game.update_screen()
		time.sleep(2)
    
