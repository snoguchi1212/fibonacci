from fastapi import FastAPI, Query

from app.fibonacci import FibonacciNumber

app = FastAPI()


@app.get("/fib", status_code=200)
def respond_nth_fibonacci_number(
        fibonacci_idx: int = Query(alias="n")
):
    return FibonacciNumber(fibonacci_idx).fibonacci_nth_number()
