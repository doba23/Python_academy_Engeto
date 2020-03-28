paths = {'/bin/mkdir' : None,
         'lib/init/vars/vars.sh' : None,
         '/lib/init/vars.sh' : None,
         '/home/documents/reports/report1.xls' : None,
         '/home/music/album3/song2.mp3' : None,
         '/home/music/album1/song2.mp3' : None,
         '/lib/systemd/system/sudo.service' : None
         }

def main():

    with open('FILESYSTEM') as file:
        filesystem = eval(file.read())

    for path in paths:
        paths[path] = file_exists(path,filesystem)

    from pprint import pprint as pp
    pp(paths)


def file_exists(path,filesystem):
    nodes = split_path(path)
    target = nodes[-1]

    cwd = filesystem['/']

    while nodes:
        node = nodes.pop(0)
        cwd = search_folder(cwd,node)

        if cwd == target and not nodes:
            return True
        elif not cwd:
            break

    return False


def search_folder(folder, target):
    for item in folder:
        if isinstance(item,dict) and target in item:
                return item[target]
        elif item==target:
            return item


def split_path(path):
    if not is_absolute(path):
        return path.split('/')
    else:
        return path[1:].split('/')


def is_absolute(path):
    return path.startswith('/')


main()