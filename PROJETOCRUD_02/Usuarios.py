import  mysql.connector
from Banco import Banco:

class usuarios(object):
    def __init__(self,idusuario=0,nome="",telefone="",email="",usuario="",senha=""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(("INSERT INTO usuario(nome, telefone, email, usuario, senha)VALUES(%s,%s,%s,%s,%s)",
            self.nome,self.telefone,self.email,self.usuario,self.senha))
            banco.conexao.commit()
            c.close()
            return "Usuario cadastrado com sucesso!"

        except Exception as e:
            return f"Ocorreu um erro na inserçao de usuario": {e}"

    def updateUser(self):
        banco = banco()
        try:
            c = banco.conexao.cursor()
            