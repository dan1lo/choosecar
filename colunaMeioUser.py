#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-


def meioUser(nome):
	import MySQLdb
	con = MySQLdb.connect('localhost', 'root', '') # faz a conexao
	con.select_db('pythonweb')# seleciona o banco de dados
	cursor = con.cursor()#prepara um objeto cursor
	sql = "SELECT * FROM user where user='%s'" % nome
	sql2 = "SELECT * FROM comentario WHERE idUser = (select id FROM user where user='%s' ) and flag=0" % nome
	try:
		cursor.execute(sql)
		Results = cursor.fetchall()
		for linha in cursor:
			print'''
			<div align="center"><img src="../choosecar/fotos/%s" width=200 height=200 /></div><br>
			<div class="atualizarcadastro">	                
			<table align ="center">
			
			<form action="atualizarCadastro.py" method="post" enctype="multipart/form-data">
			<tr><td>Nome:</td><td><input type="text" name="nome" value="%s" /></td></tr>
			<tr><td>E-mail:</td><td><input type="text" name="mail" value="%s" /></td></tr> 
			<tr><td>Senha:</td><td><input type="password" name="senha" value="%s" /></td></tr>
			<tr><td>Ano:</td><td><input type="text" name="ano" value="%s" /></td></tr> 
			<tr><td>Modelo:</td><td><input type="text" name="modelo"value="%s" /></td></tr>
			<tr><td></td><td><input type="hidden" name="user" value="%s" /></td></tr>
			<tr><td colspan=2><input type="submit" value="enviar" /></td></tr>
			</form>
			</table>
			</div>''' % (linha[7], linha[1],linha[2],linha[4],linha[5],linha[6],nome)
		cursor.execute(sql2)
		Results = cursor.fetchall()
		print'''<div class="comentarios">'''
		for linha2 in cursor:
			print'''
					<form action ="aceitarRecados.py" method="post">
					<br />
					<b>Nome:</b> %s <br />
					<b>E-mail:</b> %s <br />
					<b>Comentário:</b> %s<br />
					Publicar <input type="radio" name="op" VALUE="op1" CHECKED>
					Deletar <input type="radio" name="op" VALUE="op2">
					<input type="hidden" name="id" value="%s">
					<input type="submit" value="ok">
					</form>
				''' %(linha2[1],linha2[2],linha2[3],linha2[0])
		print'''</div>'''	
	
	except MySQLdb.Error, e:
		print "<pre>%s</pre></body></html>" % e
		exit(1)
	