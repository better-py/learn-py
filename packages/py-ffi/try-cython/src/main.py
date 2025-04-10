import timeit

import libpyo3
from fib.cyfib import cyfib
from fib.pcfib import pcfib
from fib.pyfib import pyfib
from libpyo3 import fib2 as rsfib2


def main():
    print(f"python version:\t {pyfib(200)}")
    print(f"py+cy version:\t {pcfib(200)}")
    print(f"cython version:\t {cyfib(200)}")
    print("-" * 40)

    print(f"rust version:\t {libpyo3.fib(200)}")
    print(f"rust fib fast:\t {libpyo3.fib_fast(200)}")
    print(f"rust fib slow:\t {libpyo3.fib_slow(200)}")
    print(f"rust2 version:\t {rsfib2(200)}")
    print("-" * 40)

    #
    # 对比这4个实现的性能测试
    #   - cython 实现, 比完全不经过 cython 编译优化的纯 python 实现, 快 13.83 倍!
    #   - 增加 rust + pyo3 实现, 2个版本, 对比性能差异显著!!!
    #       - 版本1, 返回值是 PyResult<f64>, 性能有降低(可忽略, 之前的测试有问题, 重新编译, 性能降低变小)!!!
    #           - (比 cython 中使用 python object 好很多)
    #       - 版本2, 返回值是 f64, 性能接近 cython,(之前测试更好的数据, 应该是误差!!!)
    #
    """_summary_
    几组组实测数据:

    cython benchmark:       0.019643125007860363
    rust2(fast) benchmark:  0.011998083005892113 (数据有问题)
    py+cython benchmark:    0.04922675000852905
    rust(slow) benchmark:   0.023005791998002678 (数据有问题)
    python benchmark:       0.3244316659984179

    cython benchmark:       0.01906333299120888
    rust2(fast) benchmark:  0.02281266698264517 (这组才比较正常)
    rust(slow) benchmark:   0.02291825000429526 (这组才比较正常)
    py+cython benchmark:    0.04856320799444802
    python benchmark:       0.26089745899662375

    cython benchmark:       0.019508041004883125
    rust(fast) benchmark:   0.024531333008781075
    rust(slow) benchmark:   0.02609462500549853
    py+cython benchmark:    0.05109054097556509
    python benchmark:       0.26416191601310857

    """

    print(
        f"cython benchmark: \t{
            timeit.timeit(
                'cyfib(200)',  # c + cython实现
                number=100000,
                setup='from __main__ import cyfib',
            )
        }"
    )
    print(
        f"rust(fast) benchmark: \t{
            timeit.timeit(
                'libpyo3.fib_fast(200)',  # rust + pyo3实现, 返回值类型为 f64
                number=100000,
                setup='import libpyo3',
            )
        }"
    )

    print(
        f"rust(slow) benchmark: \t{
            timeit.timeit(
                'libpyo3.fib_slow(200)',  # rust + pyo3实现, 返回值类型为 PyResult<f64>, 速度降低显著!!!
                number=100000,
                setup='import libpyo3',
            )
        }"
    )

    print(
        f"py+cython benchmark: \t{
            timeit.timeit(
                'pcfib(200)',  # 纯python实现 + cythonb编译加速!
                number=100000,
                setup='from __main__ import pcfib',
            )
        }"
    )
    print(
        f"python benchmark: \t{
            timeit.timeit(
                'pyfib(200)',  # 纯python实现, 未经优化
                number=100000,
                setup='from __main__ import pyfib',
            )
        }"
    )


if __name__ == "__main__":
    main()
