def my_range(from_, to=None, step=1):
    if step < 0:
        from_, to = to, from_
        while from_ < to:
            yield to
            to += step
    if to is None:
        to = from_
        from_ = 0
        while from_ < to:
            yield from_
            from_ += step
    elif to is not None:
        while from_ < to:
            yield from_
            from_ += step



print(list(range(10)) == list(my_range(10)))
print(list(range(10, 20)) == list(my_range(10, 20)))
print(list(range(20, 10, -1)) == list(my_range(20, 10, -1)))
print(list(range(20, 10)) == list(my_range(20, 10)))
print(list(range(10, 20, -1)) == list(my_range(10, 20, -1)))
print(list(range(10, 0, -3)) == list(my_range(10, 0, -3)))
