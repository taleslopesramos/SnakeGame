#!/usr/bin/env python

# Snake Game!

# modules
import pygame, sys, random, time
from snake import *
from colors import *
from actions import *
from food import *
from globs import *

# main function
def main():
	# init pygame
	init_game()

	# get globals
	glob = globs()

	# Colors Object
	colorsObj = colors()

	# Food Object
	foodObj = food()

	# SNAKE Object
	snakeObj = snake()

	# Play surface
	playSurface = pygame.display.set_mode(glob.size)

	pygame.display.set_caption('Snake Game!')
	# game_over(playSurface,colorsObj.red)
		
	# FPS controller
	fpsController = pygame.time.Clock()
	
	# Game Loop
	while True:
		# Event checking
		moved = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT: #EXIT EVENT 
				sys.exit()

			elif event.type == pygame.KEYDOWN: #KEYBOARD INPUT EVENT
				action, actionType = getKeyAction(event.key) ##

				if actionType == ActionType.MOVE_ACTION and not moved: # Handle Move Actions
					moved = snakeObj.handleMoveAction(action)
					 
				elif actionType == ActionType.MENU_ACTION: # Handle Menu Actions
					handleMenuAction(action)

		playSurface.fill(colorsObj.white)
		foodObj.render(playSurface)
		snakeObj.render(foodObj,playSurface)
		pygame.display.flip()
		fpsController.tick(20)
		
		if(snakeObj.isDead()):
			game_over(playSurface,colorsObj.red)
			pygame.display.flip()
			time.sleep(4)
			sys.exit(-1)


def init_game():
	#init pygame
	check_errors = pygame.init()
	
	if check_errors[1] > 0:
		print('(!) Had {0} initializing errors, exiting..'.format(check_errors[1]))
		sys.exit(-1)
	else:
		print('(+) PyGame successfully initialized!')

def game_over(playSurface,fontColor):
	GOfont = pygame.font.SysFont('Lora', 72)
	GOsurf = GOfont.render('Game Over!', True, fontColor)
	GOrect = GOsurf.get_rect() 
	GOrect.midtop = (globs().width/2, 15)

	playSurface.blit(GOsurf, GOrect)
	

def getKeyAction(key):
	"""
	Define the action of the pressed key 
	"""
	action = 0
	action_type = 0

	if key == pygame.K_RIGHT or key == ord('d'):
		action = Action.MOVE_RIGHT
		action_type = ActionType.MOVE_ACTION

	elif key == pygame.K_LEFT or key == ord('a'):
		action = Action.MOVE_LEFT
		action_type = ActionType.MOVE_ACTION

	elif key == pygame.K_UP or key == ord('w'):
		action = Action.MOVE_UP
		action_type = ActionType.MOVE_ACTION

	elif key == pygame.K_DOWN or key == ord('s'):
		action = Action.MOVE_DOWN
		action_type = ActionType.MOVE_ACTION

	elif key == pygame.K_ESCAPE:
		action = Action.EXIT
		action_type = ActionType.MENU_ACTION

	else:
		action = Action.DEFAULT
		action_type = ActionType.DEFAULT
	
	return action, action_type 


def handleMenuAction(action):
	"""
	Release a menu action that is fired by the user
	@param action = INT FROM THE 'Action' ENUM CLASS 
	"""
	if action == Action.EXIT:
		sys.exit()		
	elif action == Action.DEFAULT:
		pass
# RUN MAIN FUNCTION
main()