#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-
import cgi, Cookie, os
cookie = Cookie.SimpleCookie()
try:
	cookie_string = os.environ.get('HTTP_COOKIE')	
	cookie.load(cookie_string)
	cookies = os.environ['HTTP_COOKIE']
	cookies = cookies.split('; ')
	name = cookies[0].split('=')
	value = cookies[1].split('=')
	print "Content-type: text/html; ISO-8859-1"  
	import template
	import colunaLateral
	import colunaMeioUser
	template.cabecalho()
	template.bodyInicio()
	colunaMeioUser.meioUser(name[1])
	template.bodyFinal()
except:
	cgi.print_exception()
