def filter2(list, cond):
	for i in iter(list):
		if not cond(list):
			return False
	return True	
assert filter2([1, -1, 0, 5, 2], lambda x: x > 0)