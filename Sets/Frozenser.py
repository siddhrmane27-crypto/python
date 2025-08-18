cricketers = frozenset([45,18,7,33])
print(cricketers)
print(type(cricketers))

c2=set(cricketers)

print(c2)
print(type(c2))

c2.add(93)
print(c2)

cricketers=frozenset(c2)

print(cricketers)