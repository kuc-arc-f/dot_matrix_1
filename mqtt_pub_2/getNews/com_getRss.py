# -*- coding: utf-8 -*- 
import requests
import json
import urllib
import com_appConst

#com_getRss
class getRssClass:

	def __init__(self):
		print ""

	def get_rss(self, sURL):
		sRet=""
		try:
			r = requests.get(sURL ,  timeout=30)
			print r.status_code
			sRet= r.text
			return sRet
		except:
			print "failue, get_rss"
			raise
		finally:
			print "End ,get_rss"
		return ret

