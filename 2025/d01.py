def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def read_data(filename):
	with open(filename) as file:
		lines = list(map(str, file.readlines()))
	file.close()

	return lines

def count_zero_hits(start, distance, direction):
    """Count how many clicks land on 0 during a single rotation."""
    if direction == 'L':
        first_hit = start % 100  # steps until first wrap to 0
        end_pos = (start - distance) % 100
    else:
        first_hit = (100 - start) % 100  # steps until first wrap to 0
        end_pos = (start + distance) % 100

    # If already at 0, first wrap is after 100 clicks.
    if first_hit == 0:
        first_hit = 100

    if distance < first_hit:
        hits = 0
    else:
        hits = 1 + (distance - first_hit) // 100

    return hits, end_pos

if __name__ == "__main__":
    input_data = read_data(r'C:\Users\chris\OneDrive\Documents\GitHub\advent_of_code\2025\d01_input.txt')
    dial = 50
    password_end = 0
    password_clicks = 0
    for raw in input_data:
        line = raw.strip()
        if not line:
            continue
        direction, distance = line[0], int(line[1:])
        if direction == 'L':
            dial = (dial - distance) % 100
        else:
            dial = (dial + distance) % 100
        if dial == 0:
            password_end += 1

    # Re-run for method 0x434C49434B (count clicks landing on 0).
    dial = 50
    for raw in input_data:
        line = raw.strip()
        if not line:
            continue
        direction, distance = line[0], int(line[1:])
        hits, dial = count_zero_hits(dial, distance, direction)
        password_clicks += hits

    print("Part 1: ", password_end)
    print("Part 2: ",password_clicks)
