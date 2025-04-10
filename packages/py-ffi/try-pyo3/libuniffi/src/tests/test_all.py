import pytest
import libuniffi


def test_sum_as_string():
    assert libuniffi.sum_as_string(1, 1) == "2"
