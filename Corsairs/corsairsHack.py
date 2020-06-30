from selenium import webdriver
import argparse
import sys
import time
import unittest

class CorsairsHack(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(10)
		self.driver.get(args.URL)

		self.score = 0

	def tearDown(self):
		self.driver.close()

	# main powerlevel function
	def test_StartHack(self):
		# give the page time to load
		time.sleep(3)
		# need user to click on the screen (equivant to start()) for the game to get ready
		self.driver.execute_script("start()")

		# power level till user requested level
		for i in range(int(args.level) - 1):
			# start() equivant to click the play button before each round
			self.driver.execute_script("start()")
			# incrementing the score for the level which it will +10 to the current score (see the JS source code)
			self.driver.execute_script("nextLevel()")
			# give the page time to load the next level
			time.sleep(1)
			# auto set the score because each round is 28 score. nextLevel() will +10 to score.
			# however, due to delay between executing start() and nextLevel(),
			# the boat would have moved and obtained some score for that stage.
			# Therefore, we set the score by ourselves.
			# The score will not reflect on the page till start() is called because the UI is not updated yet.
			self.score += 38
			self.driver.execute_script("window.score = " + str(self.score))

		# start the latest round and die so that the server won't be suspicious that higher score at the level is without
		# at least scoring a bit before getting hit by the bullet.
		self.driver.execute_script("start()")
		time.sleep(1)
		self.driver.execute_script("window.bang = true")
		# end the game as if it died so let the die() set all the needed variables for us and send the score.
		# Can choose to do it manually too.
		self.driver.execute_script("die()")

		# for user to see the level he/she has reached
		time.sleep(3)


# console print to display usage of the script
def printHelp():
	print('Usage: python corsairsHack.py <level to reach> "<URL that is linked to your corsairs account>"')
	print('Example: python corsairsHack.py 11 "https://tbot.xyz/corsairs/#YourID"')


if __name__ == "__main__":
	# check if user requesting for help
	if len(sys.argv) != 3:
		printHelp()
		exit(1)

	# argument parser for unittest
	parser = argparse.ArgumentParser()
	parser.add_argument('level')
	parser.add_argument('URL')
	parser.add_argument('unittest_args', nargs='*')

	args = parser.parse_args()

	sys.argv[1:] = args.unittest_args

	unittest.main()
    