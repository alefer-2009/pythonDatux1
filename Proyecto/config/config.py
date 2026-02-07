import sqlite3

class ConfigBd():
    def __init__(self):
        self.bd = self.createBd()
        self.createDatabase()
        self.bd = self.createBd()
        self.populate()

    def createBd(self):
        return sqlite3.connect('bd-si.db')

    def discontecBd(self):
        if self.bd:
            self.bd.close()

    def createDatabase(self):
        cursor = self.bd.cursor()
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios_sistema (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    nombre VARCHAR(100) NOT NULL,
                    apellido VARCHAR(100) NOT NULL,
                    tipo_usuario VARCHAR(20) NOT NULL,
                    estado BOOLEAN DEFAULT 1
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo_propiedad VARCHAR(50),
                    titulo VARCHAR(200),
                    precio DECIMAL(12,2),
                    estado VARCHAR(20)
                )
            ''')
            self.bd.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")

    def populate(self):
        cursor = self.bd.cursor()
        try:
            usuarios = [
                ('ana.torres@sistema.com', '1234', 'Ana', 'Torres', 'admin', 1),
                ('carlos.rivas@sistema.com', '1234', 'Carlos', 'Rivas', 'ventas', 1)
            ]
            cursor.executemany('INSERT OR REPLACE INTO usuarios_sistema (email, password, nombre, apellido, tipo_usuario, estado) VALUES (?,?,?,?,?,?)', usuarios)
            
            productos = [
                ('Departamento', 'Dpto Miraflores', 120000, 'disponible'),
                ('Casa', 'Casa Surco', 250000, 'disponible'),
                ('Oficina', 'Oficina San Isidro', 180000, 'disponible')
            ]
            cursor.executemany('INSERT OR REPLACE INTO productos (tipo_propiedad, titulo, precio, estado) VALUES (?,?,?,?)', productos)
            self.bd.commit()
        except Exception as e:
            print(f"Error: {e}")