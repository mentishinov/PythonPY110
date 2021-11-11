def task(camel_case_str: str) -> str:
    return "".join(filter(str.islower, camel_case_str))  # TODO отфильтровать только буквы нижнего регистра


if __name__ == "__main__":
    word = "AbCdEfGh"
    print(task(word))


# if __name__ == "__main__":
#     str_ = "1q2w3e4r5t6y"
#     chars = filter(str.isalpha, str_)  # TODO переписать с помощью filter
#     # chars = [char for char in str_ if char.isalpha()]
#     print("".join(chars))
