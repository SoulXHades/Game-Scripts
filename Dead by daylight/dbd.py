import keyboard
import time

def main():
	# add hotkeys to trigger what "script" to execute
	keyboard.add_hotkey("=", runStraight)
	keyboard.add_hotkey("c", struggleCarry)
	keyboard.add_hotkey("h", struggleHook)
	# forever blocking
	keyboard.wait()

def runStraight():
	run = True

	while run:
		# sleep to reduce the spamming speed to make it realistic
		time.sleep(0.045)
		# press the A button
		keyboard.send("left shift+w")

		# check if user presses E to end running
		if keyboard.is_pressed("e"):
			run = False

def struggleCarry():
	struggle = True

	while struggle:
		# sleep to reduce the spamming speed to make it realistic
		time.sleep(0.1)
		# press the A button
		keyboard.send("a")
		# sleep to reduce the spamming speed to make it realistic
		time.sleep(0.1)
		# press the D button
		keyboard.send("d")

		# check if user presses E to end struggle
		if keyboard.is_pressed("e"):
			struggle = False


# script to run to struggle on the hook
def struggleHook():
	struggle = True

	# struggle till user wants to stop it
	while struggle:
		# sleep to reduce the spamming speed to make it realistic
		time.sleep(0.16)
		# press the SPACE button
		keyboard.send("space")

		# check if user presses E to end struggle
		if keyboard.is_pressed("e"):
			struggle = False


main()