#smptblib is going to allow us to crete a smtp server i.e. if you send email you need an server/protocol to communicate
# As in website there is http or https to communicate
import smtplib
from email.message import EmailMessage
#This will use for substitution the variable's value by '$' sign
from string import Template
#This is like os package and its use it to access html file
from pathlib import Path


html=Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = "Aryan Rastogi"
email['to'] = "ABC@gmail.com"
email['subject'] = "This is Sample Email"
email.set_content(html.substitute({'name': "Elon"}),'html')

with smtplib.SMTP(host="smtp.gmail.com",port =587) as smtp:
    smtp.ehlo() #.....This tell server is activated.
    smtp.starttls() #....Encryption mechanism
    smtp.login('XYZ@gmail.com',"Password")
    smtp.send_message(email)
    print("all good")
