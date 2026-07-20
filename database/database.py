import sqlite3
from datetime import datetime

class Database:

    def __init__(self):

        self.conexao = sqlite3.connect("routine_manager.db")

        self.cursor = self.conexao.cursor()

        self.criar_tabelas()

    def criar_tabelas(self):

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS compromissos (
                                
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                
                    nome TEXT NOT NULL
                )
            """)

            self.conexao.commit()

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS registros (
                                
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                
                    compromisso_id INTEGER NOT NULL,
                                
                    data TEXT NOT NULL,
                                
                    FOREIGN KEY (compromisso_id)
                    REFERENCES compromissos (id)
                )
            """)

            self.conexao.commit()

    def adicionar_compromisso(self, nome):

        self.cursor.execute(
            """
            INSERT INTO compromissos (nome)
            VALUES (?)
            """,
            (nome,)
        )

        self.conexao.commit()

    def listar_compromissos(self):

        self.cursor.execute(
            """
            SELECT id, nome
            FROM compromissos
            ORDER BY nome
            """
        )
        return self.cursor.fetchall()
    
    def remover_compromisso(self, id_compromisso):
         
         self.cursor.execute(
              """
              DELETE FROM compromissos
              WHERE id = ?
              """,
              (id_compromisso,)
         )

         self.conexao.commit()

    def registrar_conclusao(self, id_compromisso):
         
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                        
        self.cursor.execute(
             """
            INSERT INTO registros(
                compromisso_id,
                data
            )
            VALUES (?, ?)
             """,
            (id_compromisso, data)
        )

        self.conexao.commit()