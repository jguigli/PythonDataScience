def callLimit(limit: int):
    """Returns a decorator that limits the number
     of times a function can be called."""
    count = 0

    def callLimiter(function):
        """Decorator function that limits the number
         of calls to the wrapped function."""

        def limit_function(*args: any, **kwargs: any):
            """Wrapped function that enforces the call limit."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")

        return limit_function
    return callLimiter
