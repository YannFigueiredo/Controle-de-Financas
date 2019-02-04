import pymysql as sql

class cadastro:
    def __init__(self):
        self.conexao = sql.connect(
            host = 'localhost',
            user = 'root',
            passwd = ''
        )

        self.cursor = self.conexao.cursor()

        self.cursor.execute("create database if not exists controle_financas")

        self.conexao.close()

        self.conexao = sql.connect(
            host = 'localhost',
            user =  'root',
            passwd = '',
            database = 'controle_financas'
        )

        self.cursor = self.conexao.cursor()

        self.cursor.execute("create table if not exists usuarios(id int not null auto_increment primary key, nome varchar(50) not null, saldo float not null, meta float not null)default charset = utf8")

        self.cursor.execute("create table if not exists debito(id_deb int not null auto_increment primary key, descricao varchar(50), valor float not null, data date not null)default charset = utf8")

        self.cursor.execute("create table if not exists credito(id_cred int not null auto_increment primary key, descricao varchar(50), valor float not null, data date not null)default charset = utf8")

        self.conexao.close()

    def definir_usuario(self):
        self.nome = input('Informe o nome do usuário: ')
        self.saldo = float(input('Informe o saldo: '))
        self.meta = float(input('Informe a meta: '))

        self.conexao = sql.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            database =  'controle_financas'
        )

        self.cursor = self.conexao.cursor()

        self.cursor.execute("insert into usuarios(id, nome, saldo, meta) values(default, '"+str(self.nome)+"','"+ str(self.saldo)+"','"+ str(self.meta)+"')")

        self.conexao.commit()

        self.conexao.close()






