
def ft_filter(funct, iterable):
	"""Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true."""
	if funct == None:
		newlist = [item for item in iterable if item == True]
	else:
		newlist = [item for item in iterable if func(item) == True]
	return newlist