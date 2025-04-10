#
# 纯 python 实现 + cython 编译加速!!!
#
def pcfib(n: int) -> float:
    a: float = 0.0
    b: float = 1.0

    for _ in range(n):
        a, b = b, a + b
    return a


def fib_show(n):
    """Print the Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b

    print("")
