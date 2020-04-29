#!/usr/local/Python-3.7/bin/Python
import pymysql
import cgi
import cgitb

cgitb.enable()
print("Content-type:text/html\n")

print("<html><head>")
print("<title>Reference</title>")

print("<style>
body{font-family:"Times New Roman"; font-size:15px;}
#RPD{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: center;
    font-size: 20px;
}"

print("<h1>References</h1>)