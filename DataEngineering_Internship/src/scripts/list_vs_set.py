def check_membership_list(numbers, value):
    return value in numbers


def check_membership_set(numbers, value):
    return value in numbers


if __name__ == "__main__":
    numbers_list = [10, 20, 30, 40, 50]
    numbers_set = {10, 20, 30, 40, 50}

    if check_membership_list(numbers_list, 40):
        print("Element found in list")

    if check_membership_set(numbers_set, 40):
        print("Element found in set")
