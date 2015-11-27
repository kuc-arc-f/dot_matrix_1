# -*- coding: utf-8 -*- 
import paho.mqtt.publish as publish
import com_appConst
#import datetime
import time
#import sys
#import traceback

#com_mqttPub
class mqttPubClass:

    def __init__(self):
        print ""
        
    def send_pubw(self, sPay ,sTopic):
		clsConst  = com_appConst.appConstClass()
		iWait=0
		iAdd=3
		if (len(sPay) < 1):
			return
		if( len(sPay) > 20 ):
			sPay=sPay[0:20]
		if( len(sPay) > 10 ):
			iAdd=6;
		print("sLen=")
		print(len(sPay))
		publish.single(topic=sTopic, payload=sPay, hostname=clsConst.mMQTT_HostName , port=clsConst.mMQTT_Port )
		print("iWait=")
		iWait = (len(sPay) * clsConst.mWaitMsec) / 1000
		iWait = iWait+iAdd
		print(str(iWait) )
		time.sleep(iWait)
		return