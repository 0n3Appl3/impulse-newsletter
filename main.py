import smtplib
import requests
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

port = 465
smtp_server = "smtp.gmail.com"

sender_name = "Impulse Newsletter"
sender_email = "automail.newsletter@gmail.com"
sender_app_password = "<password>"

receiver_email = "jedd.lupoy@gmail.com"

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

newsletter_title = email_template.article.p
newsletter_title.string = subject

newsletter_body = email_template.article.div.p
newsletter_body.clear()
newsletter_body.append(BeautifulSoup(text, "html.parser"))

newsletter_unsubscribe = email_template.footer.p.a
# Temp: Unsubscribe link will be set for each subscribed email address
newsletter_unsubscribe['href'] = "http://localhost:5173/unsubscribe?email=" + receiver_email

newsletter_content = str(email_template)

body = html_start + newsletter_content + html_end

message = MIMEText(body, 'html')
message['Subject'] = subject
message['From'] = sender_name
# Temp: Newsletter will be sent to all subscribers
message['To'] = receiver_email

def main():
    URL = "http://localhost:3001/api/v1/email/all"
    get_all_emails_request = requests.get(url = URL)
    emails = get_all_emails_request.json()
    # Temp: Check that the script can call the API endpoint to retreive all subscribers
    print(emails)
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, sender_app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    main()