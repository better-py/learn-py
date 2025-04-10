use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/*

def pcfib(n: int) -> float:
    a: float = 0.0
    b: float = 1.0

    for _ in range(n):
        a, b = b, a + b
    return a


*/

//
// 使用 pyo3 实现 fib(), 注意: 尽量不要使用 PyResult, 会严重拖慢性能!!!
//  - 详细请参考 try-cython 中性能对比测试数据!!!
//
#[pyfunction]
fn fib(n: usize) -> PyResult<f64> {
    // 不要使用递归实现:
    let mut a = 0.0;
    let mut b = 1.0;
    for _ in 0..n {
        let tmp = b;
        b = a + b;
        a = tmp;
    }
    Ok(a)
}

//
// 使用正常的 rust 数据类型返回, 性能非常好!!!
//  - 比 cython 性能还要好!!!
//
#[pyfunction]
fn fib2(n: usize) -> f64 {
    let mut a = 0.0;
    let mut b = 1.0;
    for _ in 0..n {
        let tmp = b;
        b = a + b;
        a = tmp;
    }
    a
}

/// A Python module implemented in Rust.
#[pymodule]
fn libpyo3(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;

    //
    // 注册定义的函数
    //
    m.add_function(wrap_pyfunction!(fib, m)?)?; // 糟糕用法, 作为对照组!!!
    m.add_function(wrap_pyfunction!(fib2, m)?)?; // 正确用法!!!
    Ok(())
}
