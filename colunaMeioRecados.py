#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-


def meio(id):
	import MySQLdb
	con = MySQLdb.connect('localhost', 'root', '') # faz a conexao
	con.select_db('pythonweb')# seleciona o banco de dados
	cursor = con.cursor()#prepara um objeto cursor
	sql = "SELECT * FROM user where id='%s'" % id
	sql2 = "SELECT * FROM comentario WHERE idUser ='%s' and flag=1" % id
	try:
	
		cursor.execute(sql)
		Results = cursor.fetchall()
		for linha in cursor:
			print''' <div align="center">Mural de recados de <b>%s</b><div> 
			<div align="center"><img src="../choosecar/fotos/%s" width=200 height=200 /></div><br>'''% (linha[1], linha[7])
		cursor.execute(sql2)
		Results = cursor.fetchall()
		print'''<div class="comentarios">'''
		for linha2 in cursor:
			print'''
					<br />
					<b>Nome:</b> %s <br />
					<b>E-mail:</b> %s <br />
					<b>Comentário:</b> %s<br />
				''' %(linha2[1],linha2[2],linha2[3])
		print'''-----------------------------</div>'''	
	
	except MySQLdb.Error, e:
		print "<pre>%s</pre></body></html>" % e
		exit(1)
	