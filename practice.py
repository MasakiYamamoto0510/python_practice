w = ['mon', 'tue', 'wed']
f = ['coffe', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)

s = set()
for i in range(10):
    s.add(i)

print(s)

s = {i for i in range(10)}
print(s)

def g():
    for i in range(10):
        yield i

g = g()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

g = (i for i in range(10))

print(next(g))
print(next(g))
print(next(g))
print(next(g))