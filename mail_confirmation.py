import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import NoReturn

from logger import get_logger

logger = get_logger(__name__)


def send_confirmation_email(recipient, secret_code: int) -> NoReturn:
    """This is test account, you can use it if you want, before it deleted"""

    email = "hitehnik142.for.test@gmail.com"
    password = "fxppdpvnuxpawfnv"
    message = f"Hello! Your code is {secret_code}"

    msg = MIMEMultipart()
    msg["From"] = "hitehnik142.for.test@gmail.com"
    msg["To"] = recipient
    msg["Subject"] = "CatApp mail verification"
    msg.attach(MIMEText(message, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)

    text = msg.as_string()
    server.sendmail(email, recipient, text)
    logger.info(f"Code {secret_code} was sent to {recipient}")
    server.quit()
