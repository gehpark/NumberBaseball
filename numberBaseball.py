import random
import sys

class NumberBaseball():

	def __init__(self, sol, num_count):
		self.solution = sol
		self.num_count = num_count

	def checkGuess(self, guess):
		s = 0
		b = 0
		for i in xrange(self.num_count):
			if self.solution [i] == guess[i]:
				s += 1
			elif guess[i] in self.solution:
				b += 1
		print "Strikes: %d, Balls: %d" % (s,b)
		return s

	def run(self):
		val = self.requestValidGuess("Enter your first guess: ")
		while self.checkGuess(val) != self.num_count:
			val = self.requestValidGuess("Enter your next guess: ") 
		print "game over"

	def requestValidGuess(self, prompt):
		val = raw_input(prompt)
		while len(val) != self.num_count:
			val = raw_input("Enter guess of length %d: " % self.num_count)
		return val

def main():
	if len(sys.argv) == 2:
		num_count = int(sys.argv[1])
	else:
		num_count = 4
	sol = ''
	x = list(xrange(0, 10))
	random.shuffle(x)
	for i in x[:num_count]:
		sol += str(i)
	game = NumberBaseball(sol, num_count)
	game.run()

if __name__ == "__main__":
    main()



    