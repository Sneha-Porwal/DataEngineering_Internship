# Dictionary for numbers and their squares from 1 to 10
squares = {}

for n in range(1, 11):
    squares[n] = n * n

for key, value in squares.items():
    print(key, ":", value)

