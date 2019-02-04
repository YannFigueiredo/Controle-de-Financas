import classes
import pymysql as sql

usuario = classes.cadastro()

conexao = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database =  'controle_financas'
)

cursor = conexao.cursor()

#if cursor.execute('select count(id) from usuarios')-1 == 0:
usuario.definir_usuario()

