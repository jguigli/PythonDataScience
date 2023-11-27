
def ft_filter(funct, iterable):
    """Return an iterator yielding those items of iterable
     for which function(item) is true. If function is None,
      return the items that are true."""

    if funct is None:
        newlist = [item for item in iterable if item is True]
    else:
        newlist = [item for item in iterable if funct(item) is True]
    return newlist
