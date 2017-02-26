import sys
import requests
import bs4
import subprocess as sp

class SearchVideo(object):

    def __init__(self, name):
        self.name = name
        self.url = "https://www.youtube.com/results?search_query="
        self.main_url = "https://www.youtube.com"
        self.a_class = ".yt-uix-tile-link.yt-ui-ellipsis.yt-ui-ellipsis-2.yt-uix-sessionlink.spf-link"

    def parseData(self):
        self.url += self.name


        try:
            res = requests.get(self.url)
            res_soup = bs4.BeautifulSoup(res.text)
            video_list = res_soup.select(self.a_class)
            first_video_url = self.main_url + video_list[0].get('href')
            return str(first_video_url)
        except Exception as e:
            return None

    def openBrowser(self,url):
        try:
            p = sp.Popen(["firefox",url])
            return p.pid
        except Exception as e:
            print "Internet may be slow! Unable to connect"
            return -1


def main(arguments):
    name = arguments
    try:
        print "Which video would you like to watch ?"
        print "name : ",name
        searchVideo = SearchVideo(name)
        url = searchVideo.parseData()
        pid =  searchVideo.openBrowser(url)
        if pid !=-1:
            context = {'status':True,'pid':pid}
        else:
            context = {'status': False, 'pid': pid}
        return context
    except Exception as e:
        print e
        context = {'status': False, 'pid':-1}
        return context

if __name__ == '__main__':
    main(sys.argv[1:])
