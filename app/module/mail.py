# -*- coding: utf-8 -*-
from smtplib import SMTP_SSL
from email.mime.text import MIMEText


from conf import conf


def send(to_address: str, message: str, title: str = "메일 인증 키"):
    with SMTP_SSL(host=conf['smtp']['host'], port=int(conf['smtp']['port'])) as client:
        client.login(
            user=conf['smtp']['user'],
            password=conf['smtp']['password']
        )

        msg = MIMEText(f"<h1>{message}</h1>", "html", "utf-8")
        msg['Subject'] = title

        client.sendmail(
            from_addr=conf['smtp']['user'],
            to_addrs=[to_address],
            msg=msg.as_string()
        )
