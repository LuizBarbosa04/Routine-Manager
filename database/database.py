import sqlite3


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