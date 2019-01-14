import pygame
from point import *
import random
from colors import *
from globs import *

class food:
	"""
	Food entity
	"""
	def __init__(self):
		self.foodSpawn = True

		self.pos = point(random.randrange(1,globs().width//10)*10,random.randrange(1,globs().height//10)*10)	
		
	def render(self,surface):
		if not self.foodSpawn:
			self.pos = point(random.randrange(1,globs().width//10)*10,random.randrange(1,globs().height//10)*10)	
			self.foodSpawn = True
		self.draw(surface)

	def draw(self,surface):
		pygame.draw.rect(surface,colors().brown,pygame.Rect(self.pos.x,self.pos.y,10,10))
		pass