import smtplib, ssl

class EmailSender(object):
    smtp_server: str
    port: str
    sender_email: str
    password: str
    context: ssl

    def __init__(self, email, password) -> None:
        self.sender_email = email
        self.password = password
        self.smtp_server = "smtp.gmail.com"
        self.port = 465
        self.context = ssl.create_default_context()
    
    def send_email(self, msg, email):
        print("sending e-mail")
        print(self.smtp_server)
        receiver_email = email
        message = msg

        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, message)
    
    def create_email(self, subject, text):
        return 'Subject: {}\n\n{}'.format(subject, text).encode('utf-8')
