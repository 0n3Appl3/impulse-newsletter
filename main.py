import smtplib
import requests
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

# TODO
# - Display email sending progress
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

#########################
# Temporary
subject = "The Nature of Choice"
text = "Ah, choice! The grand illusion that dances before you like a marionette on strings. You see, dear player, your decisions matter—or so you believe. The narrator’s voice guides you, nudging you toward doors, buttons, and existential musings. But is it truly choice when the outcome is predetermined? When the walls echo with laughter, mocking your futile rebellion?<br><br>Observe the branching paths—the tantalizing corridors that beckon. Left or right? Blue or red? Freedom or conformity? You choose, and yet, the threads weave back together, mocking your defiance. The narrator chuckles, for he knows the truth: you are but a rat in his maze, chasing breadcrumbs of agency. The illusion of choice, my dear player, is the cruelest trick of all."
#########################

def main():
    """
    Sends a newsletter email to all subscribers.
    """
    content = has_an_unsent_newsletter()
    if (content == False):
        return print("No new newsletter to send.")

    get_all_emails_request = requests.get(url = ALL_EMAILS_ENDPOINT)
    response = get_all_emails_request.json()

    server = smtplib.SMTP_SSL(SMTP_SERVER, PORT)
    server.login(SENDER_EMAIL, SENDER_APP_PASSWORD)

    for recipient in response:
        newsletter_title = email_template.article.p
        newsletter_title.string = content['title']

        newsletter_body = email_template.article.div.p
        newsletter_body.clear()
        newsletter_body.append(BeautifulSoup(content['content'], "html.parser"))

        newsletter_image = email_template.div.img
        newsletter_image['src'] = content['image']

        # Unsubscribe link is created for each recipient
        newsletter_unsubscribe = email_template.footer.p.a
        newsletter_unsubscribe['href'] = UNSUBSCRIBE_LINK + recipient['email']

        newsletter_content = str(email_template)

        body = html_start + newsletter_content + html_end

        message = MIMEText(body, 'html')
        message['Subject'] = subject
        message['From'] = SENDER_NAME
        message['To'] = recipient['email']

        server.sendmail(SENDER_EMAIL, recipient['email'], message.as_string())

    set_posted_newsletter_request = requests.get(url = SET_SENT_ENDPOINT)
    if (set_posted_newsletter_request.status_code != 200):
        return print("An error has occurred and the newsletter has not been set as posted.")

def has_an_unsent_newsletter():
    """
    Attempts to find a newsletter that has not been sent yet.
    """
    get_unsent_newsletters_request = requests.get(url = UNSENT_NEWSLETTER_ENDPOINT)
    response = get_unsent_newsletters_request.json()
    
    if (get_unsent_newsletters_request.status_code == 404):
        return False
    return response

if __name__ == "__main__":
    main()