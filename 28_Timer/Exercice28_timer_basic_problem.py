from time import time, sleep


class Timer:

    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time()
        self.elapsed = self.end_time - self.start_time


if __name__ == "__main__":
    t = Timer()
    with t:
        sleep(0.5)

    print(t.elapsed)