#!C:\\Python26\\python.exe -u
#-*- coding: ISO-8859-1 -*-
import cgi
form = cgi.FieldStorage()
oi = form["produto"].value

try:	
	print '''Content-type: text/html

	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
	<html><head>
	<title>login</title>
	</head>
	<body> %s
	''' % (oi)
except:
	cgi.print_exception()