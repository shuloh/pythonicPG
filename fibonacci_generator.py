def fib_seq(n):
    if n < 0:
        raise ValueError
    n0 = 0
    n1 = 1
    for i in range(n):
        print(n0)
        # evaluated from right to left (temp rvalue in cpp anyone?)
        n0, n1 = n1, n0 + n1 

def fib_list(n):
    result = [0,1]
    if n == 0:
        return result[0:1]
    if n == 1:
        return result
    for i in range(2,n):
        result.append(result[-1] + result[-2])
    return result


def fib_gen(n):
    n0 = 0
    n1 = 1
    for i in range(0,n):
        yield f"{n0}"
        n0, n1 = n1, n0 + n1

#sequence
fib_seq(10)
#list
print(fib_list(10))
#generator
for item in fib_gen(10):
    print(item)

    