#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-
import cgi, Cookie
print "Content-type: text/html; ISO-8859-1"
form = cgi.FieldStorage()
id = form.getvalue("id")
import template
template.cabecalho()
print'''
		<html>
			<head></head>
			<body leftmargin=\"0\" topmargin=\"0\" marginwidth=\"0\" marginheight=\"0\" link=\"black\" alink=\"black\" vlink=\"black\">

		<div id="topoDentro" align="center"><img src="imagens/logo.jpg" width="379" height="87" border="0" /> </div>
		<font face=\"verdana\" size=\"1\">

			<div align='center'> 
			<table>		
				<form action="enviarComentario.py" method="post">
				<tr><td>Nome:</td><td><input type="text" name="nome" /></td></tr>
				<tr><td>E-mail:</td><td><input type="text" name="mail" /></td></tr> 
				<tr><td>Comentário</td><td><textarea name="comentario" rows="10" cols="23"></textarea> </td></tr>
				<tr><td colspan=2><input type="submit" value="enviar" /></td></tr>
				<input type="hidden" value="%s" name ="id">
				</form>
				
			</table>
			</div>
			</body>

		</html>

		'''%(id)