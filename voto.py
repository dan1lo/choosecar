#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-
print "Content-type: text/html; ISO-8859-1"  
import MySQLdb
import cgitb; cgitb.enable()
import cgi
con = MySQLdb.connect('localhost', 'root', '') # faz a conexao
con.select_db('pythonweb')# seleciona o banco de dados
cursor = con.cursor()#prepara um objeto cursor	
form = cgi.FieldStorage()
id = form.getvalue("id")
id = int(id)
print '''Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head>
<title>Test PHP Script</title>
</head>
<body>
'''	
sql = "UPDATE user SET voto=voto+1 WHERE id='%i'" % (id)
try:
	cursor.execute(sql)
	Results = cursor.fetchall()
except MySQLdb.Error, e:
	print "<pre>%s</pre></body></html>" % e
	exit(1)
	
print '''<div align="center"><pre>Voto efetuado com sucesso! você será redirecionado... <meta http-equiv="refresh" content="2;URL=index.py"></pre></div>'''