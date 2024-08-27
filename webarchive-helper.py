#!/usr/bin/python3

import sys
import os
from pathlib import Path

def simplify_url(url: str) -> str:
    folder = url
    folder = folder.replace('https://', '').replace('http://', '')
    folder = folder.replace(':8080', '').replace(':80', '')
    base_folder = folder.split('/')
    if(base_folder[-1].endswith('.swf') or base_folder[-1].endswith('.dcr')):
        base_folder = '/'.join(base_folder[0:-1])
    else:
        base_folder = '/'.join(base_folder)
    return base_folder

def create_folder(folder: str, dest: str):
    dest_path = Path(dest)
    if(os.path.isdir(dest)):
        final_path = dest_path.with_segments(folder)
        os.makedirs(final_path)

def main() -> int:
    args = sys.argv
    if(len(args) < 4):
        return
    if(args[1] == 'folder'):
        url = args[2]
        folder = simplify_url(url)
        print('Folder to be created: ' + folder)
        dest = args[3]
        create_folder(folder, dest)
    return 0

if __name__ == '__main__':
    sys.exit(main())
