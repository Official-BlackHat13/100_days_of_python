def add(*args):
    sum_of_args = 0
    for n in args:
        sum_of_args += n
    return sum_of_args


print(add(2, 4, 6))
