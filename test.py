def f():
	global s
	print s
	s = "that's clear"
	print s

s = "Hello!"
f()
print s

tup = (1,2)
print float(tup[0])/tup[1]
print int(6.9)