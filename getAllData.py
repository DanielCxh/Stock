# -*- encoding:UTF-8 -*-

from Tkinter import *
#import tkMessageBox
import urllib2
import threading

#-----------------------------------------#
STATE_ERROR = -1
STATE_NORMAL = 0

DOWNLOAD_PATH = ""

# Yahoo finance url
yahooFinanceUrl = "http://table.finance.yahoo.com/table.csv?s="

# Shanghai
LOCATION_SH = ".ss"

# Shenzheng
LOCATION_SZ = ".sz"

dataList = "f=snd1l1c6"

#----------------------------------------#


def loadFile(url):
	# The state used to save current usefull or useless
	# Init the state as START_ERROR
	state = STATE_ERROR
	global fileName

	
	
	try:
	    f = urllib2.urlopen(url)
	    state = STATE_NORMAL
	    
	except urllib2.HTTPError, e:
		errLog = "[%s] open fail. Code = [%d]" % (url, e.code)
		print errLog

	if STATE_NORMAL == state :

            # Set the file path to save the download files
	    DOWNLOAD_PATH = "data/" + fileName + ".csv"
	    
	    with open(DOWNLOAD_PATH, "wb") as data:
	    	data.write(f.read())
	   	print "Loaded! " + fileName
	else:
	    pass


# Get all stock data from internet
def getAllData(stockNum):

        global fileName
        
        # Download start
	print "Load Start!"

        stockNum = "%s%s" % (stockNum, LOCATION_SH) 
        url = yahooFinanceUrl + stockNum
                
        # Get the file name by split the url by '='
        fileName = url.split("=")[1]
        loadFile(url)
        #print url

#-----------------------------------------#

#---------------CALL BACK----------------------#
class myThread(threading.Thread):
        def __init__(self, threadID, name, counter):
                threading.Thread.__init__(self)
                self.threadID = threadID
                self.name = name
                self.counter = counter

        def run(self):
                getAllData(enteyStockNum.get())

                
def onLoadBtnClicked():
        #tkMessageBox.showinfo("hh","oo")
        print ("Stock Number : %s") % (enteyStockNum.get())
        if "" == enteyStockNum.get():
                print "The stock number is empty!"
        else:
                loadStockFile = myThread(1, "Thread_loading", 1)
                loadStockFile.start()

#----------------SCREEN------------------------#

mainMenu = Tk()
mainMenu.title("Stock")
# Set main screen as 600x400
mainMenu.geometry('600x400')

xMenu = Menu(mainMenu)

enteyStockNum = Entry(mainMenu, text = "Stock number")
enteyStockNum.pack()

loadBtn = Button(mainMenu, text = "Load", command = onLoadBtnClicked)
loadBtn.configure(width = 10, height = 2)
loadBtn.pack()


mainMenu.mainloop()

# End
exitProj = raw_input ('Enter any key to exit the console!')
