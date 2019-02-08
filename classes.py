import pymysql as sql

class conta:
    def abrir_database(self): #Faz a conexão  com o banco de dados do servidor local
        self.conexao = sql.connect(
            host='localhost',
            user='root',
            passwd='',
            database='controle_financas'
        )

        return self.conexao

    def __init__(self): #Construtor(Define banco de dados e tabelas)
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

        print('Usuário cadastrado:\n')

        self.cursor = self.conexao.cursor()

        self.cursor.execute('select * from usuarios')

        for x in self.cursor:
            self.nome = x[1]
            self.saldo = x[2]
            self.meta = x[3]
            print('Nome: {} - Saldo: R${} - Meta: R${}'.format(self.nome, self.saldo, self.meta))

        self.conexao.close()

    def emitir_notificacao(self):
        print()

    def aviso_meta(self):
        print()

    def getSaldo(self):
        self.conexao = self.abrir_database()

        self.cursor = self.conexao.cursor()

        self.cursor.execute("select saldo from usuarios where id = '1'")

        for x in self.cursor:
            self.saldo = x[0]

        return float(self.saldo)

    def getMeta(self):
        self.conexao = self.abrir_database()

        self.cursor = self.conexao.cursor()

        self.cursor.execute("select meta from usuarios where id = '1'")

        for x in self.cursor:
            self.meta = x[0]

        return float(self.meta)

    def alterar_meta(self, nova_meta):
        self.conexao = self.abrir_database()

        self.cursor = self.conexao.cursor()

        self.cursor.execute("update usuarios set meta = '"+nova_meta+"' where id = '1'")

        self.conexao.commit()

        print('\nMeta alterada com sucesso!')


class operacao(conta):
    def ajustar_valor_cred(self, desc, valor, data):
        self.conexao = self.abrir_database()

        self.cursor = self.conexao.cursor()

        self.cursor.execute("insert into credito(id_cred, descricao, valor, data) values(default, '"+desc+"', '"+valor+"','"+data+"')")

        self.cursor.execute("select saldo from usuarios where id = '1'")

        for x in self.cursor:
            self.novo_saldo = x[0]

        self.novo_saldo = self.novo_saldo + float(valor)

        self.cursor.execute("update usuarios set saldo = '" + str(self.novo_saldo) + "' where id = '1'")

        self.conexao.commit()

        self.conexao.close()

    def ajustar_valor_deb(self, desc, valor, data):
        self.conexao = self.abrir_database()

        self.cursor = self.conexao.cursor()

        self.cursor.execute("insert into debito(id_deb, descricao, valor, data) values(default, '" + desc + "', '" + valor + "','" + data + "')")

        self.cursor.execute("select saldo from usuarios where id = '1'")

        for x in self.cursor:
            self.novo_saldo = x[0]

        self.novo_saldo = float(self.novo_saldo) - float(valor)

        self.cursor.execute("update usuarios set saldo = '" + str(self.novo_saldo) + "' where id = '1'")

        self.conexao.commit()

        self.conexao.close()

    def historico_deb(self):
        self.conexao = self.abrir_database()

        self.cursor = self.conexao.cursor()

        self.cursor.execute("select descricao, valor, data from debito")

        print('Histórico de débito:\n')

        for x in self.cursor:
            self.desc = x[0]
            self.val = x[1]
            self.dat = x[2]

            print("Descrição: {} - Valor: RS{} - Data: {}".format(self.desc, self.val, self.dat))

    def historico_cred(self):
        self.conexao = self.abrir_database()

        self.cursor = self.conexao.cursor()

        self.cursor.execute("select descricao, valor, data from credito")

        print('Histórico de crédito:\n')

        for x in self.cursor:
            self.desc = x[0]
            self.val = x[1]
            self.dat = x[2]

            print("Descrição: {} - Valor: RS{} - Data: {}".format(self.desc, self.val, self.dat))




