class Banco():
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pedro_db"
        )
        self.create.Table()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute('''CREATE TABLE IF NOT EXIST usuario(idusuario INT AUTO INCREMENT PRIMARY KEY,)
        nome VARCHAR(255),
        telefone VARCHAR(255),
        email VARCHAR(255),
        usuario VARCHAR(255),
        senha VARCHAR(255)
        )''')
        self.conexao.commit()
        c.close()
        