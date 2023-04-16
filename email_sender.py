# email sender
# you can use it as a email marketing tool
# don't forget to customize the html file

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

print('''
█▀▀ █▀▄▀█ ▄▀█ █ █░░ █▀ █▀▀ █▄░█ █▀▄ █▀▀ █▀█
██▄ █░▀░█ █▀█ █ █▄▄ ▄█ ██▄ █░▀█ █▄▀ ██▄ █▀▄
''')

# your email list
email_list = ['email@0.com',
              'email@1.com',
              'email@2.com'
              ]

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # connect securely to the server
    smtp.login('your_email', 'your_password')

    for mail in email_list:
        html = Template(Path('index.html').read_text())
        email = EmailMessage()
        email['from'] = 'your name'
        email['to'] = mail
        email['subject'] = 'your Subject'
        # you can create a dict with users and send each one an individual mail
        email.set_content(html.substitute({'name': 'User1'}), 'html')
        print(f'sent to {mail}')

        smtp.send_message(email)
    print('all completed!')
