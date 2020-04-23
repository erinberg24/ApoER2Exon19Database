#!/usr/local/Python-3.7/bin/Python
import cgi
import cgitb
cgitb.enable()

print("Content-type:text/html\n")

print("""<html><title>LOGIN</title>
<header>Please login</header>
<body>""")

print("""<form action = "" method="post">
Username: <input type = "text" name="name"  required/><br />
Password: <input type = "text" name="password" reqired/><br />
<input type="submit" value="Submit" />
</form>""")


