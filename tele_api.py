# import urllib2
import requests
from os import path

url='https://api.telegram.org/bot'

try:
    path=path.dirname(path.dirname(path.abspath( __file__ )))
    api_key = '615160058:AAEze_fVUzGe1gKok9-WWNl-rmmJfSc3x9s'

except:
    print ('ERROR: No Telegram API_key. Please Check Again')
    exit()

class Telegram():
    def __init__(self,to_which):
        self.ch_id = to_which

    def send(self,text=''):
        data={'chat_id':self.ch_id,'text':text}
        socket=requests.post(url=url+(api_key.strip())+'/sendMessage',data=data)
        if (socket.status_code != 200):
            print("error Occored (Telegram): " + str(socket.status_code))
        socket.close()

    def notification(self,text='',path=''):
        self.send(text+'\n'+path)

    # def test(self):
    #     req=urllib2.Request(url+api_key+'/sendMessage')
    #     req.add_data(self.ch_id+'&text=''test''')
    #     socket=urllib2.urlopen(req)
    #     print (socket.read(300))