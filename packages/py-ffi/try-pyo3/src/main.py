import libpyo3


def main():
    print(f"call rust sum: {libpyo3.sum_as_string(100, 22)}")
    print(f"call rust fib: {libpyo3.fib(20)}")
    print(f"call rust fib: {libpyo3.fib(200)}")


if __name__ == "__main__":
    main()
