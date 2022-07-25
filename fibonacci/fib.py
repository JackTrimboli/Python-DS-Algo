# ITERATIVE BRUTE:


def fib(n: int):
    first = 0
    second = 1

    for i in range(n):
        temp = second
        second = first + second
        first = temp

    return first

# RECURSIVE:


def fib_recurisve(n: int):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# RECURSIVE MEMO:


def fib_memo(n: int, memo={0: 0, 1: 1}) -> int:
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

# RECURSIVE BOTTOM UP:


def fib_bottom_up(n: int) -> int:
    if n == 0:
        return 0
    else:
        previousFib, currentFib = 0, 1
        for i in range(n - 1):
            previousFib, currentFib = currentFib, previousFib + currentFib
        return currentFib
