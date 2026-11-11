
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def is_even(self, number):
        return number % 2 == 0

    def factorial(self, number):
        if number < 0:
            raise ValueError("Negative number not allowed")

        result = 1
        for i in range(1, number + 1):
            result *= i

        return result
