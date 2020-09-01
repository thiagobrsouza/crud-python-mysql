# crud-python-mysql
Um crud feito com python e mysql

Esse crud é feito 100% sem interface gráfica. É feito para quem está iniciando os estudos e dá uma boa noção sobre trabalhos com banco de dados.
O sistema é feito seguindo boas práticas com vários arquivos separados. São ao todo:

login.py,
main.py,
app.py,
database.py,
company_script_mysql

# Como funciona
O programa é um sistema para cadastro de funcionários em um sistema. Como bônus criei uma tela de login para o sistema.
Tudo começa com a página de login que vai lhe pedir um usuário ou para cadastrar um novo usuário.
Se tudo estiver correto, ele te envia a tela do menu inicial, onde você terá as opções de inserir, consultar, editar e excluir registros.

# Execução
Para que você realize a correta configuração do ambiente, siga os passos abaixo:

1. Instalar o Python no seu computador
2. Instalar o MySQL em seu computador
3. Crie uma pasta com o nome do projeto (ex: crud-mysql) e coloque todos os arquivos dentro dessa pasta.
4. Utilize o script company_script_mysql para criar o banco, o usuário, permissões e as tabelas com as quais iremos trabalhar.
5. Ao fim, basta apenas executar o arquivo login.py. Pode ser pelo CMD ou PowerShell:
      cd pasta\python login.py

Para fins de estudo, recomendo que você não cole os arquivos, escreva os códigos manualmente por mais trabalhoso que seja, assim você consegue gravar melhor.
