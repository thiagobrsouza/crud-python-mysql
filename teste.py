import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='arit',
    password='@rit2020',
    database='teste'
)

cursor = db.cursor()

def inserir(nome, idade, peso):
    cursor.execute('INSERT INTO pessoas (nome, idade, peso) VALUES (%s, %s, %s)',
                   (nome, idade, peso))
    db.commit()

def consulta():
    cursor.execute('SELECT id, nome, idade, peso FROM pessoas')
    for titulo in cursor:
        print('ID -- Nome -- Idade -- Peso')
    for (id, nome, idade, peso) in cursor:
        print(id, nome, idade, peso)

opcao= int(input('1. Novo registro\n2. Consulta\n--> '))
if opcao == 1:
    nome = input('Nome: ')
    idade = input('Idade: ')
    peso = float(input('Peso: '))
    inserir(nome, idade, peso)

if opcao == 2:
    consulta()