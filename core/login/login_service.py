from core.login.login_repository import LoginRepository
from core.login.login import Login

class LoginService:

    def __init__(self):
        
        self.repository = LoginRepository()

    
    def autenticar(self, login: Login):

        usuario = self.repository.buscar_usuario_por_email(login.email)
        
        if not usuario:

            raise ValueError("Usuário não encontrado.")
        
        if usuario.senha != login.senha:

            raise ValueError("senha incorreta.")
        
        if usuario.situacao.lower() != "ativo":

            raise ValueError("Usuário inativo.")
        
        return usuario