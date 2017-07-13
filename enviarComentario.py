#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-
import cgi, Cookie
print "Content-type: text/html; ISO-8859-1"
form = cgi.FieldStorage()
nome = form.getvalue("nome")
mail = form.getvalue("mail")
comentario = form.getvalue("comentario")
id = form.getvalue("id")
flag="0"
import template

import MySQLdb
con = MySQLdb.connect('localhost', 'root', '') # faz a conexao
con.select_db('pythonweb')# seleciona o banco de dados
cursor = con.cursor()#prepara um objeto cursor

template.cabecalho()
sql = "INSERT INTO comentario(nome,mail,comentario,idUser,flag) VALUES ('%s', '%s', '%s', '%s','%s')" % (nome, mail, comentario, id, flag)
try:
	cursor.execute(sql)
	print "Comentario efetuado com sucesso! você será redirecionado... <meta http-equiv='refresh' content='2;URL=index.py'></body></html>"
except MySQLdb.Error, e:
    print "<pre>%s</pre></body></html>" % e
    exit(1)

