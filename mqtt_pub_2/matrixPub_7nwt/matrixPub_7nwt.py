#------------------------------------
# @calling
# @purpose : Time/Weather/News Publish(MQTT)
# @date : 2015-12-05
# @Author : Kouji Nakashima / kuc-arc-f.com
#------------------------------------
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
#nCountNew=0

mTyp_WDAT =1
mTyp_TIME =2
mTyp_NEWS =3

def proc_newsPub(items, sHHMM):
	clsPub=com_mqttPub.mqttPubClass()
	for item in items:
		#print( "item="+ item)
		clsPub.send_pubw(item ,mTopic)

if __name__ == "__main__":
	clsSend= com_sendString.sendStringClass()
	clsPub=com_mqttPub.mqttPubClass()
	from datetime import datetime
	tmBef = datetime.now()
	iTyp=mTyp_TIME
	while True:
		tmNow = datetime.now()
		tmSpan = tmNow - tmBef
		iSpan = tmSpan.total_seconds()
		time.sleep(1.0)
		sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		#sHHMM = datetime.now().strftime("%H:%M")
		print("time=" +sTime)
		if iSpan > mTimeMax:
			tmBef = datetime.now()
			try:
				clsNews= com_news.newsClass()
				items = clsNews.get_newsData( mMaxTitle )
				for item in items:
					sHHMM = datetime.now().strftime("%H:%M")
					clsPub.send_pubw(sHHMM ,mTopic)
					time.sleep(2.0)
					clsPub.get_sendWdata("Fukuoka", mTopic)
					time.sleep(2.0)
					sTitle= "!" + item["title"]
					lst=clsSend.get_List( sTitle )
					proc_newsPub(lst ,sHHMM)
					#time.sleep(2.0)
			except:
				print "--------------------------------------------"
				print traceback.format_exc(sys.exc_info()[2])
				print "--------------------------------------------"
	


