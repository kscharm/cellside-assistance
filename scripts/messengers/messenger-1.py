import bs4
import time

from googlevoice import Voice


def extractsms(htmlsms):
    msgitems = []
    tree = bs4.BeautifulSoup(htmlsms, features="xml")
    conversations = tree.findAll("div",  attrs={"id": True}, recursive=False)
    for conversation in conversations:
        rows = conversation.findAll(attrs={"class": "gc-message-sms-row"})
        for row in rows:
            msgitem = {"id": conversation["id"]}
            spans = row.findAll("span", attrs={"class": True}, recursive=False)
            for span in spans:
                cl = span["class"].replace('gc-message-sms-', '')
                msgitem[cl] = (" ".join(span.findAll(text=True))).strip()
            msgitems.append(msgitem)
    return msgitems

def run():
    i = 0

    while True:
        i += 1

        voice = Voice()
        voice.login("tlee753server@gmail.com", "13577531")
        voice.sms()

        for msg in extractsms(voice.sms.html):
            if msg:
                print(msg)
                caller = msg["from"].replace("+", "").replace(":", "")
                voice.send_sms(caller, "Are you kidding me?")

                for message in voice.sms().messages:
                    if message.isRead:
                        message.delete()

        print('Idle Counter: ' + str(i))
        time.sleep(8)


__name__ == '__main__' and run()
