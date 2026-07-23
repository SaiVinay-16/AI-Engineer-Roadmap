def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

# Example usage:
if __name__ == "__main__":
    counter = infinite_counter()
    for _ in range(10):
        print(next(counter), end=" ")