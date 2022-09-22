with open("ht.html","w") as g:
	g.write('''<html>
<head>
<tag> Test site <\ tag>
<body>
<\ body>
<\head>
<\html>
	'''
	)
	g.close()
	
	with open("ht.html") as f:
		print(f.read())
		