class Receita:

    def __init__(self, id=0, categoria="", nome_receita="", ingredientes="", modo_preparo=""):
        
        self.id           = id
        self.categoria    = categoria
        self.nome_receita = nome_receita
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo