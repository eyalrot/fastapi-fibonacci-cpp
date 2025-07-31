from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

from math_operations import fibonacci, fibonacci_sequence, fibonacci_with_info, get_implementation

app = FastAPI(
    title="Math Operations API",
    description="FastAPI server for mathematical operations with C++ optimization",
    version="2.0.0"
)


class FibonacciResponse(BaseModel):
    n: int = Field(..., description="The position in Fibonacci sequence")
    value: int = Field(..., description="The Fibonacci value at position n")


class FibonacciSequenceResponse(BaseModel):
    n: int = Field(..., description="Number of Fibonacci numbers to generate")
    sequence: List[int] = Field(..., description="List of Fibonacci numbers")


class FibonacciInfoResponse(BaseModel):
    n: int = Field(..., description="The position in Fibonacci sequence")
    value: int = Field(..., description="The Fibonacci value at position n")
    is_even: bool = Field(..., description="Whether the value is even")
    digits: int = Field(..., description="Number of digits in the value")


@app.get("/")
async def root():
    return {
        "message": "Welcome to Math Operations API",
        "implementation": get_implementation(),
        "endpoints": {
            "/fibonacci/{n}": "Get the nth Fibonacci number",
            "/fibonacci/sequence/{n}": "Get first n Fibonacci numbers",
            "/fibonacci/info/{n}": "Get detailed info about nth Fibonacci number",
            "/status": "Get API status and implementation details"
        }
    }


@app.get("/fibonacci/{n}", response_model=FibonacciResponse)
async def get_fibonacci(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="n must be a non-negative integer")
    
    if n > 10000:
        raise HTTPException(status_code=400, detail="n is too large (max 10000)")
    
    try:
        value = fibonacci(n)
        return FibonacciResponse(n=n, value=value)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/fibonacci/sequence/{n}", response_model=FibonacciSequenceResponse)
async def get_fibonacci_sequence(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="n must be a non-negative integer")
    
    if n > 1000:
        raise HTTPException(status_code=400, detail="n is too large (max 1000)")
    
    try:
        sequence = fibonacci_sequence(n)
        return FibonacciSequenceResponse(n=n, sequence=sequence)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/fibonacci/info/{n}", response_model=FibonacciInfoResponse)
async def get_fibonacci_info(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="n must be a non-negative integer")
    
    if n > 10000:
        raise HTTPException(status_code=400, detail="n is too large (max 10000)")
    
    try:
        info = fibonacci_with_info(n)
        return FibonacciInfoResponse(**info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/status")
async def get_status():
    return {
        "status": "running",
        "implementation": get_implementation(),
        "performance": {
            "description": "C++ implementation provides significant speedup for large Fibonacci numbers",
            "typical_speedup": "10-100x for n > 1000"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)