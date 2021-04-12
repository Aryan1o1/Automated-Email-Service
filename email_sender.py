#smptblib is going to allow us to crete a smtp server i.e. if you send email you need an server/protocol to communicate
# As in website there is http or https to communicate
import smtplib
from email.message import EmailMessage


email = EmailMessage()
email['from'] = "Aryan Rastogi"
email['to'] = "ABC@gmail.com"
email['subject'] = "This is Sample Email"
email.set_content( "hello this is automated email generated statically")

with smtplib.SMTP(host="smtp.gmail.com",port =587) as smtp:
    smtp.ehlo() #.....This tell server is activated.
    smtp.starttls() #....Encryption mechanism
    smtp.login('XYZ@gmail.com',"Password")
    smtp.send_message(email)
    print("all good")
