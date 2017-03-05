import time
import subprocess as sp
import sys
import os
import numpy as np
def play():
	try:
		path = os.getcwd() + '/app/medias/'
		dir_list = os.listdir(path)
		rand_num = np.random.randint(0,len(dir_list))
		song_name = dir_list[rand_num]
		p = sp.Popen(["vlc",path+song_name])
		print str(p.pid)
		return {'status':True,'pid':p.pid}	
	except Exception as e:
		print e
		return {'status':False,'pid':-1}
	#p.kill()
