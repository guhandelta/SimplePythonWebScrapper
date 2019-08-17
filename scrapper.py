# Packages installed for this app requests, bs4(Beautiful Soup)
import requests # Access a page and pull out all the data from that page
from bs4 import BeautifulSoup # This allows to parse the webpage/site data received using the requests.get() and -
# - pull out individual items form it
import smtplib # Enables the feature to send Emails
import time

URL = 'https://www.amazon.com/Harney-Sons-Pomegranate-Oolong-Sachets/dp/B00JPY0FAC/ref=sr_1_22?keywords=ti+quan+yin&qid=1565994204&s=gateway&sr=8-22'

headers ={"User Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def price_check():

    page = requests.get(URL, headers=headers) # Returns all the data from that website/specified URL

    soup = BeautifulSoup(page.content, 'html.parser') # html.parser parses the page allows for each item to be pulled out

    title = soup.find(id="title").get_text() # There are lot of ways to identifying items using find(), throught id, name, class...etc
    price = soup.find(id="priceblock_ourprice").get_text() # find() returns the first occurance of the items, as per with which parameter it is searched
    cleaned_price = float(price[1:5])

    if(cleaned_price > 9):
        send_mail()

    print(title.strip() + ': \t ')
    print(price.strip())
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587) # (server_domain_name, connection_port_number) 465 for SSL connections, 587 for TLS connections
    server.ehlo()# EHLO or Extended Hello -> command sent by an email server to identify itself when connecting with another email server-
    #- to start the process of sending an email
    server.starttls() # This will encrypt the entire session
    server.ehlo()

    server.login('ngp.tempacc@gmail.com', 'trgpzhooicrnwrxv')

    subject = 'Price Update'
    body = 'Chekout the item at : https://www.amazon.com/Harney-Sons-Pomegranate-Oolong-Sachets/dp/B00JPY0FAC/ref=sr_1_22?keywords=ti+quan+yin&qid=1565994204&s=gateway&sr=8-22'

    msg = f"Subject: {subject}\n\n{body}" # f -> can interpolate

    server.sendmail(
            'ngp.tempacc@gmail.com',
            'varietyrice@gmail.com',
            msg
    )

    print('Mail sent Succesfully!!!!')

    server.quit() # Closing the connection

while(true):
    price_check()
    time.sleep(7200) # Will checkout the price every 20 Hours
