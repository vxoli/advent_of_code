from collections import defaultdict
from dataclasses import dataclass
from functools import cache

with open('d24-input.txt', 'r') as f:
	data = f.readlines()


@dataclass(frozen=True)
class Tile:
	x: int
	y: int
	z: int

	@cache
	def neighbours(self):
		out = set()
		for direction in directions.values():
			out.add(Tile(
				self.x + direction[0],
				self.y + direction[1],
				self.z + direction[2]
			))
		return out


directions = {
	'e': [1, 0, -1],
	'ne': [0, 1, -1],
	'nw': [-1, 1, 0],
	'w': [-1, 0, 1],
	'sw': [0, -1, 1],
	'se': [1, -1, 0]
	}

floor = defaultdict(bool)
for line in data:
	x, y, z = 0, 0, 0
	line = list(line.strip())
	while line:
		fc = line.pop(0)
		if fc in ['e', 'w']:
			attr = fc
		else:
			attr = fc + line.pop(0)
		x1, y1, z1 = directions[attr]
		x += x1
		y += y1
		z += z1
	target_tile = Tile(x, y, z)
	if target_tile in floor:
		floor[target_tile] = not floor[target_tile]
	else:
		floor[target_tile] = True
print('Part 1:', sum(floor.values()))

for day in range(100):
	tiles_to_search = set()
	tiles_searched = set()
	tiles_to_search.update(floor)
	tiles_to_flip = []
	while tiles_to_search:
		current_tile = tiles_to_search.pop()
		tiles_searched.add(current_tile)
		neighbours = current_tile.neighbours()
		adj_val = sum([floor.get(n, 0) for n in neighbours])
		if floor[current_tile]:
			tiles_to_search.update([n for n in neighbours if n not in tiles_searched])
			if adj_val == 0 or adj_val > 2:
				tiles_to_flip.append(current_tile)
		else:
			if adj_val == 2:
				tiles_to_flip.append(current_tile)
	for tile in tiles_to_flip:
		floor[tile] = not floor[tile]
		print('Part 2:', sum(floor.values()))