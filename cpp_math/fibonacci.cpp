#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <stdexcept>
#include <cstdint>
#include <unordered_map>

namespace py = pybind11;

class FibonacciCalculator {
private:
    mutable std::unordered_map<int, uint64_t> cache;
    
public:
    FibonacciCalculator() {
        cache[0] = 0;
        cache[1] = 1;
    }
    
    uint64_t fibonacci(int n) const {
        if (n < 0) {
            throw std::invalid_argument("n must be a non-negative integer");
        }
        
        if (cache.find(n) != cache.end()) {
            return cache[n];
        }
        
        uint64_t a = 0, b = 1;
        for (int i = 2; i <= n; ++i) {
            uint64_t temp = a + b;
            a = b;
            b = temp;
            cache[i] = b;
        }
        
        return b;
    }
    
    std::vector<uint64_t> fibonacci_sequence(int n) const {
        if (n < 0) {
            throw std::invalid_argument("n must be a non-negative integer");
        }
        
        std::vector<uint64_t> sequence;
        if (n == 0) return sequence;
        
        sequence.push_back(0);
        if (n == 1) return sequence;
        
        sequence.push_back(1);
        uint64_t a = 0, b = 1;
        
        for (int i = 2; i < n; ++i) {
            uint64_t temp = a + b;
            a = b;
            b = temp;
            sequence.push_back(b);
        }
        
        return sequence;
    }
    
    py::dict fibonacci_with_info(int n) const {
        if (n < 0) {
            throw std::invalid_argument("n must be a non-negative integer");
        }
        
        uint64_t value = fibonacci(n);
        bool is_even = (value % 2 == 0);
        int digits = std::to_string(value).length();
        
        py::dict result;
        result["n"] = n;
        result["value"] = value;
        result["is_even"] = is_even;
        result["digits"] = digits;
        
        return result;
    }
};

// Matrix multiplication method for very large Fibonacci numbers
std::pair<uint64_t, uint64_t> fib_matrix(int n) {
    if (n == 0) return {0, 1};
    
    auto m = fib_matrix(n >> 1);
    uint64_t c = m.first * (2 * m.second - m.first);
    uint64_t d = m.first * m.first + m.second * m.second;
    
    if (n & 1) {
        return {d, c + d};
    } else {
        return {c, d};
    }
}

uint64_t fibonacci_fast(int n) {
    if (n < 0) {
        throw std::invalid_argument("n must be a non-negative integer");
    }
    return fib_matrix(n).first;
}

PYBIND11_MODULE(fibonacci_cpp, m) {
    m.doc() = "Fast Fibonacci calculation using C++";
    
    py::class_<FibonacciCalculator>(m, "FibonacciCalculator")
        .def(py::init<>())
        .def("fibonacci", &FibonacciCalculator::fibonacci, "Calculate nth Fibonacci number")
        .def("fibonacci_sequence", &FibonacciCalculator::fibonacci_sequence, "Generate Fibonacci sequence")
        .def("fibonacci_with_info", &FibonacciCalculator::fibonacci_with_info, "Get Fibonacci info");
    
    m.def("fibonacci", [](int n) {
        static FibonacciCalculator calc;
        return calc.fibonacci(n);
    }, "Calculate nth Fibonacci number");
    
    m.def("fibonacci_sequence", [](int n) {
        static FibonacciCalculator calc;
        return calc.fibonacci_sequence(n);
    }, "Generate Fibonacci sequence");
    
    m.def("fibonacci_with_info", [](int n) {
        static FibonacciCalculator calc;
        return calc.fibonacci_with_info(n);
    }, "Get Fibonacci info");
    
    m.def("fibonacci_fast", &fibonacci_fast, "Calculate nth Fibonacci using matrix method");
}