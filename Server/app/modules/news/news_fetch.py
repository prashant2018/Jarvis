import requests

def main():
    url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=f075648a2a714d7186071a41b9ffe5bc"
    r = requests.get(url)
    json = r.json()
    s = "1. "+json['articles'][0]['title'] + ", 2 . "+json['articles'][1]['title']
    print s
    return s

if __name__=='__main__':
    main()
