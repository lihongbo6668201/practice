#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw del <keyword> - Delete keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw rm - Delete all the keywords.

import shelve, pyperclip, sys
mcbShelf = shelve.open( 'mcb' )

# Save clipboard content.
if len(sys.argv) == 3 :

    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()

    elif sys.argv[1].lower() == 'del':
        del mcbShelf[sys.argv[2]]
    
elif len(sys.argv) == 2:

    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy( str(list(mcbShelf.keys())))

    elif sys.argv[1].lower() == 'rm':
        for key in mcbShelf.keys():
            del mcbShelf[key]

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

# Delete a key
mcbShelf.close()
