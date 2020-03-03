def func(prefix, suffix, *argumenty):
    for arg in argumenty:
        print(prefix + arg + suffix)


func('in', 'ly', 'competent', 'formal', 'credib')


print('')


def name_f(prefix, suffix, *args, **kwargs):
    for arg in args:
        if 'capital' in kwargs and kwargs['capital'] == True:
            arg = arg.upper()
        print(prefix + arg + suffix)


name_f('la', '!', 'mbada', 'mbda', 'corida', capital=True)


print('')


def name_g(prefix, suffix, *args, capital):
    for arg in args:
        if capital:
            arg = arg.upper()
        print(prefix + arg + suffix)


name_g('la', '!', 'mbada', 'mbda', 'corida', capital=True)
