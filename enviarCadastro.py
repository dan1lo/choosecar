#!C:\\Python26\\python.exe -u
#-*- coding: ISO-8859-1 -*-
print "Content-type: text/html; ISO-8859-1"  
import cgi, os
import cgitb; cgitb.enable()
import MySQLdb
con = MySQLdb.connect('localhost', 'root', '') 
con.select_db('pythonweb')
cursor = con.cursor()

form = cgi.FieldStorage()


fileitem = form['file']
nome = form.getvalue("nome")
mail = form.getvalue("mail")
user = form.getvalue("username")
senha = form.getvalue("senha")
ano = form.getvalue("ano")
modelo = form.getvalue("modelo")
foto = ""

if fileitem.filename:

   fn = os.path.basename(fileitem.filename)
   foto = user+fn
   open('../choosecar/fotos/'+user+fn, 'wb').write(fileitem.file.read())

   message = fn
else:
   message = "oi"
voto=0
sql = "INSERT INTO user(nome,mail,user,senha,ano,modelo,foto,voto) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%i')" % (nome, mail, user, senha, ano, modelo, foto, voto)

import template
template.cabecalho()
print'''<body leftmargin=\"0\" topmargin=\"0\" marginwidth=\"0\" marginheight=\"0\" link=\"black\" alink=\"black\" vlink=\"black\">

		<div id="topoDentro" align="center"><img src="imagens/logo.jpg" width="379" height="87" border="0" /> </div>
		<font face=\"verdana\" size=\"1\">
		<br />"'''	

try:
	cursor.execute(sql)
	print "<div align='center'> Cadastro efetuado com sucesso! você será redirecionado...</div> <meta http-equiv='refresh' content='2;URL=index.py'></body></html>"
except MySQLdb.Error, e:
    print "<div align='center'><pre>Usuário já cadastrado</pre><meta http-equiv='refresh' content='2;URL=cadastro.py'></div></body></html>"
    exit(1)
