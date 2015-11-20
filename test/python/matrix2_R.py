import paho.mqtt.publish as publish
import datetime
import time
import sys
import traceback

mTopic="topic/device-1/matrix-1"
# mHostName="test.mosquitto.org"
mHostName="localhost"

mTimeMax=25
mTyp_MSG =1
mTyp_TIME=2

if __name__ == "__main__":
	sPay=""
	from datetime import datetime
	tmBef = datetime.now()
	iTyp=mTyp_MSG
	sPay_msg="Merry Christmas"
	while True:
		tmNow = datetime.now()
		tmSpan = tmNow - tmBef
		iSpan = tmSpan.total_seconds()
		time.sleep(1.0)
		sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		sHHMM = datetime.now().strftime("%H:%M")
		sPay=sPay_msg
		if iTyp == mTyp_TIME:
			sPay=sHHMM
		print("time=" +sTime)
		print(str(iTyp))
		if iSpan > mTimeMax:
			tmBef = datetime.now()
			
			try:
				publish.single(topic=mTopic, payload=sPay, hostname=mHostName, port=1883)
				print("OUT:" + sPay)
				iTyp=iTyp+1
				if iTyp > 2:
					iTyp =mTyp_MSG
			except:
				print "--------------------------------------------"
				print traceback.format_exc(sys.exc_info()[2])
				print "--------------------------------------------"
				#clsLog.debug( traceback.format_exc(sys.exc_info()[2]) )


