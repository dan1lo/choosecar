import MySQLdb
con = MySQLdb.connect('localhost', 'root', '') # faz a conexao
con.select_db('pythonweb')# seleciona o banco de dados
bla = con.cursor()#prepara um objeto cursor
