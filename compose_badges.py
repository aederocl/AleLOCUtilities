import string
import os

os.system("ls ID_*.pdf > allIDs.lis")

latexMainFile = open("main.tex","w")

text1 = r'''
\documentclass{article}
\usepackage[left=0cm,right=1.0cm,top=1.0cm,bottom=1.0cm]{geometry}
\usepackage{graphicx}
\begin{document}
\noindent

'''

latexMainFile.write(text1)

allIDs = open("allIDs.lis","r")

for index,eachLine in enumerate(allIDs) :
	myCount = index + 1
	eachLine = eachLine.strip()
	text = r"""
\includegraphics[width=9.9cm]{"""
	latexMainFile.write(text + eachLine + "} ")
	text = r"""
\hspace{0cm}\includegraphics[width=9.9cm]{"""
	latexMainFile.write(text + eachLine + "} \n")
	latexMainFile.write("~\\\\~\\\\ \n")
	
	if myCount % 3 == 0 :
		latexMainFile.write("\\newpage")
		latexMainFile.write("~~\\newpage")

textEnd = r"""
\end{document}
"""

latexMainFile.write(textEnd)

#os.system("pdflatex main.tex")
