import libpyo3


def main():
    print(f"call rust lib: {libpyo3.sum_as_string(100, 22)}")


if __name__ == "__main__":
    main()
