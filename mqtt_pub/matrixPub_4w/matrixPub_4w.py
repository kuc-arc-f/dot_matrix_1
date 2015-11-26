import paho.mqtt.publish as publish
import datetime
import time
import sys
import traceback
import com_appConst
import com_weather
import com_mqttPub

mTopic="topic-1126A/device-1/matrix-1"

mTimeMax=15

def get_wdata(sCity):
	sPay=""
	clsConst  = com_appConst.appConstClass()
	clsWeaher= com_weather.weatherClass()
	clsPub=com_mqttPub.mqttPubClass()
	dic= clsWeaher.get_wdata(sCity)
	print(len(dic))
	print(dic)
	if (len(dic) < 1):
		return
	#city
	clsPub.send_pubw(dic["city"] ,mTopic)
	#cond
	clsPub.send_pubw(dic["cond"] ,mTopic)
	#temp-H
	print("temp_H=")
	print(str(dic["temp_H"]))
	sTemp="High Temp:" + str(dic["temp_H"]) + "(C)"
	clsPub.send_pubw(sTemp ,mTopic)
	#temp-L
	sTemp="Low Temp:" + str(dic["temp_L"]) + "(C)"
	clsPub.send_pubw(sTemp ,mTopic)
	return

if __name__ == "__main__":
	sPay=""
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
				get_wdata("Tokyo")
			except:
				print "--------------------------------------------"
				print traceback.format_exc(sys.exc_info()[2])
				print "--------------------------------------------"


