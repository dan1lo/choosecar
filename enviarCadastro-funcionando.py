#!C:\\Python26\\python.exe -u
#-*- coding: ISO-8859-1 -*-
import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

try:
	import msvcrt,os
	msvcrt.setmode( 0, os.O_BINARY ) # stdin  = 0
	msvcrt.setmode( 1, os.O_BINARY ) # stdout = 1
except ImportError:
	pass

# Get filename here.
fileitem = form['file']
# Test if the file was uploaded
if fileitem.filename:

   fn = os.path.basename(fileitem.filename)
   open('../choosecar/fotos/' + fn, 'wb').write(fileitem.file.read())

   message = 'A imagem "' + fn + '" foi enviada'
   
else:
   message = 'No file was uploaded'
   
print '''\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
'''% (message)