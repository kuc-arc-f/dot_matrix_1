# -*- coding: utf-8 -*- 
import paho.mqtt.publish as publish
import datetime
import time
import sys
import traceback
import com_appConst
import com_news
import com_mqttPub
#define

mMaxSend=100
mMaxOne =16

#com_sendString
class sendStringClass:

	def __init__(self):
		print ""

	def get_List(self, sPay):
		List=[]
		iCt=0
		clsConst  = com_appConst.appConstClass()
		
		if (len(sPay) > mMaxSend):
			sPay=sPay[0:mMaxSend]
		items =sPay.split(" ")
		#print("len="+ str(len(items)))
		#print items
		if(len(items) < 1):
			return
		sBuff=""
		sTmp=""
		for item in items:
			sTmp=item
			if( len(sTmp) > mMaxOne):
				sTmp=sTmp[0:mMaxOne]
			#print sTmp
			sAft=sBuff+sTmp
			if(len(sAft) >= mMaxOne):
				List.append(sBuff)
				sBuff=""
				iCt=0
			if(iCt > 0):
				sBuff=sBuff+" "+ sTmp
			else:
				sBuff=sBuff+  sTmp
			iCt=iCt+1
		if(len(sTmp)>0):
			List.append(sTmp)
				
		#print List
		return	List