# encoding:UTF-8

import os
import re
import csv

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

    def getStockHigh(self):
        return self.high

    def getStockLow(self):
        return self.low

    def getStockVolume(self):
        return self.volume

    def getStockAdjClose(self):
        return self.adjClose
    
#--------------------------------------------------------------------#

# Get all the files
def getFiles():
    global allFiles
    for parent, firnames, filenames in os.walk(rootdir):
        allFiles = filenames

def readFile(fileName):

    global allStock

    if -1 == fileName.find(".csv", (len(fileName) - len(".csv")), len(fileName)):
        return
    else:
        pass

    stock = []
    fs = open(rootdir + "\\" + fileName)

    # Skip first line
    fs.readline()

    reader = csv.reader(fs)
    for c1, c2, c3, c4, c5, c6, c7 in reader:
        mystock = StockData(fileName, c1, c2, c3, c4, c5, c6, c7)
        stock.append(mystock)
        #print c7
    allStock.append(stock)
    

def analysis(myStock):
    print "-----------------------"

    Evaluation = 0
    
    total = 0
    s_min = 999
    s_max = 0
    
    total_sixty = 0
    s_min_sixty = 999
    s_max_sixty = 0

    total_tirty = 0
    s_min_tirty = 999
    s_max_tirty = 0

    stockId = ""

    max_money = 0
    avr_money = 0
    min_money = 0

    counter = 0
    SIXTY_DAY = 60
    TIRTY_DAY = 30

    for stock in myStock:
        if stockId == "":
            stockId = stock.getStockId()
        else:
            pass
            
        val = float(stock.getStockOpen())
        total = total + val

        # Get 60Day total
        if counter < SIXTY_DAY:
            total_sixty = total_sixty + val

            if counter < TIRTY_DAY:
                total_tirty = total_tirty + val
            else:
                pass
        
        else:
            pass

        # Get the min value
        if s_min > val:
            s_min = val

            if counter < SIXTY_DAY:
                s_min_sixty = val

                if counter < TIRTY_DAY:
                    s_min_tirty =  val
                else:
                    pass
            
            else:
                pass
        
        else:
            pass

        # Get the max value
        if s_max < val:
            s_max = val

            if counter < SIXTY_DAY:
                s_max_sixty = val

                if counter < TIRTY_DAY:
                    s_max_tirty =  val
                else:
                    pass
                
            else:
                pass
        else:
            pass

        counter += 1

    
    print ">StockID = %s" % (stockId)
    print ">Stock number = %d" % (len(myStock))
    print ">Total        = %f" % (total)
    print ">Average      = %f" % (total / len(myStock))

    print ">Min          = %f" % (s_min)
    print ">Max          = %f" % (s_max)
    
    print ">60 Day Total = %f" % (total_sixty)
    print ">60 Day Avg   = %f" % (total_sixty / SIXTY_DAY)

    print ">60 Day Min   = %f" % (s_min_sixty)
    print ">60 Day Max   = %f" % (s_max_sixty)

    print ">30 Day Total = %f" % (total_tirty)
    print ">30 Day Avg   = %f" % (total_tirty / TIRTY_DAY)

    print ">30 Day Min   = %f" % (s_min_tirty)
    print ">30 Day Max   = %f" % (s_max_tirty)



#--------------------------------------------------------------------#

getFiles()

for myFile in allFiles:
    readFile(myFile)

for myStock in allStock:
    analysis(myStock)

# End
exitProj = raw_input ('Enter any key to exit the console!')
