from typing import List

# Try to import C++ optimized version
try:
    import fibonacci_cpp

    _cpp_available = True
except ImportError:
    _cpp_available = False


def get_implementation():
    """Return current implementation (Python or C++)"""
    return "C++" if _cpp_available else "Python"


def fibonacci(n: int) -> int:
    if _cpp_available:
        return int(fibonacci_cpp.fibonacci(n))

    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def fibonacci_sequence(n: int) -> List[int]:
    if _cpp_available:
        return [int(x) for x in fibonacci_cpp.fibonacci_sequence(n)]

    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return []

    sequence = [0]
    if n == 1:
        return sequence

    sequence.append(1)
    a, b = 0, 1

    for _ in range(2, n):
        a, b = b, a + b
        sequence.append(b)

    return sequence


def fibonacci_with_info(n: int) -> dict:
    if _cpp_available:
        result = fibonacci_cpp.fibonacci_with_info(n)
        return {
            "n": result["n"],
            "value": int(result["value"]),
            "is_even": result["is_even"],
            "digits": result["digits"],
        }

    if n < 0:
        raise ValueError("n must be a non-negative integer")

    value = fibonacci(n)
    is_even = value % 2 == 0

    return {"n": n, "value": value, "is_even": is_even, "digits": len(str(value))}
