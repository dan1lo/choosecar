#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-

def meio():
	import MySQLdb
	con = MySQLdb.connect('localhost', 'root', '') # faz a conexao
	con.select_db('pythonweb')# seleciona o banco de dados
	cursor = con.cursor()#prepara um objeto cursor
	sql = "SELECT * FROM user ORDER BY voto DESC LIMIT 0,10"

	try:
		cursor.execute(sql)
		Results = cursor.fetchall()
		num=0
		for linha in cursor:
			num = num+1
			print'''<div class="texto1">
					<img src="../choosecar/fotos/%s" width=300 height=300 /><br />
					<b>Posição:</b>%i <br />
					<b>Usuário:</b> %s <br />
					<b>Ano do carro:</b> %s <br />
					<b>Modelo:</b> %s<br />
					
					<b>Numero de votos</b>: %i<br/>
					</div>''' % (linha[7], num, linha[3], linha[5], linha[6], linha[8])
	except MySQLdb.Error, e:
		print "<pre>%s oi</pre></body></html>" % e
		exit(1)
	print'''<div class="texto1">	                
	
	</div>
	<div class="texto2">

	</div>
	
	'''