import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # set board mode to Broadcom
li[0]
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

while gamestate == 1:
	time.sleep(2)
	newcolor = random.randint(0, 3)
	li.append(newcolor)
	
	for x in li:
		if x == 0:
			#red
			GPIO.output(13, 1) # turn on 13 red light
			time.sleep(1)
			GPIO.output(13, 0) #turn off red warning	
		if x == 1:
			#green
			GPIO.output(5, 1) # turn on 5 green light warning
			time.sleep(1)
			GPIO.output(5, 0) # turn off green warning	
		if x == 2:
			#white
			GPIO.output(27, 1) # turn on 27 white light
			time.sleep(1)
			GPIO.output(27, 0) # turn off white warning
		if x == 3: 
			#yellow
			GPIO.output(4, 1) # turn on 4 yellow light
			time.sleep(1)
			GPIO.output(4, 0) # turn off yellow warning

	for x in li:
		while !GPIO.input(17) || !GPIO.input(22) || !GPIO.input(6) || !GPIO.input(19):
			# wait for user to press button for curr instr
		if GPIO.input(19) && x != 0
			//game over didnt choose red
			gamestate = 0
			printf "You lose! You didn't hit red. Your score is %s" %score
			exit(-1)
		if GPIO.input(6) && x != 1
			//game over didnt choose green
			gamestate = 0
			printf "You lose! You didn't hit green. Your score is %s" %score
			exit(-1)
		if GPIO.input(22) && x != 2
			//game over didnt choose white
			gamestate = 0
			printf "You lose! You didn't hit white. Your score is %s" %score
			exit(-1)
		if GPIO.input(17) && x != 3
			//game over didnt choose yellow	
			gamestate = 0
			printf "You lose! You didn't hit yellow. Your score is %s" %score
			exit(-1)

		score = score + 1
