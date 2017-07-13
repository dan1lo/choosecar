#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-
print "Content-type: text/html; ISO-8859-1"  


def meio():
	print'''
	<script>
	function enviar(){
	
	if(document.dados.nome.value==""){
            alert("Preencha campo NOME corretamente!");
			document.dados.nome.focus();
			return false;
        }
		if( document.dados.mail.value=="" || document.dados.mail.value.indexOf('@')==-1 || document.dados.mail.value.indexOf('.')==-1 )
		{
		alert( "Preencha campo E-MAIL corretamente!" );
		document.dados.mail.focus();
		return false;
		}
	if( document.dados.username.value=="" )
		{
		alert( "Preencha campo Username" );
		document.dados.username.focus();
		return false;
		}
	if( document.dados.senha.value=="" )
		{
		alert( "Preencha campo senha" );
		document.dados.senha.focus();
		return false;
		}
	if( document.dados.ano.value=="" )
		{
		alert( "Preencha campo Ano" );
		document.dados.ano.focus();
		return false;
		}
	if( document.dados.modelo.value=="" )
		{
		alert( "Preencha campo Modelo" );
		document.dados.modelo.focus();
		return false;
		}
	
	return true;
	
	}
 
	</script>
	<div class="texto1" align="center">	                
	<table align ="center">
	<form action="enviarCadastro.py" method="post" name="dados" onSubmit="return enviar();" enctype="multipart/form-data">
		<tr><td>Nome:</td><td><input type="text" name="nome" id="nome" /></td></tr>
		<tr><td>E-mail:</td><td><input type="text" name="mail" /></td></tr> 
		<tr><td>User:</td><td><input type="text" name="username" /></td></tr>
		<tr><td>Senha:</td><td><input type="password" name="senha" /></td></tr>
		<tr><td>Ano:</td><td><input type="text" name="ano" /></td></tr> 
		<tr><td>Modelo:</td><td><input type="text" name="modelo" /></td></tr>
		<tr><td>Foto</td><td><input type="file" name="file" /></td></tr>
		<tr><td colspan=2><input type="submit" value="enviar" /></td></tr>
	</form>
	</table>
	</div>
	
	'''