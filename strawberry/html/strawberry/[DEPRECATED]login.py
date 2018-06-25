#!/usr/bin/env python
#DEPRECATED
import cgi
form = cgi.FieldStorage() # instantiate only once!
#name = form.getfirst('name', 'empty')

# Avoid script injection escaping the user input
# name = cgi.escape(name)
print("""Content-type: text/html

<html>
<head>
  <title>LOGIN TO ANONYMOUS' iPHONE</title>
<style>
  .login{
    border:solid;
    border-radius:70px;
  }
body{/**background: linear-gradient(to left,5632E6,684CDA,5632E6);**/}
</style>
</head>
<body><center>
  <div id=login>
    <form method=get action="index.py">
    input session token<br><input type="text" name="token"><input type="submit" value="submit">
    </form>
  </div>
</div>
</center></body>
</html>
""")
