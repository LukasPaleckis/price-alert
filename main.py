from bs4 import BeautifulSoup
import requests
import smtplib
import time
import secrets

# nuskaito faila kuriame nurodoma prekes nuoroda ir kainos priminimas

read_text_input = []
with open('important.txt', 'rt') as myfile:
    for myline in myfile:
        read_text_input.append(myline)
        if myline == '\n':
            read_text_input.remove('\n')
    website_url = read_text_input[0].rstrip()
    desired_price = float(read_text_input[1])

# funkcija prisijungimui prie pasto ir pranesimo issiuntimui


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
# įrašyti savo paštą ir slaptažodį.
    server.login(secrets.sender_email, secrets.password)

    body = f'Perziurek cia: {website_url}'

    mesagge = f'Subject: Pranesimas del kainos\n\n{body}'
    # irasyti pasta is kurio i kuri siunciu
    server.sendmail(
        secrets.sender_email,
        secrets.reciever_email,
        mesagge
    )
    print('Email sent')
    server.quit()

# kainos patikrinimo funkcija


def check_product_price(desired_price, website_url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    website_url = requests.get(
        website_url, headers=headers)
    soup = BeautifulSoup(website_url.content, 'html.parser')
    price = soup.find('span', {'class': 'price'}).get_text()
    price = price.replace('\xa0', '').replace('€', '').replace(',', '.')
    price = price.strip()
    price = float(price)
    if price <= desired_price:
        send_mail()
    else:
        print(price)


check_product_price(desired_price, website_url)
