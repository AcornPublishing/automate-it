__author__ = 'Chetan'

import PyPDF2
from PyPDF2 import PdfFileReader

pdf = open("diveintopython.pdf", 'rb')
readerObj = PdfFileReader(pdf)
print "PDF Reader Object is:\n", readerObj

# Details of diveintopython book
print "Details of diveintopython book"
print "Number of pages", readerObj.getNumPages()
print "Title:", readerObj.getDocumentInfo().title
print "Author:", readerObj.getDocumentInfo().author

print "Book Outline"
for heading in readerObj.getOutlines():
    if type(heading) is not list:
        print dict(heading).get('/Title')

print "Reading Page 1"
page = readerObj.getPage(1)
print page.extractText()

pdf.close()