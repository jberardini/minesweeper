from random import randint

class Board(object):
	def __init__(self, size, mines):
		self.size = size
		self.mines = mines
		self.board = [['.' for _ in range(self.size)] for _ in range(self.size)]

	def place_mines(self):
		seen = set()

		i = 0

		while i < self.mines:
			y = randint(0, self.size - 1)
			x = randint(0, self.size - 1)
			

			if (y, x) not in seen:
				self.board[y][x] = 'M'
				seen.add((y,x))
				i += 1

	def print_board(self):

		for y in range(self.size):
			print self.board[y]

	def __getitem__(self, i):
		return self.board[i]