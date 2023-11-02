from datetime import datetime


def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        print(result)
        print(f"Execution Time: {execution_time.microseconds}")
    return wrapper


@calculate_execution_time
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)
