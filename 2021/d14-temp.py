import urllib.request

file = urllib.request.urlopen('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d14-input.txt')
data = file.read().strip()
data = data.decode("utf8")
lines = data.split("\n")


s = lines[0]
print(s)

k = {}

for q in lines[2:]:
    x, y = q.split(" -> ")
    k[x] = y

for _ in range(3):
    n = s[0]
    for c in s[1:]:
        n += k[n[-1] + c]
        n += c
    s = n
    print(s)
    print(len(s))
c = {}

for char in s:
    if char not in c: c[char] = 0
    c[char] += 1

print(max(c.values()) - min(c.values()))
