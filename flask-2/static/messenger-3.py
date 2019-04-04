import bs4
import json
import time
from googlevoice import Voice


class Messenger():

    def __init__(self):
        print("Messenger Running...")
        self.debug = True
        self.username = "tlee753server"
        self.password = "13577531"
        self.timer = 8

    def extractsms(self, htmlsms):
        msgitems = []
        tree = bs4.BeautifulSoup(htmlsms, features="xml")
        conversations = tree.findAll("div",  attrs={"id": True}, recursive=False)
        for conversation in conversations:
            rows = conversation.findAll(attrs={"class": "gc-message-sms-row"})
            for row in rows:
                msgitem = {"id": conversation["id"]}
                spans = row.findAll("span", attrs={"class": True}, recursive=False)
                for span in spans:
                    cl = span["class"].replace("gc-message-sms-", '')
                    msgitem[cl] = (" ".join(span.findAll(text=True))).strip()
                msgitems.append(msgitem)
        return msgitems

    def run(self):
        i = 0

        voice = Voice()
        voice.login(self.username, self.password)

        while True:
            i += 1

            voice.sms()

            for msg in self.extractsms(voice.sms.html):
                if msg:
                    if self.debug:
                        print(msg)

                    caller = msg["from"].replace("+", "").replace(":", "")
                    print(msg["time"] + "," + caller + "," + msg["text"], file=open("data.csv", "a"))
                    
                    # reply = msg["text"] + " is so cool! :D"
                    reply = dbFunciton(msg["text"])
                    print(msg["time"] + "," + "17408720211" + "," + reply, file=open("data.csv", "a"))
                    voice.send_sms(caller, reply)

                    for message in voice.sms().messages:
                        if message.isRead:
                            message.delete()

            if self.debug:
                print('Idle Counter: ' + str(i))
            time.sleep(self.timer)

m = Messenger()
m.run()
