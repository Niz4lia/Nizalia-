
mydict = {
	1: "we'll see",
	2: 'ok',
	3: 'hi',
	4: 'tschuss',
	5: 'bonjour',
	6: 'hello',
	7: 'holla',
}
mydict1=mydict.copy()
print(mydict)
print("shallow copy", mydict1)
mydict={}
print("after clearing", mydict, mydict1)