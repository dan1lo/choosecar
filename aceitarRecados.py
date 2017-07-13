#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-
import cgi, Cookie
print "Content-type: text/html; ISO-8859-1"
form = cgi.FieldStorage()
id = form.getvalue("id")
op = form.getvalue("op")
import template

import MySQLdb
con = MySQLdb.connect('localhost', 'root', '') # faz a conexao
con.select_db('pythonweb')# seleciona o banco de dados
cursor = con.cursor()#prepara um objeto cursor
if(op=='op1'):
	template.cabecalho()
	flag="1"
	sql = "UPDATE comentario SET flag='%s' where id= '%s' "%(flag,id)
	try:
		cursor.execute(sql)
		print "Comentario publicado com sucesso! você será redirecionado... <meta http-equiv='refresh' content='2;URL=paginauser.py'></body></html>"
	except MySQLdb.Error, e:
		print "<pre>%s</pre></body></html>" % e
		exit(1)
else:
	template.cabecalho()
	
	sql = "DELETE FROM comentario WHERE id='%s' " %(id)
	try:
		cursor.execute(sql)
		print "Comentario Deletado com sucesso! você será redirecionado... <meta http-equiv='refresh' content='2;URL=paginauser.py'></body></html>"
	except MySQLdb.Error, e:
		print "<pre>%s</pre></body></html>" % e
		exit(1)
