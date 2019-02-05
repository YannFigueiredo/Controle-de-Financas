import pymysql as sql

class conta:
    def abrir_database(self):
        self.conexao = sql.connect(
            host='localhost',
            user='root',
            passwd='',
            database='controle_financas'
        )

        return self.conexao

    def __init__(self):
        self.conexao = sql.connect(
            host = 'localhost',
            user = 'root',
            passwd = ''
        )

        self.cursor = self.conexao.cursor()

        self.cursor.execute("create database if not exists controle_financas")

        self.conexao.close()

        self.conexao = self.abrir_database()

        self.cursor = self.conexao.cursor()

        self.cursor.execute("create table if not exists usuarios(id int not null auto_increment primary key, nome varchar(50) not null, saldo float not null, meta float not null)default charset = utf8")

        self.cursor.execute("create table if not exists debito(id_deb int not null auto_increment primary key, descricao varchar(50), valor float not null, data date not null)default charset = utf8")

        self.cursor.execute("create table if not exists credito(id_cred int not null auto_increment primary key, descricao varchar(50), valor float not null, data date not null)default charset = utf8")

        self.conexao.close()

    def cadastrar(self):
        self.nome = input('Informe o nome do usuário: ')
        self.saldo = float(input('Informe o saldo: '))
        self.meta = float(input('Informe a meta: '))

        self.conexao = self.abrir_database()

        self.cursor = self.conexao.cursor()

        self.cursor.execute("insert into usuarios(id, nome, saldo, meta) values(default, '"+str(self.nome)+"','"+ str(self.saldo)+"','"+ str(self.meta)+"')")

        self.conexao.commit()

        self.conexao.close()

    def mostrar_conta(self):
        self.conexao = self.abrir_database()

        print('\nUsuário cadastrado:\n')

        self.cursor = self.conexao.cursor()

        self.cursor.execute('select * from usuarios')

        for x in self.cursor:
            print(x)

        self.conexao.close()

    def emitir_notificacao(self):
        print()

    def aviso_meta(self):
        print()

    def getSaldo(self):
        self.conexao = self.abrir_database()

        self.cursor = self.conexao.cursor()

        self.saldo = self.cursor.execute("select saldo from usuarios where id = '1'")

        return self.saldo

    def getMeta(self):
        self.conexao = self.abrir_database()

        self.cursor = self.conexao.cursor()

        self.cursor.execute("select meta from usuarios where id = '1'")

        self.meta = self.cursor.fetchall()

        for x in self.meta:
            self.valor = x[2]
        return self.valor




