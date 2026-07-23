def sample_gen():
    for i in range(1,21):
        if i%2==0:
            yield i
temp=sample_gen()
for num in temp:
    print(num)