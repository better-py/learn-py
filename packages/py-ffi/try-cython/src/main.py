from fib.fib import fib
from fib.fibonacci import fib as fibonacci


def main():
    print(f"python version: {fibonacci(2000)}")
    print(f"cython version: {fib(20)}")


if __name__ == "__main__":
    main()
