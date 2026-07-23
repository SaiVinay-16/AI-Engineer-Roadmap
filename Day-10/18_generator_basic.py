def sample_gen():
    for i in range(1,6):
        yield i
temp=sample_gen()
for num in temp:
    print(num)