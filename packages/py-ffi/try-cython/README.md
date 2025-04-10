# Python FFI + C 方案

- python 多语言混编方案

> 双向调用

- python 基于 FFI 方案， 调用其他语言的库
- 其他语言基于 FFI 方案， 调用 python 的库

## quick start

```ruby
# 编译 cython 实现的fib 库, 会自动生成 .c 和 .so 文件
uv run setup.py build_ext --inplace

# 运行示例:
uv run src/main.py
```

## Python + C

- cffi
- [cython](https://github.com/cython/cython): 首选方案, 成熟. 大量热门项目使用.
- mypyc
- [Nuitka](https://github.com/Nuitka/Nuitka)

### mypyc

- [mypyc: GitHub](https://github.com/python/mypy/tree/master/mypyc)
- <https://mypyc.readthedocs.io/en/latest/introduction.html#why-mypyc>
- 新方案, python 官方支持的方案, 目前仍然在测试阶段

### Cython

- [Cython](https://cython.org/): 首选方案, 成熟. 大量热门项目使用.

## References

- <https://github.com/cython/cython>
