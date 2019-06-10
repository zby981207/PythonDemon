def my_range(start, end=0, step=1):

    if step == 0:
        raise ValueError("range() step argument must not be zero")

    if not end and step > 0:
        start, end = end, start

        while start < end:
            yield start
            start += step
    if step < 0 and start > end:

        while start > end:
            yield start
            start += step

for i in my_range(10, 4, -1 ):
    print(i)
