
def my_gen():
    n=1
    print(f'primeiro print, n={n}')
    yield n

    n+=1
    print(f'segundo print, n={n}')
    yield n

    n+=1
    print(f'terceiro print, n={n}')
    yield n

test = my_gen();
test.__next__();
test.__next__();
test.__next__();
test.__next__();