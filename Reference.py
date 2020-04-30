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
#des{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: left;
    font-size: 20px;
    }
#RPD{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: left;
    font-size: 20px;
    }
#ncbi{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: left;
    font-size: 20px;
    }
#onto{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: left;
    font-size: 20px;
    }
#affy{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: left;
    font-size: 20px;
    }
</style></head>")

print("<body>
<h1>References</h1>

<div id = des><p>
We would like to recognize these free and open source databases that allowed us to search through useful information about the mouse genome in order to succesfully complete this project. 
To access these helpful websites, please click on "Reactome Pathway Database", "NCBI", "Gene Ontology", and "Affymetrix". These links will automatically connect and open 
a new browser tab to their respective websites.</p></div>

<div id = RPD><p>
For the reactome website, we can quickly search through the reaction, protein, and pathway. There is a list of categories users can search by but
if the users know exactly which species, type, or compartments they are looking for, then the resulting output will be significantly reduced.</p></div>

<div id = ncbi><p>
In the NCBI website, the popularly used resources are on the right-hand side of the webpage. By clicking on gene, the system will link to the search gene page, and
users can then search for a particular gene symbol.</p></div>

<div id = onto><p>
The website allows us to add the gene ID while selecting for the biological process or molecular function for a specific species. By clicking on "launch", the 
search result will pop-up.</p></div>

<div id = affy><p>
By clicking on the affymetrix website, the system will connect to the homepage website. Once the "Affymetrix microarray data analysis" is clicked, there will be a search box which allows  
users to search for the affymetrix id. The users can then simply click on "Gene expression assays" and the results will appear.</p></div>

<a href ="https://reactome.org/" target="_blank">Reactome Pathway Database</a>

<a href = "https://www.ncbi.nlm.nih.gov/" target="_blank">NCBI</a>

<a href = "http://geneontology.org/" target="_blank">Gene Ontology</a>

<a href = "http://www.affymetrix.com/products/arrays/index.affx" target="_blank">Affymetrix</a>

</body>")

print("</html>")
