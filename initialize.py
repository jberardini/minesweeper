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

non_mine_count = 0

keep_going = True



while keep_going:

	if game_board[y][x] == 'M':
		break

	non_mine_count += 1

	if non_mine_count == game_board.mines:
		break

	new_board = check_cell(game_board, y, x, cover_board)

	for y in range(size):
		print new_board[y]

	guess = input('Please enter coordinates to guess: ')
	y = guess[0]
	x = guess[1]

print "Game over"



