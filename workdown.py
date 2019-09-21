#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Eldridge Alexander"
__version__ = "0.0.1"
__license__ = "MIT"

import glob
import markdown
import subprocess

from os.path import basename, splitext
from os import system

class get_markdown_as_bytes:
    """Fakes being a file type object so I can use markdownFromFile for input but out to a variable."""
    html_output = None
    def write(self, input):
        self.html_output = input
    def read(self):
        return self.html_output

def convert_markdown_files_to_html(header, footer):
    markdown_filepaths = glob.glob("content/*")
    for filepath in markdown_filepaths:
        filename = splitext(basename(filepath))[0]
        conversion_output = get_markdown_as_bytes()
        markdown.markdownFromFile(input=filepath, output=conversion_output) 
        html_output_file = open("html_output/" + filename + ".html", "wb")
        html_output_file.write(header)
        html_output_file.write(conversion_output.read())
        html_output_file.write(footer)
        html_output_file.close()

def push_html_to_kv():
    html_filepaths = glob.glob("html_output/*")
    for filepath in html_filepaths:
        filename = splitext(basename(filepath))[0]
        return_code = subprocess.run(['wrangler kv:key put --binding=pages ' + filename + ' "$(cat ' + filepath + ')"'], shell=True)
        print(return_code)

def push_assets_to_kv():
    assets_filepaths = glob.glob("assets/*")
    for filepath in assets_filepaths:
        filename = basename(filepath)
        return_code = subprocess.run(['wrangler kv:key put --binding=assets ' + filename + ' "$(cat ' + filepath + ')"'], shell=True)
        print(return_code)

def get_partials():
    global header
    global footer
    header = open("partials/header.html", "rb").read()
    footer = open("partials/footer.html", "rb").read()

def main():
    """ Main entry point of the app """
    get_partials()
    convert_markdown_files_to_html(header, footer)
    push_html_to_kv()
    push_assets_to_kv()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()