# -*- coding: utf-8 -*- 

import datetime
import sys
import traceback
import time

import com_getRss
import com_parseXml
import com_appConst


mOK_CODE=1
mNG_CODE=0

mTimeMax=600

def execute():
	clsRss =com_getRss.getRssClass()
	clsXml = com_parseXml.parseXmlClass()
	sXml = clsRss.get_rss("http://feeds.reuters.com/reuters/topNews?format=xml")
#print sXml.encode('utf-8')
	clsXml.exec_parse( sXml.encode('utf-8') )

if __name__ == "__main__":
    from datetime import datetime
    tmBef     = datetime.now()
    tmBefPush = datetime.now()
    execute()
    while True:
    	tmNow = datetime.now()
    	tmSpan = tmNow - tmBef
    	iSpan = tmSpan.total_seconds()
    	time.sleep(1.0)
    	sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    	#print("time=" +sTime)
    	if iSpan > mTimeMax:
    		tmBef = datetime.now()
    		try:
    			execute()
    		except:
    			print "--------------------------------------------"
    			print traceback.format_exc(sys.exc_info()[2])
    			print "--------------------------------------------"

