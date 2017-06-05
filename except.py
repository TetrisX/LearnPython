def do_something(x):
    try:
        print(x)
    except:
        print('gg')


x = 0
while x < 10:
    do_something(x)
x += 1