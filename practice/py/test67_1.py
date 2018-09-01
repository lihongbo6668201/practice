
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice1', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'mouse', 'goose']]

def printTable( tableData ):
    colWidths = [0] * len( tableData )
    lnum = len( tableData )
    snum = len( tableData[0] )

    for i in range( lnum ):
        for j in range( snum ): 
            if len( tableData[i][j] ) > colWidths[i]:
                colWidths[i] = len( tableData[i][j] )

    for i in range( snum ):
        for j in range( lnum ):
            print( tableData[j][i].rjust( colWidths[j] + 1 ), end = '' )
            if ( j == lnum - 1 ):
                print( '\n' )

printTable( tableData )
