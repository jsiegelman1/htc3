#produce a list that contains every item in list where cond(item) is True.
def filter2(list, cond):
	ret = []
	for i in iter(list):
		if cond(i):
			ret.append(i)
	return ret
	
assert filter2([1, -1, 0, 5, 2], lambda x: x > 0) == [1, 5, 2]
assert filter2(["Hello", "Hi", "Bye", "This is a string"], lambda x: len(x) > 3) == ["Hello", "This is a string"]
assert map(len, ["Hello", "Hi", "Bye", "This is a string"]) == [5, 2, 3, 16]

def sum_to(n):
	return sum(range(n))
assert sum_to(3) == (1 + 2)
assert sum_to(10) == (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)