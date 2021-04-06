# Duo_login_alert_email_sender
Small program to automatically send out a email lockout alert.
Uses SendGrid API  to send an email SendGrid free acccount allows 100 emails per day.
Can upgrade to a paid account if more emails a day are being sent.

To run execute: 

**python3 Duo_app_loggin_email_sender.py**

Will need to contruct a .ini file in the cloned directory named 'API-params.ini'

[api_params]
ikey = 
skey = 
api-host = 
sendgrid_api_key = 
sendgrid_email_template = 
from_email = 
to_email = 

One. contructed can run the included 'encrypt' script to encrypt the config file.
Warning! - Once encrypted cannot be decrpted
