
from app.model.fibonacci import FibonacciNumber


class TestFibonacci:

    def test_fibonacci_1st_number(self):
        assert FibonacciNumber(2).fibonacci_nth_number() == 1

    def test_fibonacci_2nd_number(self):
        assert FibonacciNumber(2).fibonacci_nth_number() == 1

    def test_fibonacci_99th_number(self):
        assert FibonacciNumber(99).fibonacci_nth_number() == 218922995834555169026
