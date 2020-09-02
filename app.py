'''
Esse arquivo carrega quase toda a lógica do nosso sistema. Nele estão as funções que são chamadas toda vez que uma
opção é selecionada no arquivo main
'''
# importando a classe Database do arquivo database.py
from database import Database
import main

# instanciando o banco de dados utilizado lá no arquivo database
db=Database('company')

# inserir um novo registro no banco de dados (INSERT)
def novo_registro():
    print('\n    ###### NOVO REGISTRO ######')
    fname=input('    Primeiro nome: ')
    lname=input('    Sobrenome: ')
    cargo=input('    Cargo: ')
    salario=float(input('    Salário: '))
    db.insert_db(fname, lname, cargo, salario)

# consultar um registro do banco de dados (SELECT)
def consultar_registro():
    print('\n    ###### CONSULTAR REGISTRO ######')
    option=int(input('    1. Consultar um\n    2. Consultar todos\n    --> '))
    if option == 1:
        fname=input('    Primeiro nome: ')
        lname=input('    Sobrenome: ')
        db.consulta_nome(fname, lname)
    elif option == 2:
        db.consulta_todos()
    else:
        print('    Opção Inválida!')
        consultar_registro()

# editar um registro no banco de dados
def editar_registro():
    print('\n    ###### EDITAR UM REGISTRO ######')
    fname=input('    Primeiro nome: ')
    lname=input('    Sobrenome: ')
    db.consulta_nome(fname, lname)
    option=int(input('    1. Editar cargo\n    2. Editar salário\n    3. Ambos\n    --> '))
    if option == 1:
        novo_cargo=input('    Novo cargo: ')
        db.edit_cargo(novo_cargo, fname, lname)
    elif option == 2:
        novo_salario=float(input('    Novo salário: '))
        db.edit_salario(novo_salario, fname, lname)
    elif option == 3:
        novo_cargo=input('    Novo cargo: ')
        novo_salario=float(input('    Novo salário: '))
        db.edit_ambos(novo_cargo, novo_salario, fname, lname)
    else:
        print('    Opção inválida!')

# excluir um registro do banco de dados
def excluir_registro():
    print('\n    ###### EXCLUIR UM REGISTRO ######')
    fname=input('    Primeiro nome: ')
    lname=input('    Sobrenome: ')
    db.consulta_nome(fname, lname)
    option=int(input('    1. Confirmar exclusão\n    2. Cancelar\n    --> '))
    if option == 1:
        db.delete_func(fname, lname)
    elif option == 2:
        exit()
    else:
        print('    Opção Inválida!')
        exit()