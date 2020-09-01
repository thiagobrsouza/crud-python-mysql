'''
Esse arquivo é o primeiro arquivo a ser executado, já que trata-se de uma tela de login.
Se tudo der certo, o arquivo main.py será chamado
'''
# importando a classe Database do arquivo database e também o responsável por controlar senhas
from database import Database
import main
import getpass

# instanciando o banco de dados utilizado lá no arquivo database.py
db=Database('company')

def tela_login():
    print('\n')
    print('    ############################################################################')
    print('    ###############                 CRUD-MYSQL                   ###############')
    print('    ###############              -- Tela Login --                ###############')
    print('    ############################################################################')
    print('    Para iniciar selecione uma das opções abaixo:')
    option=int(input('    1. Login\n    2. Novo usuário\n    --> '))
    if option == 1:
        login()
    elif option == 2:
        cria_usuario()
    else:
        print('    Opção inválida!')
        tela_login()


# função para realizar o login
def login():
    print('    ###### INSIRA SUAS CREDENCIAIS DE ACESSO ######')
    user=input('    Usuário: ')
    password=getpass.getpass('    Senha: ')
    tentativas=3
    while not db.seleciona_login(user, password):
        print('    Dados inválidos!\n')
        login()
    else:
        main.menu()


# função para criar um novo usuário no banco de dados
def cria_usuario():
    print('     ###### NOVO USUÁRIO ######')
    user=input('    Novo usuário: ')
    password=getpass.getpass('    Nova Senha: ')
    c_password=getpass.getpass('    Confirma Senha: ')
    if password != c_password:
        print('    Senhas não coincidem!\n')
        cria_usuario()
    elif password == c_password:
        db.cria_usuario(user, password)
        print('    Usuário registrado com sucesso!\n')
        tela_login()


# executando a função tela login quando o arquivo login é executado
if __name__ == '__main__':
    tela_login()