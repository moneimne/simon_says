import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM) # set board mode to Broadcom
li = []
gamestate = 1
score = 0

GPIO.setup(4, GPIO.OUT) # set up pin 4 yellow light
GPIO.setup(27, GPIO.OUT) # set up pin 27 white light
GPIO.setup(5, GPIO.OUT) # set up pin 5 green light
GPIO.setup(13, GPIO.OUT) # set up pin 13 red light

GPIO.setup(17, GPIO.IN) # set up pin 18 yellow button
GPIO.setup(22, GPIO.IN) # set up pin 22 white button
GPIO.setup(6, GPIO.IN) # set up pin 6 green button
GPIO.setup(19, GPIO.IN) # set up pin 19 red button

def flash():
	GPIO.output(13, 1)
	GPIO.output(27, 1)
	GPIO.output(5, 1)
	GPIO.output(4, 1)
	time.sleep(.25)
	GPIO.output(13, 0)
	GPIO.output(27, 0)
	GPIO.output(5, 0)
	GPIO.output(4, 0)
	time.sleep(.25)
	

def restart():
	GPIO.output(13,1)
	time.sleep(.25)
	GPIO.output(13, 0)
	GPIO.output(27, 1)
	time.sleep(.25)
	GPIO.output(27, 0)
	GPIO.output(5, 1)
	time.sleep(.25)
	GPIO.output(5, 0)
	GPIO.output(4, 1)
	time.sleep(.25)
	GPIO.output(4, 0)
	flash()
	flash()
	flash()

restart()
while gamestate == 1:
	time.sleep(2)
	newcolor = random.randint(0, 3)
	li.append(newcolor)
	print "playing...\n"

	for x in li:
		time.sleep(.5)
		if x == 0:
			#red
			GPIO.output(13, 1) # turn on 13 red light
			time.sleep(.75)
			GPIO.output(13, 0) #turn off red warning	
		if x == 1:
			#green
			GPIO.output(5, 1) # turn on 5 green light warning
			time.sleep(.75)
			GPIO.output(5, 0) # turn off green warning	
		if x == 2:
			#white
			GPIO.output(27, 1) # turn on 27 white light
			time.sleep(.75)
			GPIO.output(27, 0) # turn off white warning
		if x == 3: 
			#yellow
			GPIO.output(4, 1) # turn on 4 yellow light
			time.sleep(.75)
			GPIO.output(4, 0) # turn off yellow warning
	print "waiting...\n"
	for x in li:
		pressed = ""
		while True:
			if GPIO.input(19):
				pressed = "red"
				GPIO.output(13, 1)
				time.sleep(1)
				GPIO.output(13, 0)
				break
			if GPIO.input(6):
				pressed = "green"
				GPIO.output(5, 1)
				time.sleep(1)
				GPIO.output(5, 0)
				break
			if GPIO.input(22):
				pressed = "white"
				GPIO.output(27, 1)
				time.sleep(1)
				GPIO.output(27, 0)
				break
			if GPIO.input(17):
				pressed = "yellow"
				GPIO.output(4, 1)
				time.sleep(1)
				GPIO.output(4, 0)
				break
			# wait for user to press button for curr instr
		if (pressed != "red" and x == 0):
			#game over didnt choose red
			gamestate = 0
			print "You lose! You didn't hit red. Your score is %s \n" % (score)
			restart()
			break
		if (pressed != "green" and x == 1):
			#game over didnt choose green
			gamestate = 0
			print "You lose! You didn't hit green. Your score is %s \n" % (score)
			restart()
			break
		if (pressed != "white" and x == 2):
			#game over didnt choose white
			gamestate = 0
			print "You lose! You didn't hit white. Your score is %s \n" % (score)
			restart()
			break
		if (pressed != "yellow" and x == 3):
			#game over didnt choose yellow	
			gamestate = 0
			print "You lose! You didn't hit yellow. Your score is %s \n" % (score)
			restart()
			break

		score = score + 1
