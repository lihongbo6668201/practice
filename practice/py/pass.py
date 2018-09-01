#! python3
#pass.py - An insecure password locker program.

PASSWORDS = { 'email' : 'lihongbo0617',
              'qq' : 'Lihongbo0617',
              'git' : 'lihongbo0617',
              'oa' : 'lhb6668201'}

import sys, pyperclip
if len(sys.argv) < 2:
    print( 'Usage: python pass.py [account] - copy account password' )
    sys.exit()

account = sys.argv[1] #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy( PASSWORDS[account] )
    print( 'Password for ' + account + ' copied to clipboard.' )
else:
    print( 'There is no account named ' + account )
