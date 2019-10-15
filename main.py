from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import secrets

# funkcija prisijungimui prie pasto ir pranesimo issiuntimui


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
# įrašyti savo paštą ir slaptažodį.
    server.login(secrets.sender_email, secrets.password)

    body = 'Perziurek cia: https://www.topocentras.lt/kompiuteriai-ir-plansetes/nesiojamieji-kompiuteriai/nesiojamas-kompiuteris-acer-predator-helios-300-ph315-51-i7-8750h-16-1tb-128gb-ssd-gtx1050ti-4gb-win.html'

    mesagge = f'Subject: {alert}\n\n{body}'
    # irasyti pasta is kurio i kuri siunciu
    server.sendmail(
        secrets.sender_email,
        secrets.reciever_email,
        mesagge
    )
    print('Email sent')
    server.quit()


# pasirinkta kaina
desired_price = 300.00
user_mail = 'pastas@gmail.com'
alert = 'pranesimas del kainos'
# kainos patikrinimo funkcija


def check_product_price(desired_price, website_url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    website_url = requests.get(
        website_url, headers=headers).text
    soup = BeautifulSoup(website_url, 'html.parser')
    price = soup.find('span', {'class': 'price'}).get_text()
    price = price.replace('&nbsp;', '').replace('€', '').replace(',', '.')
    price = price.strip()
    price = float(price)
    if price <= desired_price:
        send_mail()
    else:
        return(price)


# reikia kad sustotu jei issius emaila???????
# while True:
#   check_product_price()
#  time.sleep(84000)
# flask aplikacija
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', **locals())


@app.route('/response', methods=['POST'])
def response():
    website_url = request.form.get("website_url")
    desired_price = request.form.get("desired_price")
    desired_price = float(desired_price)
    price = check_product_price(desired_price, website_url)
    return render_template("index.html", price=price, value=desired_price)


app.run(debug=True)
