import urllib.request
import string
from collections import defaultdict
import copy

def read_url(url):
    file = urllib.request.urlopen(url)
    data = file.read().strip()
    data = data.decode("utf8")
    data = data.split("\n")
    template = data[0]
    for line in data[2:]:
        rules = [line.split(" -> ") for line in data[2:]]
    return template, rules

template, rules = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d14-input.txt')

# Modify the template
freqs = defaultdict(int)
for i in range(len(template) - 1):
    freqs[template[i:i + 2]] += 1

elements = string.ascii_uppercase


def replace(freqs):
    new_freqs = copy.copy(freqs)
    for pair in freqs:
        for start, end in rules:
            if pair == start:
                occs = freqs[pair]
                new_freqs[pair] -= occs
                new_freqs[pair[0] + end] += occs
                new_freqs[end + pair[1]] += occs
                break

    return new_freqs


for i in range(40):
    freqs = replace(freqs)

# Count each element
count = defaultdict(int)
for pair in freqs:
    count[pair[0]] += freqs[pair]
    count[pair[1]] += freqs[pair]

count[template[0]] += 1
count[template[-1]] += 1

count_vals = [c[1] // 2 for c in count.items()]

ans = max(count_vals) - min(count_vals)
print(ans)
