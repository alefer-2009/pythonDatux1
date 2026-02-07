import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailService:
    def __init__(self):
        self.smtp_server = "sandbox.smtp.mailtrap.io"
        self.smtp_port = 2525
        self.username = "29820646eeb8eb"
        self.password = "298f6a0f84e21e"
        self.sender_email = "sistema@datux.com"
        self.sender_name = "Sistema Inmobiliario DATUX"
    
    def send_email(self, to_email, subject, message):
        try:
            msg = MIMEMultipart()
            msg['From'] = f"{self.sender_name} <{self.sender_email}>"
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.login(self.username, self.password)
                server.sendmail(self.sender_email, to_email, msg.as_string())
            return True
        except Exception:
            return False