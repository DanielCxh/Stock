# encoding:UTF-8

import urllib2

#-----------------------------------------#
STATE_ERROR = -1
STATE_NORMAL = 0

DOWNLOAD_PATH = ""

yahooFinanceUrl = "http://table.finance.yahoo.com/table.csv?s="

LOCATION_SH = ".ss"
LOCATION_SZ = ".sz"


def loadFile(url):
	# The state used to save current usefull or useless
	# Init the state as START_ERROR
	state = STATE_ERROR
	global fileName
	
	try:
	    f = urllib2.urlopen(url)
	    
	    # Set the file path to save the download files
	    DOWNLOAD_PATH = "data/" + fileName + ".csv"
	    
	    state = STATE_NORMAL
	except urllib2.HTTPError, e:
		errLog = "[%s] open fail. Code = [%d]" % (url, e.code)
		print errLog

	if STATE_NORMAL == state :
	    with open(DOWNLOAD_PATH, "wb") as data:
	    	data.write(f.read())
	   	print "Loaded! " + fileName
	else:
	    pass

i = 601988

while i < 601990:
	stockNum = "%06d%s" % (i, LOCATION_SH) 
	url = yahooFinanceUrl + stockNum
	
	# Get the file name by split the url by '='
	fileName = url.split("=")[1]
	loadFile(url)
	i = i + 1
	#print url





# End
exitProj = raw_input ('Enter any key to exit the console!')
