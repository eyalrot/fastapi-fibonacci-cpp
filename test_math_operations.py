import pytest

import math_operations
from math_operations import (fibonacci, fibonacci_sequence,
                             fibonacci_with_info, get_implementation)


class TestFibonacci:
    def test_base_cases(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5

    def test_known_values(self):
        known_values = [
            (10, 55),
            (15, 610),
            (20, 6765),
            (30, 832040),
            (40, 102334155),
            (50, 12586269025),
        ]

        for n, expected in known_values:
            assert fibonacci(n) == expected, f"fibonacci({n}) should equal {expected}"

    def test_negative_input(self):
        with pytest.raises(ValueError, match="n must be a non-negative integer"):
            fibonacci(-1)

        with pytest.raises(ValueError, match="n must be a non-negative integer"):
            fibonacci(-10)


class TestFibonacciSequence:
    def test_empty_sequence(self):
        assert fibonacci_sequence(0) == []

    def test_single_element(self):
        assert fibonacci_sequence(1) == [0]

    def test_two_elements(self):
        assert fibonacci_sequence(2) == [0, 1]

    def test_sequence_generation(self):
        assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]
        assert fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_sequence_length(self):
        for n in [10, 50, 100, 500]:
            seq = fibonacci_sequence(n)
            assert len(seq) == n, f"Sequence length should be {n}"

    def test_negative_input(self):
        with pytest.raises(ValueError):
            fibonacci_sequence(-1)


class TestFibonacciWithInfo:
    def test_info_structure(self):
        info = fibonacci_with_info(10)
        assert "n" in info
        assert "value" in info
        assert "is_even" in info
        assert "digits" in info

    def test_info_values(self):
        info = fibonacci_with_info(10)
        assert info["n"] == 10
        assert info["value"] == 55
        assert info["is_even"] is False
        assert info["digits"] == 2

    def test_even_odd_detection(self):
        even_indices = [0, 3, 6, 9, 12, 15]
        for n in even_indices:
            info = fibonacci_with_info(n)
            assert info["is_even"] is True, f"fibonacci({n}) should be even"

    def test_digit_count(self):
        test_cases = [
            (5, 1),  # fib(5) = 5 (1 digit)
            (10, 2),  # fib(10) = 55 (2 digits)
            (20, 4),  # fib(20) = 6765 (4 digits)
            (30, 6),  # fib(30) = 832040 (6 digits)
        ]

        for n, expected_digits in test_cases:
            info = fibonacci_with_info(n)
            assert info["digits"] == expected_digits


class TestImplementation:
    def test_implementation_detection(self):
        impl = get_implementation()
        assert impl in [
            "Python",
            "C++",
        ], "Implementation should be either Python or C++"
        print(f"Current implementation: {impl}")

    def test_consistency_between_implementations(self):
        # Force Python implementation
        original_cpp = math_operations._cpp_available

        try:
            # Test with Python
            math_operations._cpp_available = False
            python_results = {
                "fib_10": fibonacci(10),
                "seq_5": fibonacci_sequence(5),
                "info_20": fibonacci_with_info(20),
            }

            # Test with C++ if available
            if original_cpp:
                math_operations._cpp_available = True
                cpp_results = {
                    "fib_10": fibonacci(10),
                    "seq_5": fibonacci_sequence(5),
                    "info_20": fibonacci_with_info(20),
                }

                # Compare results
                assert python_results["fib_10"] == cpp_results["fib_10"]
                assert python_results["seq_5"] == cpp_results["seq_5"]
                assert python_results["info_20"] == cpp_results["info_20"]

        finally:
            # Restore original state
            math_operations._cpp_available = original_cpp


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
