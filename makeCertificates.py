#import string
import os
#import sys

attendantsFile = open("participantsList.csv","r")
for index,eachLine in enumerate(attendantsFile):
    if index > 0:
        tmp = eachLine.strip().split(",")
        name = tmp[1][1:-1]    
        nameFile = open("name.txt","w")
        nameFile.write(name)
        nameFile.close()
        os.system("pdflatex certificate.tex ")
        command = 'mv certificate.pdf ' + name.replace(' ','') + '.pdf'
        print(command)
        os.system(command)

attendantsFile.close()

os.system("rm *log")
os.system("rm *aux")
