import time

from math_operations import fibonacci, fibonacci_sequence, get_implementation


def benchmark_fibonacci(n_values):
    print(f"Benchmarking Fibonacci implementation: {get_implementation()}")
    print("-" * 60)

    for n in n_values:
        start_time = time.perf_counter()
        result = fibonacci(n)
        end_time = time.perf_counter()

        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"fibonacci({n:4d}) = {result:20d} | Time: {execution_time:8.3f} ms")

    print("\n" + "-" * 60)


def benchmark_sequence(n_values):
    print("Benchmarking Fibonacci sequence generation:")
    print("-" * 60)

    for n in n_values:
        start_time = time.perf_counter()
        result = fibonacci_sequence(n)
        end_time = time.perf_counter()

        execution_time = (end_time - start_time) * 1000
        print(
            f"fibonacci_sequence({n:4d}) | Length: {len(result):4d} | Time: {execution_time:8.3f} ms"
        )

    print("\n" + "-" * 60)


def compare_implementations():
    print("Comparing Python vs C++ implementations")
    print("=" * 60)

    # Test values
    test_values = [10, 20, 30, 40, 50, 100, 500, 1000, 5000]

    # Benchmark current implementation
    benchmark_fibonacci(test_values)

    # If C++ is available, force Python and compare
    try:
        import fibonacci_cpp  # noqa: F401
        # Temporarily disable C++ to test Python
        import math_operations

        original_cpp_available = math_operations._cpp_available

        print("\nForcing Python implementation for comparison...")
        math_operations._cpp_available = False

        # Benchmark Python
        python_times = []
        for n in test_values:
            start_time = time.perf_counter()
            _ = fibonacci(n)
            end_time = time.perf_counter()
            python_times.append((end_time - start_time) * 1000)

        # Re-enable C++
        math_operations._cpp_available = original_cpp_available

        # Benchmark C++
        cpp_times = []
        for n in test_values:
            start_time = time.perf_counter()
            _ = fibonacci(n)
            end_time = time.perf_counter()
            cpp_times.append((end_time - start_time) * 1000)

        # Display comparison
        print("\nPerformance Comparison:")
        print("-" * 80)
        print(f"{'n':>6} | {'Python (ms)':>12} | {'C++ (ms)':>12} | {'Speedup':>10}")
        print("-" * 80)

        for i, n in enumerate(test_values):
            speedup = (
                python_times[i] / cpp_times[i] if cpp_times[i] > 0 else float("inf")
            )
            print(
                f"{n:6d} | {python_times[i]:12.3f} | {cpp_times[i]:12.3f} | {speedup:9.2f}x"
            )

    except ImportError:
        print("\nC++ module not available. Only Python implementation tested.")


if __name__ == "__main__":
    compare_implementations()

    print("\nSequence generation benchmark:")
    benchmark_sequence([10, 50, 100, 500, 1000])
