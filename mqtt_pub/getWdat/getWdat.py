import threading
import  pywapi
import string
import time

import com_appConst
import com_weather
 
mOK_CODE=1
mNG_CODE=0

mTimeMax=300

def get_wdata():
    clsConst  = com_appConst.appConstClass()
    clsWeaher= com_weather.weatherClass()
    sCity="Tokyo"
    clsWeaher.delete_dat(sCity)
    #tokyo
    result = pywapi.get_weather_from_yahoo('JAXX0085')
    #oosaka
    #result = pywapi.get_weather_from_yahoo('JAXX0071') 
    #fukuoka
    #result = pywapi.get_weather_from_yahoo('JAXX0009') 
    #sapporo
    #result = pywapi.get_weather_from_yahoo('JAXX0078') 
    
    print '---'
    print result['title']
    print 'city: ' + result['location']['city']
    print 'condition: ' + result['condition']['text']
    print 'temp: ' + result['condition']['temp'] + '(C)'
    print 'High Temp: ' + result['forecasts'][1]['high']
    print 'Low Temp: ' + result['forecasts'][1]['low']
    print '---'
    clsWeaher.saveData( result)

if __name__ == "__main__":
	from datetime import datetime
	tmBef = datetime.now()
	while True:
		tmNow = datetime.now()
		tmSpan = tmNow - tmBef
		iSpan = tmSpan.total_seconds()
		time.sleep(1.0)
		sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		#print("time=" +sTime)
		#print("iSpan=" +str(iSpan) )
		if iSpan > mTimeMax:
			tmBef = datetime.now()
			try:
				get_wdata()
			except:
				print "--------------------------------------------"
				print traceback.format_exc(sys.exc_info()[2])
				print "--------------------------------------------"

