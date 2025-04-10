#
# 对照组: 纯 python 实现, 不使用 cython 编译加速
#
def pyfib(n: int) -> float:
    a: float = 0.0
    b: float = 1.0

    for _ in range(n):
        a, b = b, a + b
    return a
