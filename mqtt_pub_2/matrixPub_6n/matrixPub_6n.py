import paho.mqtt.publish as publish
import datetime
import time
import sys
import traceback
import com_appConst
import com_news
import com_mqttPub
import com_sendString
 
mTopic="item-kuc-arc-f/device-1/relay-1"

mTimeMax=15
mMaxTitle=10

def proc_pub(items):
	clsPub=com_mqttPub.mqttPubClass()
	for item in items:
		clsPub.send_pubw(item ,mTopic)

if __name__ == "__main__":
	clsSend= com_sendString.sendStringClass()
	#sPay=""
	from datetime import datetime
	tmBef = datetime.now()
	while True:
		tmNow = datetime.now()
		tmSpan = tmNow - tmBef
		iSpan = tmSpan.total_seconds()
		time.sleep(1.0)
		sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print("time=" +sTime)
		if iSpan > mTimeMax:
			tmBef = datetime.now()
			try:
				clsNews= com_news.newsClass()
				items = clsNews.get_wdata( mMaxTitle )
				for item in items:
					lst=clsSend.get_List(item["title"]  )
					proc_pub(lst)
					time.sleep(2.0)
			except:
				print "--------------------------------------------"
				print traceback.format_exc(sys.exc_info()[2])
				print "--------------------------------------------"
	


