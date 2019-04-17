import bs4
import json
import time
from Language import Language
from googlevoice import Voice


class Messenger():
    def __init__(self):
        print("Messenger Running...")
        self.debug = True
        self.username = "<MY_USERNAME>"
        self.password = "<MY_PASSWORD>"
        # Poll frequency (in seconds)
        self.timer = 8
        self.language = Language()
    
    # Extracts SMS message from HTML using BeautifulSoup
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

    # Runs the Google Voice server and listens for SMS messages
    def run(self):
        i = 0
        # Create new Google Voice instance and login
        voice = Voice()
        voice.login(self.username, self.password)
        while True:
            i += 1
            voice.sms()
            for msg in self.extractsms(voice.sms.html):
                if msg:
                    if self.debug:
                        print(msg)
                    # Write user number and message to data file for webserver
                    caller = msg["from"].replace("+", "").replace(":", "")
                    print(msg["time"] + '\t' + caller + '\t' + msg["text"], file=open("data.tsv", "a"))
                    # Parse and format message using Language class 
                    replyRaw = self.language.reply(msg["text"])
                    replyFormatted = self.language.format(replyRaw)
                    print(type(replyFormatted))
                    print(msg["time"] + '\t' + "17408720211" + '\t' + replyFormatted, file=open("data.tsv", "a"))
                    replyFormatted = replyFormatted.replace("\t", "\n")
                    # Send reply message with patient information back to user
                    voice.send_sms(caller, str(replyFormatted))

                    # Delete previously read messages from Google Voice
                    for message in voice.sms().messages:
                        if message.isRead:
                            message.delete()

            if self.debug:
                print('Idle Counter: ' + str(i))
            time.sleep(self.timer)
        voice.logout()


m = Messenger()
m.run()
