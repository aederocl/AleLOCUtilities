# AleLOCUtilities

Here is a series of scripts to prepare badges and participation certificates for conferences which I created over the years.

To begin with you should have a banner and the scanned signature of the chair of the Local Organising Committee.
I try to have the banner with a 4:1 aspect ratio and at least 900pixels wide.

For this example, they are:
* GenericMeeting.png
* Leonardo_Da_Vinci.png

The list of participants is a csv file. The important field is the name of the participant which should be the second column of the file and the affiliation should be the fifth.

The badges are created with a tex file called ID.tex
You should change:
* the name of the banner
* the size of the badge (if needed)

The Python scripts should run without modifications:
python make_badges.py
python compose_badges.py
finally you should run a pdflatex main.tex
(I do not know why this does not run properly in the Python script)
The resulting main.pdf file should have the badges in pairs, so that you can have them side by side, you can cut it, fold it and you have a badge which is identical in both front and back.

The certificates are generated with a tex file called certificate.tex
You should change:
* the name of the banner
* the name of the file with the signature
* the name of the chair of the LOC (as well as the text coming with it)
* the text of the certificate

The Python script should run without modifications:
python makeCertificates.py

The script will create certificates (as pdf files), named "NameSurname.pdf" in the same directory where the script is executed.

I am sure that the program can be further improved.
For ideas and suggestions, please, email: aederocl.astro@gmail.com

## Dependencies

* pdflatex
* Python 3.9 (or more)

## to be added:
* script to make badges
