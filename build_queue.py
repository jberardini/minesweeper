from collections import deque

def check_cell(game_board, y, x, cover_board):
	to_visit = deque()
	seen = set()

	count = 0
	to_visit.append((y,x))
	
	while to_visit:
		y, x = to_visit.popleft()
		mine_count = 0
		neighbors = deque()

		for j in range(y-1, y+2):
			for i in range(x-1, x+2):

				if is_valid_direction(game_board, j, i):
					if game_board[j][i] == 'M':
						mine_count += 1

					elif (j, i) not in seen:
						neighbors.append((j,i))
						seen.add((j,i))

		if mine_count == 0:
			cover_board[y][x] = game_board[y][x]
			to_visit.extend(neighbors)

		else:
			cover_board[y][x] = mine_count


		print to_visit
		count += 1

	results = {'board': cover_board, 'count': count}

	return results

def is_valid_direction(game_board, y, x):

	try:
		game_board[y][x] 
		return True

	except IndexError:
		return False





	




