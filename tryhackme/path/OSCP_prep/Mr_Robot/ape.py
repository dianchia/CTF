#!/usr/bin/python3

with open('fsocity.dic') as handler:
	data = handler.read().split('\n')

print(len(data))
data = list(set(data))

with open('fsocity_sorted.dic', 'w+') as handler:
	for d in data:
		handler.write(d + '\n')