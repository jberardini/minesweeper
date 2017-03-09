from board import Board
from collections import deque
from build_queue import check_cell


size = input("Please enter a board size: ")
mines = input("Please enter a number of mines: ")

game_board = Board(size, mines)
game_board.place_mines()
game_board.print_board()

cover_board = [['X' for _ in range(size)] for _ in range(size)]


guess = input('Please enter coordinates to guess: ')
y = guess[0]
x = guess[1]

non_mines_seen = 0



while True:

	if game_board[y][x] == 'M':
		print "you hit a mine"
		break

	results = check_cell(game_board, y, x, cover_board)

	new_board = results['board']
	additional_non_mines = results['count']

	non_mines_seen += additional_non_mines
	print non_mines_seen

	if non_mines_seen == (game_board.size**2 - game_board.mines):
		print "you win!"
		break


	for y in range(size):
		print new_board[y]

	guess = input('Please enter coordinates to guess: ')
	y = guess[0]
	x = guess[1]

print "Game over"



