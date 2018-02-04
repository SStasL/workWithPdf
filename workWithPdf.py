#! python3
# -*- coding: utf-8 -*-

# TODO: create a func, create a main func, run with main func

from PyPDF2 import PdfFileWriter, PdfFileReader
import io, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

os.chdir('D:\\pythonTemp')      #opening cwd



pdfFileObj = open("1936_exp.pdf", "rb")               # opening pdf
pdfReader = PdfFileReader(pdfFileObj)                   # creating pdf reader object
pdfWriter = PdfFileWriter()
allNumPages = str(pdfReader.numPages)
#print(pdfReader.numPages)                               # printing number of pages
for page in range(pdfReader.numPages):
    box = io.BytesIO()                                  # create buffer
    #print(str(page + 1) + ' from ' + allNumPages)
    c = canvas.Canvas(box)                              # create canvsc obj in the box
    c.drawString(100,800,str(str(page + 1) + ' from ' + allNumPages))   # filling the canvas obj
    c.save()                                                        # save the canvas obj
    box.seek(0)         # take 0 ofset
    canvasMark = PdfFileReader(box)     # read canvas obj to canvasMark
    p1 = pdfReader.getPage(page)        # get current page from the orig pdf
    p1.mergePage(canvasMark.getPage(0)) # merge with canvasMark (canvasMark iterated)
    pdfWriter.addPage(p1)               # add new page to pdfWriter obj



# finally, write "pdfWriter" to real file
newFile = open("dest.pdf", "wb")
pdfWriter.write(newFile)
newFile.close()
pdfFileObj.close()
