def func(prefix, suffix, *argumenty):
    for arg in argumenty:
        print(prefix + arg + suffix)

func('in', 'ly', 'competent', 'formal', 'credib')

def name_f(prefix, suffix, *args, **kwargs):
    for arg in args:
        if 'capital' in kwargs and kwargs['capital'] == True:
            arg = arg.upper()
        print (prefix+arg+suffix)
name_f('la','!', 'mbada', 'mbda', 'corida', capital=True)
