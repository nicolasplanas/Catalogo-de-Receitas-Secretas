from core.contato.contato import Contato
import sqlite3

class ContatoRepository:

    def __init__(self, db_path='dbReceitas.db'):

        self.conn             = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._criar_tabela()


    def _criar_tabela(self):

        query = '''
            CREATE TABLE IF NOT EXISTS contatos (
                id  INTEGER PRIMARY KEY,
                facebook TEXT,
                rede_x TEXT,
                instagram TEXT,
                linkedin TEXT,
                github TEXT
            )
        '''

        self.conn.execute(query)
        self.conn.commit()


    def salvar(self, contato: Contato):

        cursor = self.conn.cursor()

        if self.buscar_por_id(contato.id):

            cursor.execute("""
                UPDATE contatos
                SET github = ?, rede_x = ?, facebook = ?, linkedin = ?, instagram = ?
                WHERE id = ?
            """, (contato.github, contato.rede_x, contato.facebook, contato.linkedin, contato.instagram, contato.id))

        else:

            cursor.execute("""
                INSERT INTO contatos (id, github, rede_x, facebook, linkedin, instagram)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (contato.id, contato.github, contato.rede_x, contato.facebook, contato.linkedin, contato.instagram))
        
        self.conn.commit()


    def buscar_por_id(self, id):

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM contatos WHERE id = ?", (id,))
        row = cursor.fetchone()
        return Contato(**row) if row else None
    
