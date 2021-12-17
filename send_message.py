# -*- coding: utf-8 -*-
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import base64
from apiclient import errors, discovery
import sys

# If modifying these scopes, delete the file token.json.
SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.labels'
]
#<div style="width: 960px; height: 540px; background: #fff url('https://i.imgur.com/xc2iaiu.jpg'); text-align: center;">
new_html5 = """
<div style="width: 960px; height: 540px; background: #fff url('cid:image1'); text-align: center;">
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
 <h3 style="font: 1.25em Verdana, Arial, Helvetica, sans-serif; color: red; font-size: 20px; padding-bottom: em; letter-spacing: -1px;"><a href="http://ozon.ru">{}</a></h3>
</div>""".format(sys.argv[2])



html=('<html><body>' + new_html5 + '</body></html>')


imgpath = sys.argv[3]

def CreateMessage2(to):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Подарочный сертификат'
    msgRoot['From'] = 'xxxx@xxxx.com'
    msgRoot['To'] = to
    msgRoot.preamble = 'Lupa'
     
    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
     
    msgText = MIMEText('This email was sent from Python')
    msgAlternative.attach(msgText)
     
     
    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText(html, 'html')
    msgAlternative.attach(msgText)
     
    # This example assumes the image is in the current directory
    fp = open(imgpath, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
     
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    raw = base64.urlsafe_b64encode(msgRoot.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}
    return body

def sendMessage(to):
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        creds = None
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret2.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    msg = CreateMessage2(to)
    try:
        message = (service.users().messages().send(userId="me", body=msg).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

if __name__ == '__main__':
    sendMessage(sys.argv[1]) 
# [END gmail_quickstart]
