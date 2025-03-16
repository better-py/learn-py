import pythonnet


def hello() -> str:
    print(f"pythonet all: {pythonnet.__all__}")
    return "Hello from try-pythonnet!"


if __name__ == "__main__":
    print(hello())
