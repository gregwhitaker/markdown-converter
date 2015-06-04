import os
import sys
import argparse
import markdown2
from colorama import Fore

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts Markdown files to HTML')
    parser.add_argument('--dir', action='store', dest='walk_dir', help='Directory to recursively search for Markdown files')
    args = parser.parse_args()

    abs_path = os.path.abspath(args.walk_dir)

    print(Fore.GREEN + "Searching '" + Fore.YELLOW + abs_path + Fore.GREEN + "' recursively for markdown files..." + Fore.RESET)

    for root, subdirs, files in os.walk(abs_path):
        print('--\nroot = ' + root)
        list_file_path = os.path.join(root, 'my-directory-list.txt')
        print('list_file_path = ' + list_file_path)

        with open(list_file_path, 'wb') as list_file:
            for subdir in subdirs:
                print('\t- subdirectory ' + subdir)

            for filename in files:
                file_path = os.path.join(root, filename)

                print('\t- file %s (full path: %s)' % (filename, file_path))

                with open(file_path, 'rb') as f:
                    f_content = f.read()
                    list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
                    list_file.write(f_content)
                    list_file.write(b'\n')