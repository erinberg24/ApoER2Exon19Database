#!/usr/local/Python-3.7/bin/Python
import pymysql
import sys
import cgi
import cgitb
cgitb.enable()

def header():
    print("Content-type:text/html\n")

    print("""<html><head>
    <title>LOGIN</title>
    <style>
        body{font-family:"Times New Roman"; font-size:15px;}
        #login{
            border-style:ridge;
            border-color:#fa8072;
            padding: 15px;
            text-align: center;
            font-size: 20px;
        }
    </style></head>
    """)

def log_in():
    print("""<div id = login>
    <h1>Please login</h1>
    <form method="POST" action="" id=login_form>
    <p>Username: <input type = "text" name="name"  required/></p>
    <p>Password: <input type = "text" name="password" reqired/></p>
    <p> <input type="submit" value="Submit"> </p>
    </form></div>""")

form = cgi.FieldStorage()
if form:
    header()
    try:
        name = str(form.getvalue("Username"))
        pwd = str(form.getvalue("Password"))

        pwdbin = password.encode()
    header()
    print("<meta http-equiv="refresh" content="0")
    </head>
    <body>")

else:
    print("</head><center><font color = "red"><h2>Please Try again</h2></font></center>")
    login()

except Exception as exc:
    print("Error:", str(e))

else:
    header()
    login()

print("</body></html>")