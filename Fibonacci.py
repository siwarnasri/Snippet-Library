def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

for index, x in enumerate(fib()): # vertical output
    if index == 10:
        break
    print("%s" % x)
    
for index, x in enumerate(fib()): # horizontal output
    if index == 10:
        break
    print("%s" % x),
