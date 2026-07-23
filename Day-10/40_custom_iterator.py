class NumberIterator:
    def __init__(self, N):
        self.N = N
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.N:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
            
if __name__ == "__main__":
    numbers = NumberIterator(10)
    for num in numbers:
        print(num, end=" ")