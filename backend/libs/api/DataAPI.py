import sqlite3 as sql

class DataGeren():
    def __init__(self) -> None:
        self.database = "backend/libs/data/database.db"
        self.connection = None
        self.cursor = None
    
    def conectar(self) -> None:
        self.connection = sql.connect(self.database)
        self.cursor = self.connection.cursor()

    def desconectar(self) -> None:
        self.connection.close()
        
    def criarTabelas(self) -> None:
        self.conectar()
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS faculdades (
            faculdade TEXT PRIMARY KEY UNIQUE,
            sigla TEXT NOT NULL
            );""")
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS notas (
            faculdade TEXT PRIMARY KEY NOT NULL,
            sigla TEXT NOT NULL,
            curso TEXT NOT NULL,
            concorrencia TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
            );""")
            
        self.connection.commit()
        self.desconectar()

if __name__ == '__main__':
    pass