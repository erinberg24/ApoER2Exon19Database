#!/usr/local/Python-3.7/bin/python
import pymysql
import cgi
import cgitb
cgitb.enable()


print("Content-type: text/html\n")

print("<html><head>")
print("<title>Home Page</title>")

print("
<style>
    body{font-family:"Times New Roman"; font-size:15px;})