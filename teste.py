#!C:\\Python26\\python.exe -u
#-*- coding: ISO-8859-1 -*-

print '''Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head>
<title>login</title>
<script language="javascript">
function createCookie(name,value,days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        var expires = "; expires="+date.toGMTString();
    }
    else var expires = "";
    document.cookie = name+"="+value+expires+"; path=/";
}
</script>
</head>
<body><a href="teste2.py?produto=1" onclick="createCookie('oi',3,3)">Clique aqui</a>

'''