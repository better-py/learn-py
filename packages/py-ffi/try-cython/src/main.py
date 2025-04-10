import timeit

from fib.cyfib import cyfib
from fib.pcfib import pcfib
from fib.pyfib import pyfib


def main():
    print(f"python version: {pyfib(200)}")
    print(f"python+cy version: {pcfib(200)}")
    print(f"cython version: {cyfib(200)}")

    #
    # 对比这3个实现的性能测试
    #   - cython 实现, 比完全不经过 cython 编译优化的纯 python 实现, 快 13.83 倍!
    #
    print(
        timeit.timeit(
            "cyfib(200)",  # cython实现
            number=100000,
            setup="from __main__ import cyfib",
        )
    )
    print(
        timeit.timeit(
            "pcfib(200)",  # 纯python实现 + cythonb编译加速!
            number=100000,
            setup="from __main__ import pcfib",
        )
    )

    print(
        timeit.timeit(
            "pyfib(200)",  # 纯python实现, 未经优化
            number=100000,
            setup="from __main__ import pyfib",
        )
    )


if __name__ == "__main__":
    main()
