#! /usr/bin/env python
def bread(func):
    def wrapper(*args, **kwargs):
        print "</''''''\>"
        func(*args, **kwargs)
        print "<\______/>"
    return wrapper

def layers(number=1):
    def wrap(func):
        def wrapped_f(*args, **kwargs):
            for _ in range(number):
                func(*args, **kwargs)
        return wrapped_f
    return wrap

def ingredients(with_cheese=False):
    def wrap(func):
        def wrapper(*args, **kwargs):
            print
            print "#tomatoes#"
            func(*args, **kwargs)
            print "~salad~"
            if with_cheese:
                print "*cheese*"
            print
        return wrapper
    return wrap

@bread
@layers(number=2)
@ingredients(with_cheese=True)
def sandwich(food='--ham--'):
    print food

if __name__ == '__main__':
    print
    sandwich()
    print