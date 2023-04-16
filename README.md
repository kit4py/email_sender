# email_sender

The email_sender program is built on top of the Simple Mail Transfer Protocol (SMTP), making it easy for users to send emails to multiple recipients. Don't forget to customize the index.html template and add your credentials.

Installation:
1. git clone
2. cd email_sender/

Important:
In order to be able to send email you will need to get an App Password from Gmail:
1. Go to Google Accounts Page
2. Turn on the 2-step verification.
3. Security > App passwords https://i.stack.imgur.com/Vvl2H.png![image](https://user-images.githubusercontent.com/105520646/232308460-a5701487-0b35-431e-a8fa-4da26b7ff51b.png)
4. Select "Other apps" from the app menu.
5. Copy App Password and paste it to 'your_password'
6. Paste your email adress to 'your_email'



Prep:
1. Customize index.html for your needs
2. Customize email_sender.py (Subject, From, Login, App Password, Email List)

Usage:
1. python3 email_sender.py
