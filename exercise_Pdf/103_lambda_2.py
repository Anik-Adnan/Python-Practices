# They can also take arbitrary number of arguments / keyword arguments, like normal functions.
greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
greeting('hello', 'world', world='world')
# prints:
# hello ('world',) {'world': 'world'}
