import time

from loguru import logger
from tsidpy import TSID


def generate_id_str():
    """Generate a string representation of a new ID
    生成一个新的 ID 的字符串表示

    _example_: [
        0KAPXXQJKG83B, 0KAPXXQJKG83C,
        0KAPXXQJKG83D, 0KAPXXQJKG83E,
        0KAPXXQJKG83F, 0KAPXXQJKG83G,
        0KAPXXQJKG83H, 0KAPXXQJKG83J,
        0KAPXXQJKG83K, 0KAPXXQJKG83M,
    ]
    Returns:
        _type_: str
        _description_: 生成一个新的 ID 的字符串表示
    """

    return TSID.create()


def generate_id_digit():
    """Generate a numeric representation of a new ID
    生成一个新的 ID 的数字表示

    _example_: [
        696615413582069203, 696615413582069204,
        696615413582069205, 696615413582069206,
        696615413582069207, 696615413582069208,
        696615413582069209, 696615413582069210,
        696615413582069211, 696615413582069212,
    ]

    Returns:
        _type_: int
        _description_: 生成一个新的 ID 的数字表示
    """
    return TSID.create().number


def generate_ids(total: int, typ: str = "str"):
    """生成一组id

    Args:
        total (int): _description_
        typ (str, optional): _description_. Defaults to "str".

    Returns:
        ids (list): 生成的 ID 列表
    """
    ids = []

    fn_id_gen = generate_id_str if typ == "str" else generate_id_digit
    logger.debug(f"Generating {total} IDs of type {typ}")

    for _ in range(total):
        # Generate a new ID
        ids.append(fn_id_gen())
    logger.debug(f"Generated ID count: {len(ids)}")
    logger.debug(f"Generated IDs: {ids[:10]}")
    return ids


def test_id_uniqueness(ids):
    """Test if IDs are unique and print duplicates"""
    id_set = set()
    duplicates = 0
    for id in ids:
        if id in id_set:
            print(f"Duplicate ID: {id}")
            duplicates += 1
        id_set.add(id)
    return duplicates


def benchmark_id_generation_and_uniqueness(count=100000, typ="str"):
    """Benchmark ID generation and uniqueness testing speed"""
    start_time = time.time()
    ids = generate_ids(100000, typ)
    end_time = time.time()

    logger.debug(f"Generated 100000 IDs in {end_time - start_time:.2f} seconds")

    start_time = time.time()
    duplicates = test_id_uniqueness(ids)
    end_time = time.time()

    logger.debug(f"Tested ID uniqueness in {end_time - start_time:.2f} seconds")
    logger.warning(f"Found {duplicates} duplicate IDs")


def main():
    """Main function to run the benchmarks"""
    logger.info("Starting ID generation and uniqueness testing")

    # 字符串 ID 测试
    benchmark_id_generation_and_uniqueness(count=100000, typ="str")

    # 数字 ID 测试
    benchmark_id_generation_and_uniqueness(count=100000, typ="digit")

    logger.info("Finished ID generation and uniqueness testing")


if __name__ == "__main__":
    main()
