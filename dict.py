# -*- coding: utf-8 -*-
d = {
	"Adam":95,
	"Tom":99,
	"Poke":91
}

print d;

print d["Adam"]

if "Poker" in d:
	print d["Poker"]


if "Tom" in d:
	print d["Tom"]




print d.get("Tom")
print d.get("tom")

s = set(['A','b','c'])

print s

s1 = set (['A','b','b','c'])

print s1

print 'b'  in s1

s1.add("d")

if "A" in s1:
	s1.remove("A")

print s1