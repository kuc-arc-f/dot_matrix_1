# -*- coding: utf-8 -*- 
import xml.dom.minidom
import com_appConst
import com_news

#com_parseXml
class parseXmlClass:

	def __init__(self):
		print ""

	def exec_parse(self, sXml ):
		ret={}
		clsConst  = com_appConst.appConstClass()
		clsNews = com_news.newsClass()
		clsNews.delete_dat()
		try:
			dom = xml.dom.minidom.parseString(sXml)
			for node in dom.getElementsByTagName('item'):
				for title in node.getElementsByTagName("title"):
					sTitle = title.firstChild.data
					#print "  " + title.tagName + "=" +sTitle
					clsNews.saveData(sTitle)
		except:
			print "failue, exec_parse"
			raise
		finally:
			print "End ,exec_parse"
		return ret

	def test_parse(self, sXml ):
		ret={}
		clsConst  = com_appConst.appConstClass()
		
		try:
			dom = xml.dom.minidom.parseString(sXml)
			for node in dom.getElementsByTagName('item'):
				for url in node.getElementsByTagName("itemName"):
					print "  " + url.tagName + "=" + url.firstChild.data					
				for item_id in node.getElementsByTagName("itemId"):
					print "  " + item_id.tagName + "=" + item_id.firstChild.data
		except:
			print "failue, test_parse"
			raise
		finally:
			print "End ,test_parse"
		return ret
