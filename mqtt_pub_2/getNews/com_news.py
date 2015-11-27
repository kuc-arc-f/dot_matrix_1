# -*- coding: utf-8 -*- 
import MySQLdb
import com_appConst
#define


#com_news
class newsClass:

    def __init__(self):
        print ""
        
    def delete_dat(self ):
    	ret=False
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	cursor = connection.cursor()
    	sSql="delete from t_news;"
    	cursor.execute(sSql)
    	connection.commit()
    	connection.close()
    	ret=True
    	return ret

    def saveData(self, sTitile ):
    	ret=False
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	cursor = connection.cursor()
    	sSql=u"INSERT INTO t_news (title"
    	sSql=sSql+",created"
    	sSql=sSql+") values ("
    	sSql=sSql+ " \""+ sTitile +"\" "
    	sSql=sSql+",now() );"
    	#print sSql
    	cursor.execute(sSql)
    	connection.commit()
    	cursor.close()
    	connection.close()
    	ret=True
    	return ret
    	