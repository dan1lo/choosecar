#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-


def meio():
	import MySQLdb
	con = MySQLdb.connect('localhost', 'root', '') # faz a conexao
	con.select_db('pythonweb')# seleciona o banco de dados
	cursor = con.cursor()#prepara um objeto cursor
	sql = "SELECT * FROM user order by RAND() Limit 0,2"
	try:
		cursor.execute(sql)
		Results = cursor.fetchall()
		for linha in cursor:
			print'''<div class="texto1">
					<b>Usuário:</b> %s <br />
					<b>Ano do carro:</b> %s <br />
					<b>Modelo:</b> %s<br />
					<img src="../choosecar/fotos/%s" width=300 height=300 />
					<form action="voto.py" method="post">
						<input type="hidden" value="%s" name ="id">
						<button type="submit" class="enviar"> </button> 
						</form>
						<form action="comentario.py" method="post" target="_blank">
						<input type="hidden" value="%s" name ="id">
						<button type="submit" class="btComentario"> </button>
						</form>
						<form action="recados.py" method="post" target="_blank">
						<input type="hidden" value="%s" name ="id">
						<button type="submit" class="mural"> </button>
						</form>
				</div>''' % (linha[3], linha[5], linha[6], linha[7], linha[0], linha[0], linha[0])
			
	
	except MySQLdb.Error, e:
		print "<pre>%s</pre></body></html>" % e
		exit(1)