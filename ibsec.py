#!/usr/bin/env python
import fire
import json
import pyperclip

def lookup(code1, code2):
    with open('codes.json') as codes_file:
        CODES = json.load(codes_file)
    response = CODES[code1 - 1] + CODES[code2 - 1]
    pyperclip.copy(response)
    print (response + ' has been copied to the clipboard!')

if __name__ == '__main__':
  fire.Fire(lookup)
