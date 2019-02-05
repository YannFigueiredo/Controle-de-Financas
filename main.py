import classes
import pymysql as sql

usuario = classes.conta()

conexao = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'controle_financas'
)

cursor = conexao.cursor()

#if cursor.execute('select count(id) from usuarios')-1 == 0:
#usuario.cadastrar()

while True:
    print('_______________________________________________________________')
    print('\t\tPROGRAMA CONTROLE DE FINANÇAS')
    print('_______________________________________________________________')
    print('[1] Perfil do usuário\n[2] Registrar débito\n[3] Registrar crédito\n[4] Mostrar histórico de débito\n[5] Mostrar histórico de crédito\n[6] Alterar meta\n[7] Sair')
    op = int(input('Informe a opção: '))

    if op == 1:
        usuario.mostrar_conta()
    elif op == 2:
        x = usuario.getMeta()

        print(x)
    elif op == 3:
        print('')
    elif op == 4:
        print('')
    elif op == 5:
        print('')
    elif op == 6:
        print('')
    elif op == 7:
        print('Saindo...')
        break
    elif op < 1 or op > 7:
        print('Opção inválida!')

