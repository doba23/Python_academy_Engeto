file = open('test.txt')
print('file name:',file.name)
print('file encoding:', file.encoding)
print('file mode:', file.mode)

import sys

print( sys.getsizeof(file))