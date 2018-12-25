#!/usr/bin/env python2.7
import datetime
import urllib.request
from bs4 import BeautifulSoup
import re
import smtplib
import time

#print(site1)
site= "https://in.bookmyshow.com/buytickets/sarkar-trichy/movie-tric-ET00074493-MT/" #Replace this your movieandcity url
date="20181106" #replace the date with the date for which you'd like to book tickets! Format: YYYYMMDD
site=site+date
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
delay=10 #timegap in seconds between 2 script runs

TO = 'example@example.com' #mail id for which you want to get alerted
# Please add your username and password here, and make sure you 
# toggle allow less secure apps to on 
# https://myaccount.google.com/lesssecureapps?pli=1 
GMAIL_USER = 'example@example.com'
GMAIL_PASS = 'examplepass'


#req = urllib3.Request(site,headers=hdr)
def send_email():
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    SUBJECT = 'Tickets are now available, Book fast'
    TEXT = 'The tickets are now available for the movie.'
    print(TEXT)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print (header)
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()

def loop():

    try:
        page = urllib.request.urlopen(site)
        soup = BeautifulSoup(page, "html.parser")
        soup2 = soup.find_all('div', {'data-online': 'Y'})
        line2 = str(soup2)
        result = re.findall('data-availability="A"', line2)
        if len(result) > 0:
            print("Available")
            temp = len(result)
            send_email()
        else:
            print("Not available yet")
            time.sleep(delay)
    except urllib.error.URLError as e:
        print(e)
        print("Not available yet")


hours=datetime.datetime.now().time()
timelimit=12 #The Time when the script needs to stop ex : 12 or 24 or 15 time is in railway standard
n=0
while(hours.hour<timelimit):
    hours = datetime.datetime.now().time()
    print(str(hours) + " => try : "+str(n))
    n+=1
    loop()