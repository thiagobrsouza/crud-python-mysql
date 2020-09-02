'''
Esse arquivo corresponde as conexões e querys ao banco de dados. Escolhemos utilizar o MySQL, já que trata-se
de um banco mais profissional usado em grande escala no mercado. Mas nada impede de usar o SQLITE.
'''
# importando o conector do mysql
import mysql.connector

# criação da classe Database para guardar a conexão e os métodos querys do banco de dados
class Database:
    def __init__(self, db_name):
        self.connect=mysql.connector.connect(
            host='localhost',
            user='goku',
            password='shenlong',
            database='company'
        )
        self.cursor=self.connect.cursor()


    # criando um novo usuário para acessar o sistema. Será chamado na função cria_usuario no arquivo login.py
    def cria_usuario(self, user, password):
        self.cursor.execute('INSERT INTO usuarios (user, password) VALUES (%s, %s)',
                            (user, password))
        self.connect.commit()


    # selecionando o usuário para poder acessar o sistema. Será chamado na função login no arquivo login.py
    def seleciona_login(self, user, password):
        self.cursor.execute('SELECT user, password FROM usuarios WHERE user= %s AND password= %s',
                            (user, password))
        return self.cursor.fetchone()


    # inserindo dados. Esse método será chamado pela função novo_registro do arquivo app.py
    def insert_db(self, fname, lname, cargo, salario):
        self.cursor.execute('INSERT INTO funcionarios (fname, lname, cargo, salario) VALUES (%s, %s, %s, %s)',
                            (fname, lname, cargo, salario))
        self.connect.commit()
        print('\n   ',self.cursor.rowcount, 'Registro gravado com sucesso!')


    # selecionando pelo nome e sobrenome. Esse método será chamado pela função consultar_registro e outras também
    def consulta_nome(self, fname, lname):
        self.cursor.execute('SELECT * FROM funcionarios WHERE fname= %s AND lname= %s ORDER BY fname',
                            (fname, lname))
        resultado=self.cursor.fetchall()
        print('\n   ', self.cursor.rowcount, 'total de registros encontrados!\n')
        for x in resultado:
            print('    ID Funcionário = ', x[0], )
            print('    Primeiro Nome  = ', x[1])
            print('    Último Nome    = ', x[2])
            print('    Cargo          = ', x[3])
            print('    Salário (R$)   = ', x[4], '\n')


    # consultando todos os dados do banco
    def consulta_todos(self):
        self.cursor.execute('SELECT * FROM funcionarios ORDER BY fname ASC')
        resultado = self.cursor.fetchall()
        print('\n   ', self.cursor.rowcount, 'total de registros encontrados!\n')
        for x in resultado:
            print('    ID Funcionário = ', x[0], )
            print('    Primeiro Nome  = ', x[1])
            print('    Último Nome    = ', x[2])
            print('    Cargo          = ', x[3])
            print('    Salário (R$)   = ', x[4], '\n')


    # editando o cargo após informar o funcionário. Esse método será chamado pela função editar_registro no app.py
    def edit_cargo(self, cargo, fname, lname):
        self.cursor.execute('UPDATE funcionarios SET cargo= %s WHERE fname= %s AND lname= %s',
                            (cargo, fname, lname))
        self.connect.commit()
        print('\n   ',self.cursor.rowcount, 'registro(s) atualizado(s)!')


    # editando o salário após informar o funcionário. Esse método será chamado pela função editar_registro no app.py
    def edit_salario(self, salario, fname, lname):
        self.cursor.execute('UPDATE funcionarios SET salario= %s WHERE fname= %s AND lname= %s',
                            (salario, fname, lname))
        self.connect.commit()
        print('\n   ',self.cursor.rowcount, 'registro(s) atualizado(s)!')


    # editando ambos cargo e salário. Esse método será chamado pela função editar_registro no app.py
    def edit_ambos(self, cargo, salario, fname, lname):
        self.cursor.execute('UPDATE funcionarios SET cargo= %s, salario= %s WHERE fname= %s AND lname= %s',
                            (cargo, salario, fname, lname))
        self.connect.commit()
        print('\n   ', self.cursor.rowcount, 'registro(s) atualizado(s)!')


    # excluindo um registro. Esse método será chamado pela função excluir_registro no app.py
    def delete_func(self, fname, lname):
        self.cursor.execute('DELETE FROM funcionarios WHERE fname= %s AND lname= %s',
                            (fname, lname))
        self.connect.commit()
        print('\n   ',self.cursor.rowcount, 'registro excluido com sucesso!')


    # fechando conexão com o banco de dados
    def close_db(self):
        self.connect.close()