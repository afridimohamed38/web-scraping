import requests
import selectorlib
import smtplib, ssl
import os
import time

URL = "https://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """ Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    return value


def store(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read():
    with open("data.txt", "r") as file:
        return file.read()


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "afridimohamed38@gmail.com"
    password = os.getenv("APP_PASSWORD")

    receiver = "afridimohamed38@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        content = read()
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                message = f"New event found {extracted}"
                send_email(message)
        time.sleep(30)
