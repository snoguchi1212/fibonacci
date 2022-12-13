from fastapi import FastAPI, Query, status

from app.model.fibonacci import FibonacciNumber

app = FastAPI()


@app.get("/fib", status_code=status.HTTP_200_OK)
def respond_nth_fibonacci_number(
        fibonacci_idx: int = Query(ge=1, le=10000, alias="n")
):
    return {"result": FibonacciNumber(fibonacci_idx).fibonacci_nth_number()}
