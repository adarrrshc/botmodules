import requests
import json
def getquote():
    a=requests.get("http://quotes.rest/qod")
    c=a.json()
    print(c['contents']['quotes'][0]['quote'])
if __name__ == "__main__": 
    print("main")
    getquote()
    exit()
