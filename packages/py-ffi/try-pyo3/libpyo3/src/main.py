import timeit

import libpyo3


def benchmark():
    print("-" * 20)

    # 性能测试
    print(
        f"rust sum: {
            timeit.timeit(
                'libpyo3.sum_as_string(1, 1)',
                number=100000,
                setup='import libpyo3',
            )
        }"
    )

    print(
        f"rust fib:\t {
            timeit.timeit(
                'libpyo3.fib(200)',
                number=100000,
                setup='import libpyo3',
            )
        }"
    )

    print(
        f"rust fib2:\t {
            timeit.timeit(
                'libpyo3.fib2(200)',
                number=100000,
                setup='import libpyo3',
            )
        }"
    )

    print(
        f"rust fib slow:\t {
            timeit.timeit(
                'libpyo3.fib_slow(200)',
                number=100000,
                setup='import libpyo3',
            )
        }"
    )

    print(
        f"rust fib fast:\t {
            timeit.timeit(
                'libpyo3.fib_fast(200)',
                number=100000,
                setup='import libpyo3',
            )
        }"
    )


def main():
    print(f"rust fuctions: {libpyo3.__all__}")
    print(f"rust sum: {libpyo3.sum_as_string(1, 1)}")
    print(f"rust fib: {libpyo3.fib(2)}")
    print(f"rust fib: {libpyo3.fib(20)}")
    print(f"rust fib: {libpyo3.fib(200)}")
    print(f"rust fib2: {libpyo3.fib2(200)}")
    print(f"rust fib slow: {libpyo3.fib_slow(200)}")
    print(f"rust fib fast: {libpyo3.fib_fast(200)}")

    benchmark()


if __name__ == "__main__":
    main()
