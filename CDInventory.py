"""
Created on Sat Aug  8 23:05:36 2020

@author: shakedbason
"""

#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignment 05,cd inventory
# Change Log: (Who, When, What)
# DBiesinger, 2020-Aug-11, Created File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            ds = row.split(',')
            print(ds[0])
            dicRow = {'id':int(ds[0]), 'artist':ds[1], 'title':ds[2]}
            lstTbl.append(dicRow)
        objFile.close()
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id':intID,'artist':strTitle, 'title':strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print('{}  |  {}  |  {}'.format(row['id'], row['artist'], row['title']))
    elif strChoice == 'd':
        idSearch = input("Enter the ID of the CD you would like to delete: ")
        idIntSearch = int(idSearch)
        for counter in range(len(lstTbl)):
            if lstTbl[counter]['id'] == idIntSearch:
                print('remove')
                lstTbl.pop(counter)
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        with open(strFileName,'w'): pass
    
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            strRow += str(row['id']) + ','
            strRow += str(row['artist']) + ','
            strRow += str(row['title']) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

