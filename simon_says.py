import RPi.GPIO as GPIO

li[0]
gamestate = 1
score = 0

while gamestate == 1:
	sleep 2
	newcolor = random.randint(0, 3)
	li.append(newcolor);
	
	for x in li:
		if x == 0:
			#turn on red
		if x == 1:
			#turn on green
		if x == 2:
			#turn on white
		if x == 3: 
			#turn on yellow
		sleep 1

	for x in li:
		#get input
		if x != #input:
			gamestate = 0
			printf("You lose! Your score is ", score)
			exit -1;

	score = score + 1

GPIO.setmode(GPIO.BCM) # set board mode to Broadcom

GPIO.setup(4, GPIO.OUT) # set up pin 17 yellow light
GPIO.setup(27, GPIO.OUT) # set up pin 22 white light
GPIO.setup(5, GPIO.OUT) # set up pin 5 green light
GPIO.setup(13, GPIO.OUT) # set up pin 13 red light

GPIO.setup(17, GPIO.IN) # set up pin 18 yellow button
GPIO.setup(22, GPIO.OUT) # set up pin 23 white button
GPIO.setup(6, GPIO.OUT) # set up pin 25 green button
GPIO.setup(19, GPIO.OUT) # set up pin 12 red button

if (GPIO.output
GPIO.output(4, 1) # turn on light 17
GPIO.output(27, 1) # turn on white light 22
GPIO.output(5, 1) # turn on green light 5
GPIO.output(13, 1) # turn on red light 13

GPIO.output(18, 1) # turn on  18
GPIO.output(23, 1) # turn on pin 17
GPIO.output(25, 1) # turn on pin 17 
GPIO.output(12, 1) # turn on pin 12 button
