#!C:\\Python26\\python.exe -u
#-*- coding: ISO-8859-1 -*-
print "Content-type: text/html; ISO-8859-1"  
import cgi, os
import cgitb; cgitb.enable()
import MySQLdb
con = MySQLdb.connect('localhost', 'root', '') # faz a conexao
con.select_db('pythonweb')# seleciona o banco de dados
cursor = con.cursor()#prepara um objeto cursor

form = cgi.FieldStorage()

# Get filename here.
nome = form.getvalue("nome")
mail = form.getvalue("mail")
senha = form.getvalue("senha")
ano = form.getvalue("ano")
modelo = form.getvalue("modelo")
user = form.getvalue("user")
sql = "UPDATE user SET nome='%s',mail='%s',senha='%s',ano='%s',modelo='%s' where user= '%s' " % (nome, mail, senha, ano, modelo,user)

import template
template.cabecalho()
	

try:
	cursor.execute(sql)
	print nome
	print mail
	print senha
	print ano
	print modelo 
	print user
	print "Atualização efetuada com sucesso! você será redirecionado... <meta http-equiv='refresh' content='2;URL=paginauser.py'></body></html>"
except MySQLdb.Error, e:
    print "<pre>%s</pre></body></html>" % e
    exit(1)
