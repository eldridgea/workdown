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

def convert_markdown_files_to_html():
    markdown_filepaths = glob.glob("content/*")
    for filepath in markdown_filepaths:
        filename = splitext(basename(filepath))[0]
        markdown.markdownFromFile(input=filepath, 
                                  output="html_output/" + filename + ".html") 

def push_html_to_kv():
    html_filepaths = glob.glob("html_output/*")
    for filepath in html_filepaths:
        filename = splitext(basename(filepath))[0]
        #bash$ wrangler kv:key put --binding=pages "index" "$html"
        return_code = subprocess.run(['wrangler kv:key put --binding=pages ' + filename + ' "$(cat ' + filepath + ')"'], shell=True)
        print(return_code)
        #system('wrangler kv:key put --binding=pages "index" "$(cat ' + filepath + ')"')

def main():
    """ Main entry point of the app """
    convert_markdown_files_to_html()
    print("hello world")
    push_html_to_kv()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()