import os

from Cython.Build import cythonize
from setuptools import setup


def build(mods=None):
    if mods is None:
        mods = [
            "src/fib/fib.pyx",  # 模块
            "src/fib/fibonacci.py",  # 模块
        ]

    for mod in mods:
        # 编译模块:
        setup(
            ext_modules=cythonize(mod),
        )


if __name__ == "__main__":
    print(f"current dir: {os.getcwd()}")

    build()
