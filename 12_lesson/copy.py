import sys
import shutil

# if __name__ == '__main__':
#     print (sys.argv)
#     try:
#         src = sys.argv[1]
#         dest = sys.argv[2]
#     except IndexError:
#         print ('Pouzij presne 2 arguemnty')
#         exit
#     shutil.copy (src,dest)

if __name__ == '__main__':
    print (sys.argv)
    try:
        src, dest, *rest = sys.argv[1:]
    except (IndexError, ValueError):
        print ('Pouzij presne 2 arguemnty')
        exit
    shutil.copy (src,dest)