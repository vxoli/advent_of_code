from collections import defaultdict, deque

turns = [0,5,4,1,10,14,7]  # My input
spoken_at = defaultdict(deque)
for i, x in enumerate(turns):
    spoken_at[x].append(i + 1)

last_number = turns[-1]
turn = len(turns)

# This is more complicated than it has to be, but it felt
# a bit dirty saving absolutely every turn for 30 million iterations.
# This just keep tracks of the last two times we saw a number
while turn < 2020: # int(3e7) for part 2  # Set to 2020 for part 1
    turn += 1
    if len(spoken_at[last_number]) == 1:  # The last number made it's first appearance
        last_number = 0
        spoken_at[0].append(turn)
        if len(spoken_at[0]) > 2:
            spoken_at[0].popleft()
    else:
        new_number = spoken_at[last_number][1] - spoken_at[last_number][0]
        spoken_at[last_number].popleft()
        last_number = new_number
        spoken_at[new_number].append(turn)
        if len(spoken_at[new_number]) > 2:
            spoken_at[new_number].popleft()

print(last_number)
