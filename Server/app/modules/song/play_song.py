import time
import subprocess as sp
import sys
import os
def play():
	try:	
		path = os.getcwd() + '/app/medias/'
		song_name = path+"i want to get free.mp3";
		p = sp.Popen(["vlc",song_name])
		print str(p.pid)
		return {'status':True,'pid':p.pid}	
	except Exception as e:
		print e
		return {'status':False,'pid':-1}
	#p.kill()
