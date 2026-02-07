from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box
import pyfiglet
from config.config import ConfigBd
from usuarios.userservices import Login, WelcomeUser
from config.email import EmailService

console = Console()
config = ConfigBd()
conn = config.bd
emailService = EmailService()

def getMenu(conn):
    titulo = pyfiglet.figlet_format("DATUX INMO", font="slant")
    while True:
        console.clear()
        console.print(titulo, style="bold cyan")
        console.print(Panel("1. Login | 2. Salir", style="bright_blue"))
        
        op = Prompt.ask("Seleccione", choices=["1", "2"])
        if op == "1":
            u = Prompt.ask("Email")
            p = Prompt.ask("Password")
            data = Login(u, p, conn)
            if data:
                WelcomeUser(u, emailService, "Acceso Exitoso", f"Hola {u}, bienvenido al sistema.")
                if data['type_user'] == "admin":
                    console.print("[green]Sesion Admin[/green]")
                    console.input("Enter...")
                else:
                    getMenuSale(conn)
            else:
                console.print("[red]Error de credenciales[/red]")
                console.input("Enter...")
        else:
            break

def getMenuSale(conn):
    while True:
        console.clear()
        console.print(Panel("LISTA DE PROPIEDADES", style="blue"))
        tabla = Table(box=box.ROUNDED)
        tabla.add_column("ID")
        tabla.add_column("Tipo")
        tabla.add_column("Propiedad")
        tabla.add_column("Precio")
        
        cursor = conn.cursor()
        cursor.execute("SELECT id_producto, tipo_propiedad, titulo, precio FROM productos")
        for r in cursor.fetchall():
            tabla.add_row(str(r[0]), r[1], r[2], f"S/ {r[3]:,.2f}")
            
        console.print(tabla)
        if Prompt.ask("0. Volver", default="0") == "0": break

if __name__ == "__main__":
    getMenu(conn)