import pygame
from point import *
from actions import *
from colors import *
from globs import *

class snake:
	"""
	Snake entity class
	"""
	def __init__(self, posX=100, posY=50):
		self.head = point(100,50)
		self.body = [point(100,50),point(90,50),point(80,50)]
		self.action = Action.MOVE_RIGHT 

	def render(self,food,surface):
		self.draw(surface)
		self.move(food)
		

	def draw(self,surface):
		for pos in self.body:
			pygame.draw.rect(surface, colors().green, pygame.Rect(pos.x,pos.y,10,10))


	def handleMoveAction(self,action):
		"""
		Handle a move action that is fired by the user
		@param action = INT FROM THE 'Action' ENUM CLASS 
		"""
		if self.action == action:
			return False
		elif action == Action.MOVE_RIGHT and self.action != Action.MOVE_LEFT:
			self.action = Action.MOVE_RIGHT
			return True
		elif action == Action.MOVE_LEFT and self.action != Action.MOVE_RIGHT:
			self.action = Action.MOVE_LEFT
			return True
		elif action == Action.MOVE_UP and self.action != Action.MOVE_DOWN:
			self.action = Action.MOVE_UP
			return True
		elif action == Action.MOVE_DOWN and self.action != Action.MOVE_UP:
			self.action = Action.MOVE_DOWN
			return True


	def move(self,food):

		if self.action == Action.MOVE_RIGHT:
			self.head.x += 10
		elif self.action == Action.MOVE_LEFT:
			self.head.x -= 10
		elif self.action == Action.MOVE_UP:
			self.head.y -= 10
		elif self.action == Action.MOVE_DOWN:
			self.head.y += 10

		x = self.head.x
		y = self.head.y

		self.body.insert(0,point(x,y))

		if(self.head.x == food.pos.x and self.head.y == food.pos.y):
			food.foodSpawn = False
		else:
			self.body.pop()
			
	def isDead(self):
		dead = False
		glob = globs()
		width = glob.width
		height = glob.height

		if self.head.x >= width or self.head.x < 0 or self.head.y >= height or self.head.y < 0:
			dead = True
		else:
			for part in self.body[1:]:
				if(part.x == self.head.x and part.y == self.head.y):
					dead = True
					break

		return dead