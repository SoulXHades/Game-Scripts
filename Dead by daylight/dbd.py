import keyboard
import time

def main():
	# add hotkeys to trigger what "script" to execute
	keyboard.add_hotkey("c", struggleCarry)
	keyboard.add_hotkey("h", struggleHook)

	print("Script is now running...")
	# forever blocking
	keyboard.wait()

def struggleCarry():
	struggle = True

	while struggle:
		# # sleep to reduce the spamming speed to make it realistic
		keyboard.press("a")
		time.sleep(0.05)
		keyboard.press("d")
		time.sleep(0.05)
		keyboard.release("a")
		time.sleep(0.05)
		keyboard.release("d")
		time.sleep(0.05)

		# check if user presses E to end struggle
		if keyboard.is_pressed("e"):
			struggle = False


# script to run to struggle on the hook
def struggleHook():
	struggle = True

	# struggle till user wants to stop it
	while struggle:
		keyboard.press("space")
		time.sleep(0.05)
		keyboard.release("space")
		time.sleep(0.05)

		# check if user presses E to end struggle
		if keyboard.is_pressed("e"):
			struggle = False


if __name__ == "__main__":
	main()