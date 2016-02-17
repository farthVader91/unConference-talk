def bread(func):
    def wrapper(*args, **kwargs):
        print "</''''''\>"
        func(*args, **kwargs)
        print "<\______/>"
    return wrapper

def layers(number=1, with_cheese=False):
    def wrap(func):
        def wrapped_f(*args, **kwargs):
            kwargs.update({
                'with_cheese': with_cheese
                })
            for _ in range(number):
                func(*args, **kwargs)
        return wrapped_f
    return wrap

def ingredients(func):
    def wrapper(*args, **kwargs):
        print
        with_cheese = kwargs.pop('with_cheese', False)
        if with_cheese:
            print "*cheese*"
        print "#tomatoes#"

        func(*args, **kwargs)
        print "~salad~"
        if with_cheese:
            print "*cheese*"
        print
    return wrapper

@bread
@layers(number=2, with_cheese=True)
@ingredients
def sandwich(food='--ham--'):
    print food

if __name__ == '__main__':
    print
    sandwich()
    print