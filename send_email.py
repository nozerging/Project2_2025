import smtplib
from email_message import EmailMessage

#Set the sender email and password and recipient $DRi$
from_email_addr ="3906994157@qq.com"
from_email_pass ="superccs75"
to_email_addr ="1976729868@qq.com"

# Create a message object
msg = EmailMessage()

# Set the email body
body ="Hello from Raspberry Pi"
msg.set_content(body)

# Set sender and recipient
msg['From'] = from_email_addr
msg['To'] = to_email_addr

# Set your email subject
msg['Subject'] = 'TEST EMAIL'

# Connecting to server and sending email
# Edit the following line with your provider's SMTP server details
server = smtplib.SMTP('smtp.email.com', 587)

# Comment out the next line if your email provider doesn't use
server.starttls()
# Login to the SMTP server
server.login(from_email_addr, from_email_pass)
# Send the message
server.send_message(msg)

print('Email sent')

#Disconnect from the Server
server.guit()
