'''
O programa é divido em arquivos separados para melhor organização do ambiente.
Esse arquivo é o principal, onde carregamos o menu inicial do projeto e fazemos a importação do arquivo app que será
chamado toda vez que uma opção do menu principal for selecionada.
'''
# importando o arquivo app.py e suas funções, assim como a tela de login
import app
import login

# definição de menu principal dentro de uma função
def menu():
    print('\n')
    print('    ############################################################################')
    print('    ###############                BEM-VINDO AO                  ###############')
    print('    ###############                 CRUD-MYSQL                   ###############')
    print('    ###############            -- Menu Principal --              ###############')
    print('    ############################################################################')
    print('    1. Novo registro')
    print('    2. Consultar registro')
    print('    3. Editar um registro')
    print('    4. Excluir um registro')
    print('    5. Sair')
    option=int(input('    --> '))

    if option == 1:
        app.novo_registro()
    elif option == 2:
        app.consultar_registro()
    elif option == 3:
        app.editar_registro()
    elif option == 4:
        app.excluir_registro()
    elif option == 5:
        login.tela_login()
    else:
        print('    Opção Inválida!')
        exit()


# chamar a função menu ao executar o main.py
if __name__ == "__main__":
    menu()