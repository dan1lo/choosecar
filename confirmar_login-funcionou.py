#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-
import cgi, Cookie
print "Content-type: text/html; ISO-8859-1"
form = cgi.FieldStorage()
user = form.getvalue("username")
senha = form.getvalue("senha")
cookie = Cookie.SimpleCookie()
cookie["nome"] = user
cookie["senha"] = senha
import MySQLdb
con = MySQLdb.connect('localhost', 'root', '123') # faz a conexao
con.select_db('pythonweb')# seleciona o banco de dados
bla = con.cursor()#prepara um objeto cursor
sql = "SELECT * FROM user"
print '''Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head>
<title>Test PHP Script</title>
</head>
<body>
'''
try:
	bla.execute(sql)
	Results = bla.fetchall()
	total = len(Results)
	print "<pre>%s</pre></body></html>" %(total)
except MySQLdb.Error, e:
    print "<pre>%s</pre></body></html>" % e
    exit(1)