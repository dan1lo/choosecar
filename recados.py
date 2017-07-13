#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-
import cgi

try:
	print "Content-type: text/html; ISO-8859-1"  
	import template
	import colunaLateral
	import colunaMeioRecados
	form = cgi.FieldStorage()
	id = form.getvalue("id")
	template.cabecalho()
	template.bodyInicio()
	colunaMeioRecados.meio(id)
	template.bodyFinal()
except:
	cgi.print_exception()
