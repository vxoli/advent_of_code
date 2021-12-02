# read data file
f = open("d24-input.txt", "r")
data = f.read().split("\n")

# test data
data = ["sesenwnenenewseeswwswswwnenewsewsw", "neeenesenwnwwswnenewnwwsewnenwseswesw", "seswneswswsenwwnwse", "nwnwneseeswswnenewneswwnewseswneseene", "swweswneswnenwsewnwneneseenw", "eesenwseswswnenwswnwnwsewwnwsene", "sewnenenenesenwsewnenwwwse", "wenwwweseeeweswwwnwwe", "wsweesenenewnwwnwsenewsenwwsesesenwne", "neeswseenwwswnwswswnw", "nenwswwsewswnenenewsenwsenwnesesenew", "enewnwewneswsewnwswenweswnenwsenwsw", "sweneswneswneneenwnewenewwneswswnese", "swwesenesewenwneswnwwneseswwne", "enesenwswwswneneswsenwnewswseenwsese", "wnwnesenesenenwwnenwsewesewsesesew", "nenewswnwewswnenesenwnesewesw", "eneswnwswnwsenenwnwnwwseeswneewsenese", "neswnwewnwnwseenwseesewsenwsweewe", "wseweeenwnesenwwwswnew"]

# define centre {x,y}
centrePoint = {0,0}
# tiles will be set of {x,y, colour} co-ordinates of tiles and color (b or w)
tiles = set()

# define movements ito {x,y}
def move_e(x,y):
	x += 1
	return([x,y])

def move_se(x,y):
	x += 1
	y -= 1
	return([x,y])

def move_sw(x,y):
	x -= 1
	y -= 1
	return([x,y])
	
def move_w(x,y):
	x -= 1
	return(x,y)
	
def move_nw(x,y):
	x -= 1
	y += 1
	return([x,y])
	
def move_ne(x,y):
	x += 1
	y += 1
	return([x,y])

	# read each line of the data
for line in data[0:1]:
	print(len(line), line)
	# split line into movements
	charCount = 0
	movements = []
	while charCount < len(line):
		# split string by movement codes 'e', 'se', 'sw', 'w', 'nw', 'ne'
		# if movements starts with s or n will be two character code
		if line[charCount] in {'s', 'n'}:
			movements.append(line[charCount:charCount+2])
			charCount += 2
		else:
			# if line[charCount] in {'e', 'w'}:
			movements.append(line[charCount])
			charCount += 1
	#starting at [0,0] apply moves and determine end co-ordinate
	location = [0,0]
	for move in movements:
		if move == 'e':
			location = move_e(location[0],location[1])
		if move == 'w':
			location = move_w(location[0],location[1])
		if move == 'se':
			location = move_se(location[0],location[1])
		if move == 'sw':
			location = move_sw(location[0],location[1])
		if move == 'ne':
			location = move_ne(location[0],location[1])
		if move == 'nw':
			location = move_nw(location[0],location[1])
			
		# store location and flip the tile
		location.append("b")
		print(location)
		tiles.update(location)
		print(tiles)
		#check if entry in set of tiles and locations
		#if set(location) in tiles:
			# if in set of tiles then flip the colour of the tile
		#	print("in tiles")
		#else:
			# add to set of tiles and flip colour from white to black
		#	tiles.add([location[0],location[1],"W"])