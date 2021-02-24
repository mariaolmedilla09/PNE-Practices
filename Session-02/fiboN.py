def fibon(n):
    x = 0
    y = 1
    fibonacci_list = [x, y]
    for i in range(0, n-1):
        fn = x + y
        fibonacci_list.append(fn)
        x = y
        y = fn
    return fibonacci_list[-1]   # Not necessary to return the last element of the list, because in this case the list isn't necessary as we do not need to return several numbers.
    # return fn (that's enough)

print("5th Fibonacci term: ", fibon(5))
print("5th Fibonacci term: ", fibon(10))
print("5th Fibonacci term: ", fibon(15))