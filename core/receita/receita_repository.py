from core.receita.receita import Receita
import sqlite3

class ReceitaRepository:

    def __init__(self, db_path='dbReceitas.db'):
        
        self.conn             = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._criar_tabela()


    def _criar_tabela(self):

        query = '''
            CREATE TABLE IF NOT EXISTS receitas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_receita TEXT NOT NULL,
                ingredientes TEXT NOT NULL,
                modo_preparo TEXT NOT NULL,
                categoria TEXT NOT NULL
            )
        '''
        self.conn.execute(query)
        self.conn.commit()

    
    def salvar(self, receita: Receita):

        cursor = self.conn.cursor()

        if receita.id == 0:

            cursor.execute("""
                INSERT INTO receitas (nome_receita, ingredientes, modo_preparo, categoria)
                VALUES (?, ?, ?, ?)
            """, (receita.nome_receita, receita.ingredientes, receita.modo_preparo, receita.categoria))

        else:

            cursor.execute("""
                UPDATE receitas
                SET nome_receita=?, ingredientes=?, modo_preparo=?, categoria=?
                WHERE id=?
            """, (receita.nome_receita, receita.ingredientes, receita.modo_preparo, receita.categoria, receita.id))
            
        self.conn.commit()
    

    def listar_todas(self):

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM receitas")
        rows   = cursor.fetchall()
        return [Receita(**row) for row in rows]
    

    def buscar_por_id(self, id):

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM receitas WHERE id = ?", (id,))
        row    = cursor.fetchone()
        return Receita(**row) if row else None
    

    def remover_por_id(self, id):

        self.conn.execute("DELETE FROM receitas WHERE id=?", (id,))
        self.conn.commit()


    def filtrar_por_nome_e_categoria(self, nome=None, categoria=None):

        cursor = self.conn.cursor()
        query  = "SELECT * FROM receitas WHERE 1=1"
        params = []

        if nome:

            query += " AND (nome_receita LIKE ? OR ingredientes LIKE ? OR modo_preparo LIKE ?)"
            params.append(f"%{nome}%")
            params.append(f"%{nome}%")
            params.append(f"%{nome}%")

        if categoria:
            
            query += " AND categoria = ?"
            params.append(categoria)

        cursor.execute(query, params)
        rows = cursor.fetchall()
        return [Receita(**row) for row in rows]