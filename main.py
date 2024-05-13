import smtplib
import requests
import time
import schedule
from datetime import datetime, date
from progress.bar import ChargingBar
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

# TODO
# - Schedule main function daily at 08:00

# SMTP server details
PORT = 465
SMTP_SERVER = "smtp.gmail.com"

# Email account details
SENDER_NAME = "Impulse Newsletter"
SENDER_EMAIL = "automail.newsletter@gmail.com"
SENDER_APP_PASSWORD = "<password>"

# Links
UNSUBSCRIBE_LINK = "http://localhost:5173/unsubscribe?email="
API_LINK = "http://localhost:3001/api/v1"

# API Endpoints
ALL_EMAILS_ENDPOINT = API_LINK + "/email/all"
SET_SENT_ENDPOINT = API_LINK + "/newsletter/set/posted"
UNSENT_NEWSLETTER_ENDPOINT = API_LINK + "/newsletter"

# Newsletter template
template = open('template.html')
soup = BeautifulSoup(template.read(), "html.parser")

email_template = soup.find('section')
html_start = str(soup)[:str(soup).find(str(email_template))].replace('\n', '')
html_end = str(soup)[str(soup).find(str(email_template)) + len(str(email_template)):].replace('\n', '')

def main():
    """
    Sends a newsletter email to all subscribers.
    """
    content = has_an_unsent_newsletter()
    if (content == False):
        return print("[{}] No new newsletter to send".format(get_current_date_time()))

    get_all_emails_request = requests.get(url = ALL_EMAILS_ENDPOINT)
    response = get_all_emails_request.json()

    bar = ChargingBar("Sending Newsletter", max = len(response))
    bar.next()

    # Log into the email newsletter account
    server = smtplib.SMTP_SSL(SMTP_SERVER, PORT)
    server.login(SENDER_EMAIL, SENDER_APP_PASSWORD)

    # Populate the newsletter template
    newsletter_title = email_template.article.p
    newsletter_title.string = content['title']

    newsletter_body = email_template.article.div.p
    newsletter_body.clear()
    newsletter_body.append(BeautifulSoup(content['content'], "html.parser"))

    newsletter_image = email_template.div.img
    newsletter_image['src'] = content['image']

    # Send the newsletter to all subscribers
    for recipient in response:
        # Unsubscribe link is created for each recipient
        newsletter_unsubscribe = email_template.footer.p.a
        newsletter_unsubscribe['href'] = UNSUBSCRIBE_LINK + recipient['email']

        newsletter_content = str(email_template)

        body = html_start + newsletter_content + html_end

        message = MIMEText(body, 'html')
        message['Subject'] = content['title']
        message['From'] = SENDER_NAME
        message['To'] = recipient['email']

        server.sendmail(SENDER_EMAIL, recipient['email'], message.as_string())
        bar.next()

    set_posted_newsletter_request = requests.get(url = SET_SENT_ENDPOINT)
    if (set_posted_newsletter_request.status_code != 200):
        return print("\n[{}] An error has occurred and the newsletter has not been set as posted".format(get_current_date_time()))
    print("\n[{}] Newsletter sent to all subscribers".format(get_current_date_time()))
    bar.finish()

def has_an_unsent_newsletter():
    """
    Attempts to find a newsletter that has not been sent yet.
    """
    get_unsent_newsletters_request = requests.get(url = UNSENT_NEWSLETTER_ENDPOINT)
    response = get_unsent_newsletters_request.json()
    
    if (get_unsent_newsletters_request.status_code == 404):
        return False
    return response

def get_current_date_time():
    """
    Returns the current date and time.
    """
    current_date = date.today()
    current_time = datetime.now()
    return str(current_date) + " " + current_time.strftime("%H:%M:%S")

if __name__ == "__main__":
    print("██████████  Impulse Newsletter Python Script  ██████████")
    print("[{}] Script started".format(get_current_date_time()))
    schedule.every().day.at("08:00").do(main)

    # Continuously run tasks that are scheduled to run
    while True:
        schedule.run_pending()
        time.sleep(1)