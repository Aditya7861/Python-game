import pygame
import time
import random

pygame.init()

game_width=800
game_height=600

black=(0,0,0)
white=(255,255,255)
red=(250,250,250)

car_width=100

gameDisplay=pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption('Thunder Racing')
clock=pygame.time.Clock()
carImg=pygame.image.load('car.png')

def things_passed(count):
	font = pygame.font.SysFont(None,20)
	text=font.render("Passed"+str(count),True,black)
	gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])


def text_object(text,font):
	TextSurf = font.render(text,True ,black)
	return TextSurf ,TextSurf.get_rect()

def display_message(text):
	largeText=pygame.font.Font('freesansbold.ttf',60)
	TextSurf,TextRect =text_object(text,largeText)
	TextRect.center = ((game_width/2),(game_height/2))
	gameDisplay.blit(TextSurf,TextRect)

	pygame.display.update()

	time.sleep(2)

	game_loop()

def crash():
	display_message('You are Crashed')


def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def  game_loop():
	x = (game_width*.3)
	y = (game_height*0.1)


	x_chage=0
	count=0

	game_exit=False


	thing_starty=game_height+200
	thing_startx=random.randrange(0,game_width)
	thing_speed =5
	thing_width=100
	thing_height=50

	while not game_exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_chage=-5
				elif event.key == pygame.K_RIGHT:
					x_chage = 5

			if event.type ==pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_chage=0

		#	print(event)
		x+=x_chage

		gameDisplay.fill(white)
		car(x,y)

		#things(thingx,thingy,thingw,thingh,color):
		things(thing_startx,thing_starty,thing_width,thing_height,black)
		thing_starty -= thing_speed
		things_passed(count)

		if thing_starty < 0:
			thing_starty=game_height + thing_height
			thing_startx=random.randrange(0,game_width)
			count += 1
			thing_speed +=1

		#	print(thing_startx,thing_starty)


		if x>game_width - car_width or x < 0:
			#game_exit=True
			crash()

		if thing_startx == x and thing_starty == y:
			crash()

		#print(thing_starty,x)
		if y >  thing_starty :
			print('step 1')

			if thing_startx < x and x < thing_startx + thing_width:
				crash()
		
	#	print(thing_startx,thing_starty,x,y)
		pygame.display.update()

		clock.tick(60)

game_loop()
pygame.quit()
quit()

