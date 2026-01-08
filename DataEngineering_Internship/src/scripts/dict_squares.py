def generate_squares(start=1, end=10):
    return {n: n * n for n in range(start, end + 1)}


if __name__ == "__main__":
    squares = generate_squares()
    for key, value in squares.items():
        print(f"{key} : {value}")
