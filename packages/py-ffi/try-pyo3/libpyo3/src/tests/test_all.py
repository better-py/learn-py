import pytest
import libpyo3


def test_sum_as_string():
    assert libpyo3.sum_as_string(1, 1) == "2"
