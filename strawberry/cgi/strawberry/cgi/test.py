


#!/usr/bin/python


import cgi


import glob


import cgitb; cgitb.enable()


print ("Content-type: text/html")


print ("")


print("""
<html>
<head>
</head>
<body>
""")


for item in range(0, len(glob.glob('/*'))):
    print(glob.glob('/*')[item])


print("""
</body>
</html>
""")
