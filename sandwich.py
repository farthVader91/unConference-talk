

def bread(func):
    def wrapper(*args, **kwargs):
        print args, kwargs
        print "</''''''\>"
        func()
        print "<\______/>"
    return wrapper

def ingredients(*args, **kwargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print args, kwargs
            print "#tomatoes#"
            func(*args, **kwargs)
            print "~salad~"
    return wrapper

# @bread
# @ingredients
def sandwich(food='--ham--', patty_count=1):
    for _ in range(patty_count):
        print food

sandwich = bread(ingredients(sandwich))

if __name__ == '__main__':
    print
    sandwich()
    print

