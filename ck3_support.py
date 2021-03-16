import os

exception_folders = [".", "_cache"]
ck3_game_folder = "D:\\games\\SteamLibrary\\steamapps\\common\\Crusader Kings III\\game"

root_folder = os.path.dirname(os.path.realpath(__file__))
mod_folders = [f.path.replace(root_folder, '') for f in os.scandir(os.path.dirname(os.path.realpath(__file__))) if
               f.is_dir()]

for f in mod_folders:
    for e in exception_folders:
        if f.find(e) > 0:
            mod_folders.remove(f)

for f in mod_folders:
    f.replace(root_folder, '')

print(mod_folders)


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
