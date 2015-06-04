import os
import sys
import argparse
import markdown2
from colorama import Fore

def css_content(css_dir):
    """

    """
    abs_path = os.path.abspath(css_dir)

    print(Fore.GREEN + "Searching '" + Fore.YELLOW + abs_path + Fore.GREEN + "' recursively for css files..." + Fore.RESET)

    content = ""

    for root, subdirs, files in os.walk(abs_path):
        print(Fore.GREEN + "Searching '" + Fore.YELLOW + root + Fore.GREEN + "'" + Fore.RESET)

        for filename in files:
            if filename.endswith(".css"):
                print(Fore.GREEN + "    Found '" + Fore.YELLOW + filename + Fore.GREEN + "'" + Fore.RESET)

                file_path = os.path.join(root, filename)

                with open(file_path, 'rb') as f:
                    f_content = f.read()
                    content = content + "/n" + f_content

    return content

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts Markdown files to HTML')
    parser.add_argument('--input-dir', action='store', dest='walk_dir', help='Directory to recursively search for Markdown files')
    parser.add_argument('--css-dir', action='store', dest='css_dir', default=None, help='Directory to recursively search for CSS files')

    args = parser.parse_args()

    abs_path = os.path.abspath(args.walk_dir)

    if not args.css_dir is None:
        abs_path_css = os.path.abspath(args.css_dir)
        css_file_content = css_content(abs_path_css)

    print(Fore.GREEN + "Searching '" + Fore.YELLOW + abs_path + Fore.GREEN + "' recursively for markdown files..." + Fore.RESET)

    for root, subdirs, files in os.walk(abs_path):
        print(Fore.GREEN + "Searching '" + Fore.YELLOW + root + Fore.GREEN + "'" + Fore.RESET)

        for filename in files:
            if filename.endswith(".md"):
                print(Fore.GREEN + "    Found '" + Fore.YELLOW + filename + Fore.GREEN + "'" + Fore.RESET)

                file_path = os.path.join(root, filename)

                with open(file_path, 'rb') as f:
                    f_content = f.read()

                    markdowner = markdown2.Markdown()

                    if not abs_path_css is None:
                        html_content = """<!DOCTYPE html>
                                          <html lang="en">
                                            <head>
                                                <meta charset="utf-8">
                                                <style type="text/css">
                                        """
                        html_content += css_file_content

                        html_content += """
                                                </style>
                                            </head>

                                            <body>
                                        """

                        html_content += markdowner.convert(f_content)

                        html_content += """ </body>

                                           </html>
                                        """
                    else:
                        # No CSS
                        html_content = markdowner.convert(f_content)

                    html_file_path = file_path.rstrip(".md") + ".html"

                    with open(html_file_path, "wb") as html_file:
                        html_file.write(html_content)
                        html_file.write(b'\n')


