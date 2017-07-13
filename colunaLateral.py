#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-
import Cookie, os
cookie = Cookie.SimpleCookie()
def colunaLinks():
	try:
		cookie_string = os.environ.get('HTTP_COOKIE')
		cookies = os.environ['HTTP_COOKIE']
		cookies = cookies.split('; ')
		name = cookies[0].split('=')
		value = cookies[1].split('=')		
		if (name[1]== ""):
			valida = 1
		else:
			valida = 0
	except:
		valida = 0
	print'''
	<div id="coluna-lateral">
	<div><img src="img/menu.gif" ></div>
	&nbsp;&nbsp;<img src="imagens/seta.gif" ><a href="index.py">Home </a><br /> 
	&nbsp;&nbsp;<img src="imagens/seta.gif" ><a href="rank.py">Rank </a><br />'''
	if (valida == 1):
		print '''
		&nbsp;&nbsp;<img src="imagens/seta.gif" ><a href="user.py">Logar </a><br />
		&nbsp;&nbsp;<img src="imagens/seta.gif" ><a href="cadastro.py">Cadastrar </a><br />
		</div>
		<div class="lateral-anuncio">
                  <p>&nbsp;</p>
                  <p class="h1" align="center">ANÚNCIO</p>
                  <p>&nbsp;</p>
              	</div>
              	<div class="lateral-anuncio">
                  <p>&nbsp;</p>
                  <p class="h1" align="center">ANÚNCIO</p>
                  <p>&nbsp;</p>
              </div>
		</div><!--fim do div lateral -->
		<div id="coluna-lateral-linha"> &nbsp;</div>
		<div id="coluna-meio">
		'''

	else:
	
		print '''
		&nbsp;&nbsp;<img src="imagens/seta.gif" ><a href="paginauser.py">Pagina Pessoal </a><br />
		&nbsp;&nbsp;<img src="imagens/seta.gif" ><a href="logout.php">Sair </a><br />
		
		</div>
		<div class="lateral-anuncio">
                  <p>&nbsp;</p>
                  <p class="h1" align="center">ANÚNCIO</p>
                  <p>&nbsp;</p>
              	</div>
              	<div class="lateral-anuncio">
                  <p>&nbsp;</p>
                  <p class="h1" align="center">ANÚNCIO</p>
                  <p>&nbsp;</p>
              </div>
		</div><!--fim do div lateral -->
		<div id="coluna-lateral-linha"> &nbsp;</div>
		<div id="coluna-meio">
		'''
	print 