
#
# 使用 cython 实现,
#   加速效果:
#       1. 比纯 python + cython 编译, 快2倍+
#       2. 比纯 python 实现(不经过 cython 编译优化), 快 13.83 倍!!!
#
def cyfib(int n):
    cdef int i
    cdef double a = 0.0, b = 1.0
    for i in range(n):
        a, b = b, a + b
    return a
