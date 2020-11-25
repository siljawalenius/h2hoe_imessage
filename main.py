import os
import random
import schedule
import time 

number = #<your imessage number here (no spaces)>

def get_texts(file_path):
    with open(file_path, 'r') as f:
        texts = f.readlines()
        #print(texts)
    return texts

#get_texts("texts.txt")

#pick a random text from our array to send
texts = get_texts("texts.txt")
num_texts = len(texts)-1
message = texts[random.randint(0, num_texts)]

#function to send the messages
def send_text(cell_num, text):
    os.system('osascript send.scpt {} "{}"'.format(cell_num, text))

#test
#schedule.every().day.at("00:12").do(send_text,number,message)

#schedule a text every hour between 8 and 6
#array of hours to send a text
#I should have just use a range and convert to strings... but it was midnight... so...
hours = ["08:00", "09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00"]

for hour in hours:
    schedule.every().day.at(hour).do(send_text,number,message)


while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)
