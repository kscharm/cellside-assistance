
import bs4
import time

from googlevoice import Voice


def extractsms(htmlsms):
    """
    extractsms  --  extract SMS messages from BeautifulSoup
    tree of Google Voice SMS HTML.

    Output is a list of dictionaries, one per message.
    """
    msgitems = []										# accum message items here
    # Extract all conversations by searching for a DIV with an ID at top level.
    tree = bs4.BeautifulSoup(htmlsms, features="xml")			# parse HTML into tree
    conversations = tree.findAll("div",  attrs={"id": True}, recursive=False)
    for conversation in conversations:
        # For each conversation, extract each row, which is one SMS message.
        rows = conversation.findAll(attrs={"class": "gc-message-sms-row"})
        for row in rows:								# for all rows
            # For each row, which is one message, extract all the fields.
            # tag this message with conversation ID
            msgitem = {"id": conversation["id"]}
            spans = row.findAll("span", attrs={"class": True}, recursive=False)
            for span in spans:							# for all spans in row
                cl = span["class"].replace('gc-message-sms-', '')
                # put text in dict
                msgitem[cl] = (" ".join(span.findAll(text=True))).strip()
            msgitems.append(msgitem)					# add msg dictionary to list
    return msgitems


def run():

    while True:

        voice = Voice()
        voice.login("tlee753server@gmail.com", "13577531")
        voice.sms()

        for msg in extractsms(voice.sms.html):
            if msg:
                print(msg)
                print(msg["text"])
                voice.send_sms(msg["from"], "Are you kidding me? " + msg["text"] + "??? You are so stupid, nobody says " + msg["text"] + ". Jesus, I ought to send you to jail")
                for message in voice.sms().messages:
                    if message.isRead:
                        message.delete()
        print('hitmarker')
        time.sleep(8)

__name__ == '__main__' and run()
