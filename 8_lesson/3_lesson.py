# def our_orint (par1, par2, keyw_par=1, keyw_par2=None):
#     print  (par1, par2, keyw_par=1, keyw_par2=None)
#
# our_orint('Test' ,'ate')

def our_better_print (*args, **kwargs):
    # print (type(args))
    # print (type(kwargs))
    for arg in args:
        print (arg)

our_better_print('Test' ,'ate', 4, 5, key = 'value', key2= 4)

# def lsit_divisibles(start, stop, divisor):
#     divisibles= []
#     for num in range (start, stop):
#         if num %
#
# args - {'start':1, 'stop':3, 'divisor':5}
# print
#
# # wrapper