#!/usr/local/Python-3.7/bin/Python
import cgi
import cgitb

cgitb.enable()
print("Content-type:text/html\n")

print("<html><head>")
print("<title>Help</title>")

print("<style>
body{font-family:"Times New Roman"; font-size:15px;}
#home{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: center;
    font-size: 20px;
    }
#search{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: center;
    font-size: 20px;
    }
#visual{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: center;
    font-size: 20px;
    }
#ref{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: center;
    font-size: 20px;
    }
</style></head>")

print("<body
<h1>Help</h1>

")