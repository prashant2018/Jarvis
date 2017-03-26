import requests 


def main():
	r = requests.get("http://api.apixu.com/v1/current.json?key=e38725d643b9435ca36101603172603&q=Bhubaneswar")
	print r
	json = r.json()
	d = json['current']
	
	temp = d['temp_c']
	humidity=d['humidity']
	
	
	w = d['condition']
	desc = w['text']
	
	wthr={'Temp':temp,'Humidity':humidity,'Description':desc}	
	
	return wthr
	
