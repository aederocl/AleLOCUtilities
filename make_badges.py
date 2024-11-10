import string
import os
import sys

attendantsFile = open("participantsList.csv","r")
for index,eachLine in enumerate(attendantsFile):
    if index > 0:
        tmp = eachLine.strip().split(",")
        fullName = tmp[1][1:-1]
        affiliation = tmp[4][1:-1]

        name = fullName.split()[0]
        surname = fullName.replace(name,'')

        print(name,surname,affiliation)

        nameFile = open("name.txt","w")
        nameFile.write(name)
        nameFile.close()
        nameFile = open("name.txt","w")
        nameFile.write(name)
        nameFile.close()

        surnameFile = open("surname.txt","w")
        surnameFile.write(surname)
        surnameFile.close()
    
        affiliationFile = open("affiliation.txt","w")
        affiliationFile.write(affiliation)
        affiliationFile.close()
    
        os.system("pdflatex ID.tex ")
        command = 'mv ID.pdf ID_' + fullName.replace(' ','') + '.pdf'
        print(command)
        os.system(command)


attendantsFile.close()
os.system("rm *.aux")
os.system("rm *.log")

