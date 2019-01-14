def double(arg):
    print('Przed:  ', arg)
    arg = arg * 2
    print('Po:   ', arg)


def change(arg):
    print('Przed:   ', arg)
    arg.append('Więcej dannych')
    print('Po:   ', arg)


num = 10
saying = 'hello'
numbers = [43, 43, 44, 47]

double(num)
print('###########')
double(saying)
print('###########')
double(numbers)
print('###########')

print('###########')
change(numbers)
print('###########')