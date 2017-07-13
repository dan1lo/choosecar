#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-

import colunaLateral
import rodape
import colunaMeio

def cabecalho():
	print'''
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	
	<head>
	
		<meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
		<meta name="author" content="Danilo Monteiro" />
		<link href="estilos.css" rel="stylesheet" type="text/css" />
		<link href="fontes.css" rel="stylesheet" type="text/css" />
		<title>Choose Car</title>
	</head>
	'''
def bodyInicio():
	print'''
	<body>
		<div id="geral">
		<div id="topo">
		<div id="topoDentro" align="center"><img src="imagens/logo.jpg" width="379" height="87" border="0" /> </div>
    
		</div><!-- fim da div topo -->
		<div id="meio">
			<div id="coluna-lateral">'''
	colunaLateral.colunaLinks()	
	print'''
				
			</div><!--fim do div lateral -->
        <div id="coluna-meio">
        '''
	
def bodyFinal():
	print'''
        </div><!-- fim do div coluna-meio-->
		</div><!-- fim da div meio -->
		<div id="rodape">'''
	rodape.rodape()
	print'''
		</div><!-- fim da div rodape -->

		</div><!-- fim da div geral -->
		</body>
	</html>'''


