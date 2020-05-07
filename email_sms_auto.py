import smtplib
import requests
import random
from bs4 import BeautifulSoup
import time
from email.mime.text import MIMEText

email = "youremail@gmail.com"
phone = "yourphonenumber@messaging.sprintpcs.com" # Boost Mobile


def scrape_data(): # this is a web scraping function that 
    page = requests.get("https://www.briantracy.com/blog/personal-success/26-motivational-quotes-for-success/") # page is a Response object. we can get all information from this object
    soup = BeautifulSoup(page.content, 'html.parser') 
    test = ""

    for blah in soup.find_all(id='maincounter-wrap'):
        test = test + (blah.h1.text)
        test = test + " " + (blah.div.span.text) + "\n"
    # put data in TXT
    print(test)      
    msg = MIMEText(test)
    send_message(msg)

def send_message(arg_msg):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("bot_email@gmail.com", "bot_password") # Bot email and password here
    server.sendmail(
    "bot_email@gmail.com", 
    email, # Change to phone if sending SMS message
    arg_msg.as_string())
    server.quit()

scrape_data()

# https://www.briantracy.com/blog/personal-success/26-motivational-quotes-for-success/