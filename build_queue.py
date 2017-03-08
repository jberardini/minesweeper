from collections import deque


# def check_directions(game_board, y, x):


# 	if y < game_board.size - 1:
# 		if y + 1 == "M":
# 			mine_count += 1

# 	if x > 0:
# 		if x - 1 == "M":
# 			mine_count += 1

# 	if x < game_board.size - 1:
# 		if x + 1 == "M":
# 			mine_count += 1


# check the 4 directions
# if none are equal to a mine, add to queue
# otherwise, display number
# also need to check if uncovered

def check_cell(game_board, y, x, cover_board):
	to_visit = deque()
	seen = set()


	to_visit.append((y,x))
	
	while to_visit:
		y, x = to_visit.popleft()
		mine_count = 0
		neighbors = deque()

		if y < game_board.size - 1:
			if game_board[y + 1][x] == "M":
				mine_count += 1

			elif (y+1, x) not in seen:
				neighbors.append((y+1,x))
				seen.add((y+1, x))

		if x > 0:
			if game_board[y][x-1] == "M":
				mine_count += 1

			elif (y, x-1) not in seen:
				neighbors.append((y,x-1))
				seen.add((y, x-1))


		if x < game_board.size - 1:
			if game_board[y][x+1] == "M":
				mine_count += 1

			elif (y, x+1) not in seen:
				neighbors.append((y,x+1))
				seen.add((y, x+1))



		if mine_count == 0:
			cover_board[y][x] = game_board[y][x]
			to_visit.extend(neighbors)

		else:
			cover_board[y][x] = mine_count


		print to_visit



	return cover_board





