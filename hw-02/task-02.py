import time


def measureTime(target):
    def wrapper(*args, **kwargs):
        begin = time.time()
        outcome = target(*args, **kwargs)
        finish = time.time()
        print(f"Час виконання функції: {finish - begin:.3f} секунди")
        return outcome
    return wrapper


@measureTime
def computeSum(limit):
    return sum(range(1, limit + 1))


def main():
    result = computeSum(1_000_000)
    print(f"Сума чисел: {result}")


if __name__ == "__main__":
    main()
