import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

email_list = []
with open('emails.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        email_list.append(row[0])

def main():
    from_email = "kirillbazaroff@gmail.com"
    # https://support.google.com/accounts/answer/185833?hl=ru - как получить пароль
    password = os.getenv('EMAIL_PASSWORD')

    message = MIMEMultipart()
    message["From"] = from_email
    message["Subject"] = input("Введите тему письма: ")

    body = input("Введите текст письма: ")
    message.attach(MIMEText(body, "plain"))

    # Load email list from CSV file
    email_list = []
    with open('emails.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            email_list.append(row[0])

    to_email = email_list

    # Send email to all addresses in the email list
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())


if __name__ == '__main__':
    main()

