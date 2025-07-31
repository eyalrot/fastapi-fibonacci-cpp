# FastAPI Fibonacci Server with C++ Optimization

[![CI](https://github.com/eyalrot/fastapi-fibonacci-cpp/actions/workflows/ci.yml/badge.svg)](https://github.com/eyalrot/fastapi-fibonacci-cpp/actions/workflows/ci.yml)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-green.svg)](https://fastapi.tiangolo.com/)

High-performance FastAPI server for Fibonacci calculations with C++ optimization using pybind11.

## Features

- 🚀 **High Performance**: C++ implementation with up to 1400x speedup for large numbers
- 🔄 **Automatic Fallback**: Seamlessly falls back to Python if C++ module unavailable
- 🌐 **RESTful API**: Clean API endpoints for Fibonacci operations
- 📊 **Comprehensive Testing**: Full test suite with pytest
- 🔧 **CI/CD**: Automated testing and builds with GitHub Actions

## Performance

Benchmark results comparing Python vs C++ implementations:

| n    | Python (ms) | C++ (ms) | Speedup |
|------|-------------|----------|---------|
| 10   | 0.003       | 0.002    | 1.23x   |
| 100  | 0.005       | 0.001    | 9.35x   |
| 1000 | 0.083       | 0.001    | 154.73x |
| 5000 | 0.718       | 0.000    | 1465.34x|

## Installation

### Requirements

- Python 3.8+
- C++ compiler (g++ or clang++)
- pip

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/eyalrot/fastapi-fibonacci-cpp.git
cd fastapi-fibonacci-cpp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
pip install pybind11
```

3. Build the C++ extension:
```bash
python setup.py build_ext --inplace
```

4. Run the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Get nth Fibonacci Number
```bash
GET /fibonacci/{n}
```
Returns the nth Fibonacci number.

Example:
```bash
curl http://localhost:8000/fibonacci/10
# {"n":10,"value":55}
```

### Get Fibonacci Sequence
```bash
GET /fibonacci/sequence/{n}
```
Returns the first n Fibonacci numbers.

Example:
```bash
curl http://localhost:8000/fibonacci/sequence/10
# {"n":10,"sequence":[0,1,1,2,3,5,8,13,21,34]}
```

### Get Fibonacci Info
```bash
GET /fibonacci/info/{n}
```
Returns detailed information about the nth Fibonacci number.

Example:
```bash
curl http://localhost:8000/fibonacci/info/10
# {"n":10,"value":55,"is_even":false,"digits":2}
```

### API Status
```bash
GET /status
```
Returns the current implementation status (Python or C++).

## Development

### Running Tests

```bash
# Run all tests
pytest -v

# Run with coverage
pytest --cov=. --cov-report=html
```

### Running Benchmarks

```bash
python benchmark.py
```

### Code Quality

```bash
# Format code
black .

# Sort imports
isort .

# Type checking
mypy .
```

## Project Structure

```
fastapi-fibonacci-cpp/
├── main.py                 # FastAPI application
├── math_operations.py      # Python/C++ hybrid module
├── cpp_math/
│   └── fibonacci.cpp      # C++ implementation
├── setup.py               # Build configuration
├── requirements.txt       # Python dependencies
├── test_*.py             # Test files
├── benchmark.py          # Performance benchmarks
└── .github/
    └── workflows/
        └── ci.yml        # CI/CD pipeline
```

## CI/CD

The project uses GitHub Actions for continuous integration:

- **Testing**: Runs on Python 3.8-3.12
- **Linting**: flake8, black, isort, mypy
- **Benchmarking**: Performance tests on every push
- **Coverage**: Reports to Codecov

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- C++ bindings with [pybind11](https://github.com/pybind/pybind11)
- CI/CD with [GitHub Actions](https://github.com/features/actions)