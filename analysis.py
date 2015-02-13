# encoding:UTF-8

import os
import re

rootdir = r".\data"

allFiles = []

allStock = []


class StockData:

    def __init__(self, stock_id, date, stock_open, high, low, close, volume, adjClose):
        self.stock_id = stock_id
        self.date = date
        self.stock_open = stock_open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.adjClose = adjClose

    def getStockId(self):
        return self.stock_id

    def getStockDate(self):
        return self.date

    def getStockOpen(self):
        return self.stock_open

    def getStockClose(self):
        return self.close
    
#--------------------------------------------------------------------#

# Get all the files
def getFiles():
    global allFiles
    for parent, firnames, filenames in os.walk(rootdir):
        allFiles = filenames

def readFile(fileName):

    global allStock

    stock = []
    fs = open(rootdir + "\\" + fileName)

    i = 0
    for line in fs:
        if 0 == 1:
            i = 1
            print "--------------"
            continue
        else:
            data = line.split(",")
            mystock = StockData(fileName, data[0], data[1], data[2], data[3], data[4].split(), data[5], data[6])
            stock.append(mystock)
    allStock.append(stock)
    

def analysis(myStock):
    print "-----------------------"
    total = 0
    #print len(myStock)
    for stock in myStock:
       
        print float(stock.getStockClose().pop()) + 1
        #total = float(stock.getStockClose().pop())

    print total


#--------------------------------------------------------------------#

getFiles()
#print (rootdir + "\\" + allFiles[0])

for myFile in allFiles:
    readFile(myFile)

#print allStock[0][1].getStockClose()
analysis(allStock[0])
#print allStock[0][1].getStockClose()



# End
exitProj = raw_input ('Enter any key to exit the console!')
