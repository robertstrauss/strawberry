#!/usr/bin/env python
import cgi
import hashlib
import base64
import glob
import math
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
token = form.getfirst('token', 'empty')
token = cgi.escape(token)
hash = hashlib.sha1()
hash.update(token)
hash = hash.hexdigest()
htmlpath = '../../html/strawberry/'
vpath = '../../strawberry/'
print("Content-type: text/html\n\n")
page = ""
with open(htmlpath + 'index.html', 'r') as indexhtml:
    index = indexhtml.read()
with open(htmlpath + 'login.html', 'r') as loginhtml:
    login = loginhtml.read()
with open(htmlpath + 'invalidlogin.html', 'r') as invloginhtml:
    invlog = invloginhtml.read()
with open(htmlpath + 'contenttemplate.html', 'r') as contenttemp:
    conttemp = contenttemp.read()
types = ['subservers', 'articles', 'games', 'other']
paths = {}
#names = {}
content = {}
for type in types:
    paths[type] = glob.glob(htmlpath+type+'/*')
    #names[type] = []
    #for item in paths[type]:
    #    names[type].append(item.split('/')[5])
    content[type] = "<table><tr>"
    count = 0
    if (len(paths[type]) == 0):
        content[type] = "<center style='line-height: 300px;'>Looks like you're the only one here</center>"
    for path in paths[type]:
        htmpth = "".join(path.split("/html"))
        with open(path + '/title.txt') as titletxt:
            title = titletxt.read()
        with open(path + '/description.txt') as desctxt:
            desc = desctxt.read()
        content[type] += conttemp%(htmpth, htmpth, title, title, desc)
        count += 1
        if (count % 4 == 0):
            content[type] += "</tr><tr>"
    content[type] += "</tr></table>"
index = index%(content[types[0]], content[types[1]], content[types[2]], content[types[3]])
with open(htmlpath + 'tokens.txt', 'r') as tokenstxt:
    if (hash in tokenstxt.read()):
        page += index
    elif (token == 'empty'):
        page += login
    else:
        page += invlog
print(page)
