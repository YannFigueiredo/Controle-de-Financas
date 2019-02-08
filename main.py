import classes
import pymysql as sql

usuario = classes.conta()
oper = classes.operacao()

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
    print('_'*60)
    print('\t\t\t\tCONTROLE DE FINANÇAS')
    print('_'*60)
    print('[1] Perfil do usuário\n[2] Registrar débito\n[3] Registrar crédito\n[4] Mostrar histórico de débito\n[5] Mostrar histórico de crédito\n[6] Alterar meta\n[7] Sair')
    op = int(input('Informe a opção: '))
    print('_'*60)

    if op == 1:
        usuario.mostrar_conta()
    elif op == 2:
        desc = input('Informe a descrição: ')
        valor = input('Informe o valor: ')
        data = input('Informe a data(ano-mês-dia): ')
        oper.ajustar_valor_deb(desc, valor, data)
    elif op == 3:
        desc = input('Informe a descrição: ')
        valor = input('Informe o valor: ')
        data = input('Informe a data(ano-mês-dia): ')
        oper.ajustar_valor_cred(desc, valor, data)
    elif op == 4:
        oper.historico_deb()
    elif op == 5:
        oper.historico_cred()
    elif op == 6:
        nova_meta = input('Informe a nova meta: ')
        usuario.alterar_meta(nova_meta)
    elif op == 7:
        print('Saindo...')
        break
    elif op < 1 or op > 7:
        print('Opção inválida!')

