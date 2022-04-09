#! python3
# launce google maps from the commandline or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # get address from the commandline
    address = ''.join(sys.argv[1:])
else: 
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+ address)