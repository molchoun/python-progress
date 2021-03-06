import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Senya'
email['to'] = 'movsisian.arsen@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute(name='Dunduk'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('aramacht@gmail.com', "dummypassword123")
    smtp.send_message(email)
    print('All done!')
