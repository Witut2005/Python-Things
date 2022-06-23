
def test(x,*args, **kwargs):
    print(x)
    for a in args:
        print(a)
    for b in kwargs:
        print(b, kwargs[a])


my_dict = {
    1: "one",
    2: "two",
    3: "three"
}

my_tuple = 1,2,3,4,5

test(1, my_tuple, my_dict)