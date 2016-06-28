#!/bin/python3

# TODO: add command line arguments -c -o
#       add checking for config file
#       fix output to append properly
#

import sqlite3

configFile = 'config.txt'

def main():

    # parse config params
    configLines = []
    dbLoc = ''
    queryLoc = ''
    queryString = ''
    outputLoc = ''

    with open(configFile) as config:
        for line in config:
            configLines.append(line)
    # end while opening config file

    dbLoc = configLines[0].rstrip()
    queryLoc = configLines[1].rstrip()
    outputLoc = configLines[2].rstrip()
    
    with open(queryLoc) as queryFile:
       queryString = queryFile.read() 

    # perform operations on database
    dbConnection = sqlite3.connect(dbLoc)

    dbCursor = dbConnection.cursor()

    dbCursor.execute(queryString)

    results = dbCursor.fetchall()

    dbConnection.close()

    # process results
    with open(outputLoc, 'w') as output:
        for result in results:
            #print(result[0] + ': ' + result[1])
            output.write(result[0]+': ' + result[1] + '\n')

# end def main

if __name__ == "__main__":
    main()
# end of file
