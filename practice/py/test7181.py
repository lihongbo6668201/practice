#! python3

import re,sys

def passwdCheck( passwd ):
    if len( passwd ) < 8:
        print( '长度必须大于8' )
        sys.exit()

    re1 = re.compile( r'[a-z]' ).search( passwd )
    re2 = re.compile( r'[A-Z]' ).search( passwd )
    re3 = re.compile( r'[0-9]' ).search( passwd )

    if re1 == None or re2 == None or re3 == None:
        print( '必须同时含有大小写字母和数字' )
        sys.exit()

    print( '合格口令: ' + passwd )

pawd = input( 'Enter a passwd: ' )
passwdCheck( pawd )
