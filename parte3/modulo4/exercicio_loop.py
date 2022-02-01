x = [1,2,3,4,5,6]

for i in x:
    print(i)

y=iter(x)
try:
    while True:
        print(next(y))
except StopIteration as e:
    pass