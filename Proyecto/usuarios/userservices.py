from sqlite3 import Connection
from config.email import EmailService

def Login(email, password, conn):
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM usuarios_sistema WHERE email = ?"
        result = cursor.execute(query, (email,)).fetchone()
        if result:
            if password == result[2]:
                return {"user": result[1], "type_user": result[5], "login": True}
        return False
    except Exception:
        return False

def WelcomeUser(email, emailService, asunto, mensaje):
    try:
        emailService.send_email(email, asunto, mensaje)
    except Exception:
        pass