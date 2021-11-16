def pow_gen(base: int):
    n = 0
    while True:
        yield base ** n
        n += 1


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))



# def count(start_number: float = 1, step: float = 1):
#     while True:
#         yield start_number
#         start_number += step
#
#
# if __name__ == "__main__":
#     my_count = count(10, 0.5)
#     for _ in range(10):
#         print(next(my_count))