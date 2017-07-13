<?php
$username = $_POST['username'];
$senha = $_POST['senha'];
$erro="";
setcookie("username",$username); setcookie("senha",$senha);
echo "<font face=verdana size=1>";
$conexao=mysql_connect ("localhost", "root", "") or die ('I cannot connect to the database because: ' . mysql_error());
mysql_select_db ("pythonweb") or die("não foi possivel");
$sql = "SELECT * FROM user where user='$username';";
$resultado = mysql_query($sql, $conexao);
$linhas = mysql_num_rows($resultado);
if($linhas==0)
	{
		$erro="Usuário não encontrado! $username";
		$erro="<BR><BR><BR><BR><p align=\"center\">Usuário <b>não</b> encontrado <b>Aguarde...</b></p><meta http-equiv='refresh' content='1;URL=index.py'>";
	}
else
	{
		if($senha!=mysql_result($resultado,0,"senha"))
		{
			$erro ="Senha está incorreta!<br>";
			$erro .="Não foi possivel o Login <meta http-equiv='refresh' content='2;URL='user.py'>";
		}		
		else if($senha==mysql_result($resultado,0,"senha"))
		{
			echo "<BR><BR><BR><BR><BR><p align=\"center\">Login Efetuado ! <b>Aguarde....</b></p><meta http-equiv='refresh' content='2;URL=paginauser.py'>";
		}
		else
		{
			$erro="erro: Contate o Desenvolvedor";
			$erro="<p aling=center><a href=index.py>Voltar</a></p>";
		}
	}	

if(!empty($erro)){
	echo $erro;
	}
mysql_close($conexao);
?>
