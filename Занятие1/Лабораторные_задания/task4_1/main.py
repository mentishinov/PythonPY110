from itertools import count


def task():
    counter = count(100, 10)

    for _ in range(10):
        number = next(counter)
        print(number)

    # TODO распечатать с столбик первые 10 чисел бесконечного итератора


if __name__ == "__main__":
    task()
