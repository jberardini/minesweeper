from board import Board


size = input("Please enter a board size: ")
mines = input("Please enter a number of mines: ")

game_board = Board(size, mines)
game_board.place_mines()
game_board.print_board()

cover_board = [['X' for _ in range(size)] for _ in range(size)]

for y in range(size):
	print cover_board[y]


guess = input('Please enter coordinates to guess')
y = guess[0]
x = guess[1]


while game_board[y][x] != 'M':

	cover_board[y][x] = game_board[y][x]

	for y in range(size):
		print cover_board[y]

		guess = input('Please enter coordinates to guess: ')
		y = guess[0]
		x = guess[1]



