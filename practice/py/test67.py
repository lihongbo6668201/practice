
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice1', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'mouse', 'goose']]

def printTable( tableData ):
    colWidths = [0] * len( tableData )
    for i in range( len( tableData ) ):
#        print( tableData[i] )
        for j in range( len( tableData[i] ) ): 
            if len( tableData[i][j] ) > colWidths[i]:
                colWidths[i] = len( tableData[i][j] )

#    print( colWidths )
    for i in range( len( tableData[0] ) ):
        for j in range( len( tableData ) ):
            print( tableData[j][i].rjust( colWidths[j] + 1 ), end = '' )
            if ( j == len( tableData ) - 1 ):
                print( '\n' )

printTable( tableData )
