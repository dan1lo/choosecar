#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-
import cgi, Cookie
print "Content-type: text/html; ISO-8859-1"
form = cgi.FieldStorage()
user = form.getvalue("username")
senha = form.getvalue("senha")
cookie = Cookie.SimpleCookie()

import MySQLdb
con = MySQLdb.connect('localhost', 'root', '') # faz a conexao
con.select_db('pythonweb')# seleciona o banco de dados
cursor = con.cursor()#prepara um objeto cursor
sql = "SELECT * FROM user WHERE nome = '%s' and senha = '%s'" % (user, senha)
print '''Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head>
<title>login</title>
</head>
<body>
'''
try:
	cursor.execute(sql)
	Results = cursor.fetchall()
	total = len(Results)
	if (total>0):
		print 'Set-Cookie: meucookie=%s'%(user)
		cookie['meucookie']= user
		print cookie
		print "<pre>Senha correta! você será redirecionado... <meta http-equiv='refresh' content='2;URL=paginauser.py'></pre></body></html>"
	else:	
		print "<pre>Senha errada! Não foi possivel o Login, você será redirecionado... <meta http-equiv='refresh' content='2;URL=user.py'></pre></body></html>"
except MySQLdb.Error, e:
    print "<pre>%s</pre></body></html>" % e
    exit(1)