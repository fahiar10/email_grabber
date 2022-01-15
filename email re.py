# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 17:24:39 2022

@author: fahiar10
"""

import pyperclip,re

if __name__ == '__main__':
    email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   #@ symbol
    [a-zA-Z0-9.-]+      # domain name
    \.[a-zA-Z]{2,4}     # dot-something
    )''', re.VERBOSE)

    # usn_regex = re.compile(r'4PA\d{2}CS\d{3}')

    text = str(pyperclip.paste())

    matches = email_regex.findall(text)
    # matches = usn_regex.findall(text)

    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No email addresses found.')
        pyperclip.copy('Not Email(s) found')

