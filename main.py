import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main():
    from_email = ""
    email_list = ["", ""]
    password = ""



    message = MIMEMultipart()
    message["From"] = from_email
    message["Subject"] = input("Введите описание для сообщения\n")

    body = input("Введите текст для сообщения\n")

    message.attach(MIMEText(body, "plain"))


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, password)


    to_email = ", ".join(email_list)
    print(to_email)
    server.sendmail(from_email, to_email, message.as_string())

    server.quit()


if __name__ == '__main__':
    main()