#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-

import Cookie
C = Cookie.SimpleCookie()
C["fig"] ="danilo"

try:

	print "Content-type: text/html; ISO-8859-1"  
	print'''
		<html>
			<head></head>
			<body>
			<table>
			%s
			<form action="enviarCadastro.py" method="post">
			<tr><td>Nome:</td><td><input type="text" name="nome" /></td></tr>
			<tr><td>E-mail:</td><td><input type="text" name="nome" /></td></tr> 
			<tr><td>User:</td><td><input type="text" name="nome" /></td></tr>
			<tr><td>Senha:</td><td><input type="password" name="nome" /></td></tr>
			<tr><td>Ano:</td><td><input type="text" name="nome" /></td></tr> 
			<tr><td>Modelo:</td><td><input type="text" name="nome" /></td></tr>
			<tr><td>Foto</td><td><input type=file name="images[]" /></td></tr>
			<tr><td colspan=2><input type="submit" value="enviar" /></td></tr>
		</form>
			</table>
			</body>

		</html>

		'''%(C["fig"].value)
except():
	print "erro"